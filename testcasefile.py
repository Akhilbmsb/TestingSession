import os,test_math
import pandas as pd

def findFailedStatus():
    found = False
    dataset = pd.read_csv('testreport.csv')
    for i in range(len(dataset)):
        if(dataset.loc[i][6] == 'failed'):
            found = True
    return found

def mergeCodeToReleaseBranch():
    print('inside mergeCodeToRelease')
    os.system('git checkout release')
    os.system('git merge dev')
    os.system('git add .')
    os.system('git commit -m "AUTOMATED# Adding code from dev to release through automation"')  
    os.system('git push origin release"')

def runAllTests():
    os.system('python -m pytest')
    
def runOsCommand():
    runAllTests()
    testpassed = findFailedStatus()
    print('test-passed', testpassed)
    if (testpassed == True):
        mergeCodeToReleaseBranch()
    else:
        print("test case failed")   

runOsCommand()




        