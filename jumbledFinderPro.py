
import copy

#balancedObject = []

def manageBalancedDetails(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftEndPos,rightStartPos,rightEndPos,rightSetCombination):
    dictDetails = {}
    dictDetails['leftSet'] = leftSet
    dictDetails['rightSet'] = rightSet
    dictDetails['leftStartPos'] = leftStartPos + len(dataSet) - len(testDataSet)
    dictDetails['leftEndPos'] = leftEndPos + len(dataSet) - len(testDataSet)
    dictDetails['rightStartPos'] = rightStartPos + len(dataSet) - len(testDataSet)
    dictDetails['rightEndPos'] = rightEndPos + len(dataSet) - len(testDataSet)
    balancedObject.append(dictDetails)
    if(leftEndPos < rightStartPos - 1):
        leftEndPos += 1
        leftSet = leftSet + [testDataSet[leftEndPos]]
        extraLeftCharAdded = [testDataSet[leftEndPos]]
        fixRight(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftEndPos,rightStartPos,rightEndPos,extraLeftCharAdded,rightSetCombination)
def fixLeft(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftEndPos,rightStartPos,rightEndPos,deltaRight,rightSetCombination):
    extraLeftCharAdded = []
    flag = False
    leftNewPos = 0
    deltaRightCopy = copy.deepcopy(deltaRight)
    while(True):
        for i in range(leftEndPos+1,rightStartPos):
            leftNewPos = i
            leftSet.append(testDataSet[i])
            if(testDataSet[i] == deltaRightCopy[0]):
                deltaRightCopy.remove(testDataSet[i])
                flag = True
                break
            else:
                flag2 = False
                for j in range (1, len(deltaRightCopy)):
                    if(testDataSet[i] == deltaRightCopy[j]):
                        deltaRightCopy.remove(testDataSet[i])
                        flag2 = True
                        break
                if not flag2:
                    extraLeftCharAdded.append(testDataSet[i])
        if((deltaRightCopy) == []):
            break
        else:
            if not flag:
                return 0
            else:
                leftEndPos = leftNewPos
                flag = False
    if(flag):
        if(extraLeftCharAdded == []):
            manageBalancedDetails(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftNewPos,rightStartPos,rightEndPos,rightSetCombination)
        else:
            fixRight(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftNewPos,rightStartPos,rightEndPos,extraLeftCharAdded,rightSetCombination)
    else:
        return 0
def fixRight(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftEndPos,rightStartPos,rightEndPos,deltaLeft,rightSetCombination=[]):
    extraRightAdded = []
    extraRightTemp = []
    while(True):
        extraRightAddedAtLeft = []
        extraRightAddedAtRight = []
        #find left occ if any
        if(deltaLeft == []):
            break
        valToFind = deltaLeft[0]
        #raw_input('chk')
        leftLoc = [False,float('inf')]
        rightLoc = [False,float('inf')]
        valToFindTestLeft = copy.deepcopy(deltaLeft)
        rightSetLeftTest = copy.deepcopy(rightSet)
        valToFindTestRight = copy.deepcopy(deltaLeft)
        rightSetRightTest = copy.deepcopy(rightSet)
        #if (valToFind != startCharacter):
        for i in range(rightStartPos-1,leftEndPos,-1):
            rightSetLeftTest = [testDataSet[i]] + rightSetLeftTest
            if(testDataSet[i] == valToFind):
                valToFindTestLeft.remove(testDataSet[i])
                leftLoc[0] = True
                leftLoc[1] = i
                break
            else:
                flag2 = False
                for j in range (0, len(valToFindTestLeft)):
                    if(testDataSet[i] == valToFindTestLeft[j]):
                        valToFindTestLeft.remove(testDataSet[i])
                        flag2 = True
                        break
                if not flag2:
                    extraRightAddedAtLeft.append(testDataSet[i])
        for i in range(rightEndPos + 1,len(testDataSet)):
            rightSetRightTest.append(testDataSet[i])
            if(testDataSet[i] == valToFind):
                valToFindTestRight.remove(testDataSet[i])
                rightLoc[0] = True
                rightLoc[1] = i
                break
            else:
                flag2 = False
                for j in range (1, len(valToFindTestRight)):
                    if(testDataSet[i] == valToFindTestRight[j]):
                        valToFindTestRight.remove(testDataSet[i])
                        flag2 = True
                        break
                if not flag2:
                    extraRightAddedAtRight.append(testDataSet[i])

        if(rightLoc[0]):
            dictToStore = {}
            dictToStore['rightStartPos'] = copy.deepcopy(rightStartPos)
            dictToStore['rightEndPos'] = copy.deepcopy(rightLoc[1])
            dictToStore['leftStartPos'] = copy.deepcopy(leftStartPos)
            dictToStore['leftEndPos'] = copy.deepcopy(leftEndPos)
            dictToStore['extraRightTemp'] = copy.deepcopy(extraRightTemp + extraRightAddedAtRight)
            dictToStore['leftSet'] = copy.deepcopy(leftSet)
            dictToStore['rightSet'] = copy.deepcopy(rightSetRightTest)
            dictToStore['deltaLeft'] = copy.deepcopy(valToFindTestRight)
            rightSetCombination.append(dictToStore)

        if(leftLoc[0]):
            dictToStore = {}
            dictToStore['rightStartPos'] = copy.deepcopy(leftLoc[1])
            dictToStore['rightEndPos'] = copy.deepcopy(rightEndPos)
            dictToStore['leftStartPos'] = copy.deepcopy(leftStartPos)
            dictToStore['leftEndPos'] = copy.deepcopy(leftEndPos)
            dictToStore['extraRightTemp'] = copy.deepcopy(extraRightAddedAtLeft + extraRightTemp)
            dictToStore['leftSet'] = copy.deepcopy(leftSet)
            dictToStore['rightSet'] = copy.deepcopy(rightSetLeftTest)
            dictToStore['deltaLeft'] = copy.deepcopy(valToFindTestLeft)
            rightSetCombination.append(dictToStore)
        anyRightFixRemaining = False
        for i in range(0,len(rightSetCombination)):
            if(len(rightSetCombination[i]['deltaLeft']) != 0):
                rightStartPos = copy.deepcopy(rightSetCombination[i]['rightStartPos'])
                rightEndPos = copy.deepcopy(rightSetCombination[i]['rightEndPos'])
                leftStartPos = copy.deepcopy(rightSetCombination[i]['leftStartPos'])
                leftEndPos = copy.deepcopy(rightSetCombination[i]['leftEndPos'])
                extraRightTemp = copy.deepcopy(rightSetCombination[i]['extraRightTemp'])
                rightSet = copy.deepcopy(rightSetCombination[i]['rightSet'])
                leftSet = copy.deepcopy(rightSetCombination[i]['leftSet'])
                deltaLeft = copy.deepcopy(rightSetCombination[i]['deltaLeft'])
                anyRightFixRemaining = True
                del rightSetCombination[i]
                break
        if(anyRightFixRemaining == False):
            break
    #print rightSetCombination

    if(deltaLeft == []):
        manageBalancedDetails(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftEndPos,rightStartPos,rightEndPos,rightSetCombination)
        return 0
    if(len(rightSetCombination) == 0):
        return 0
    else:
        for count in rightSetCombination:
            rightSetCombinationData = rightSetCombination[0]
            rightStartPos = copy.deepcopy(rightSetCombinationData['rightStartPos'])
            rightEndPos = copy.deepcopy(rightSetCombinationData['rightEndPos'])
            extraRightTemp = copy.deepcopy(rightSetCombinationData['extraRightTemp'])
            rightSet = copy.deepcopy(rightSetCombinationData['rightSet'])
            leftStartPos = copy.deepcopy(rightSetCombinationData['leftStartPos'])
            leftEndPos = copy.deepcopy(rightSetCombinationData['leftEndPos'])
            leftSet = copy.deepcopy(rightSetCombinationData['leftSet'])
            if(extraRightTemp == []):
                rightSetCombination.remove(rightSetCombinationData)
                manageBalancedDetails(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftEndPos,rightStartPos,rightEndPos,rightSetCombination)
            else:
                rightSetCombination.remove(rightSetCombinationData)
                a = fixLeft(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftEndPos,rightStartPos,rightEndPos,extraRightTemp,rightSetCombination)
def controller(balancedObject,dataSet):
    lenOrig = len(dataSet)
    for i in range(0,lenOrig):
        testDataSet = dataSet[i:]
        startCharacter = testDataSet[0]
        testSetLocation = []
        for j in range(0,len(testDataSet)):
            if(testDataSet[j] == startCharacter):
                testSetLocation.append(j)
        for index in range(1,len(testSetLocation)):
            leftSet = [startCharacter]
            rightSet = [startCharacter]
            leftStartPos = leftEndPos = 0
            rightStartPos = rightEndPos = testSetLocation[index]
            deltaLeft = []
            fixRight(balancedObject,dataSet,testDataSet, leftSet,rightSet,leftStartPos,leftEndPos,rightStartPos,rightEndPos,deltaLeft)
def main(dataString,heuristicData = []):
    #testStringOriginal ='1153135511422417667110715531153421421167716615355351112424161767124445624562456258356335133'
    testDataSet = []
    for data in dataString:
        testDataSet.append(data)
    #testDataSet =[3,5,1,3,5,5,1,1,4,2,2,4,1,7,6,6,7,1,1,0,7,1,5,3,5,1,1,5,3,4,2,1,4,2,1,1,6,7,7,1,6,6,1,5,3,5,5,3,5,1,1,1,2,4,2,4,1,6,1,7,6,7,1]
    balancedObject = []
    controller(balancedObject,testDataSet)

    #print balancedObject
    largestPtrn = []

    #filtering and grouping the patterns
    countPatternCombination = len(balancedObject)
    patternDictList = []
    index = -1

    for ele in balancedObject:
        rightSet1 = ele['rightSet']
        leftSet1 = ele['leftSet']
    setsConsidered = []
    for ele in balancedObject:
        index += 1
        leftSet1 = ele['leftSet']
        if(leftSet1 in setsConsidered):
            continue
        rightSet1 = ele['rightSet']
        leftStartPos1 = ele['leftStartPos']
        leftEndPos1 = ele['leftEndPos']
        rightStartPos1 = ele['rightStartPos']
        rightEndPos1 = ele['rightEndPos']
        patternDict = {}
        patternDict['leftSet'] = leftSet1
        patternDict['rightSets'] = [rightSet1]
        patternDict['patterns'] = [leftSet1,rightSet1]
        patternDict['occurrences'] = [[leftStartPos1,leftEndPos1],[rightStartPos1,rightEndPos1]]
        
        setsConsidered.append(leftSet1)
        setsConsidered.append(rightSet1)
        for ele2 in balancedObject[index+1:]:
            leftSet2 = ele2['leftSet']
            rightSet2 = ele2['rightSet']
            leftStartPos2 = ele2['leftStartPos']
            leftEndPos2 = ele2['leftEndPos']
            rightStartPos2 = ele2['rightStartPos']
            rightEndPos2 = ele2['rightEndPos']
            countRightSets = len(patternDict['rightSets'])

            if(leftSet2 == leftSet1):
                rightSetPresent = False
                for k in range(0,countRightSets):
                    if(rightSet2 == patternDict['rightSets'][k]):
                        rightSetPresent = True
                        if([rightStartPos2,rightEndPos2] not in patternDict['occurrences']):
                            patternDict['patterns'].append(rightSet2)
                            patternDict['rightSets'].append(rightSet2)
                            patternDict['occurrences'].append([rightStartPos2,rightEndPos2])
                if not rightSetPresent:
                    patternDict['patterns'].append(rightSet2)
                    patternDict['rightSets'].append(rightSet2)
                    patternDict['occurrences'].append([rightStartPos2,rightEndPos2])

        patternDictList.append(patternDict)
    
    result = findMostPromisingDataSet(patternDictList)
    return result
def findMostPromisingDataSet(patternDictList):
    largestPtrn = []
    obj = None
    #print patternDict2
    for ele in patternDictList:
        #print ele
        if(len(ele['leftSet']) > len(largestPtrn)):
            largestPtrn = ele['leftSet']
            obj = ele
    return obj
def init():
    #testStringOriginal ='153355114224176671107155311534214211677166153553511124241617671'
    #testStringOriginal ='1153135511422417667110715531153421421167716615355351112424161767124445624562456258356335133'
    #testStringOriginal ='123123123'
    testStringOriginal = raw_input('input data set')
    result = main(testStringOriginal)
    print result
init()