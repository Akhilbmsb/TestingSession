import os,csv,test_math
import pandas as pd

def findFailedStatus():
    found = False
    dataset = pd.read_csv('testreport.csv')
    for i in range(len(dataset)):
        if(dataset == True):
            found = dataset.loc[i][5] == 'failed'      
    return found

def mergeCodeToReleaseBranch():
    # os.system('git add .')
    # os.system('git commit -m "adding code from dev to release through automation# AUTOMATED"')  
    # os.system('git push origin release"')
    print("message added")


def runOsCommand():
    testpassed = findFailedStatus()
    if (testpassed == True):
        mergeCodeToReleaseBranch()
    else:
        print("test case failed")   
        




        