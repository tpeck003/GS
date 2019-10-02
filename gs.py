import random
import time

def generatePref(first, second, size):
    random.seed(time.time())
    newLi = []
    #2d list of preferences to be generated
    jk = 0
    while(jk < size):
        jk += 1
        column = []
        for i in range(size + 1):
            column.append("_")
        newLi.append(column)
    #populates the 2d list we need for list of prefernces
    for i in range(0,size):
        usedN = []
        #list of used names so we do not have repeats on the prefernce list
        newLi[i][0] = first[i]
        #puts the name of the person to have matches generated for as the first index
        for z in range(1,(size + 1)):
            name = second[random.randint(0, size - 1)]
            #generates a random name
            while (name in usedN ):
                name  = second[random.randint(0, size - 1)]
                #retries until an unused name has been generated
            newLi[i][z] = name
            usedN.append(name)
            #adds name to the used list
    print(newLi)
    #printing just for test purposes
    return newLi
    #returns this 2d list

def findInd(inList, name):
    #finds the index of any name inside a list, necessary for many parts of the function below
    retList = [0,0]
    found = 0
    for i in range(len(inList)):
          for j in range(len(inList[0])):
            if (inList[i][j] == name):
                retList[0] = i
                retList[1] = j
                found = 1
    if(found):
        return retList
    else:
        retAlt = []
        return retAlt


def matchGenerator(mL,fL, size):
    inMale = mL
    inFemale = fL
    sizeL = size
    nMatches = []
    maleL = generatePref(inMale,inFemale, sizeL)
    femaleL = generatePref(inFemale, inMale, sizeL)
    myStack = []
   
    for i in range(sizeL):
        myStack.append(mL[i]) 
    print(myStack)
    while ((len(myStack)) != 0):
        #Loops as long as there are males left to be matched
        curr = myStack.pop()
        #loading the next male to attempt matching from the stack
        currInd = findInd(maleL, curr)
        #finding the index of this male in the male preference list so we can find his preferences
        for i in range(1,(sizeL + 1)):
        #for the range of preferences of the male at that index
            currF = maleL[currInd[0]][i]
            #iterating through his prefernces and assigning each female to the current
            if (currF != "_"):
                #making sure he hasnt tried to propose to this female before
                x = findInd(nMatches, currF)
                #checking to see if she is matched already
                if(len(x) > 1):
                    #if she is matched
                    m1 = findInd(femaleL,curr)
                    #finding the index of current male on female preference list
                    m2 = findInd(femaleL,nMatches[x[0]][0])
                    #finding the index of the currently matched male on the female preference list
                    if(m1 > m2):
                        #if she would prefer this new male to the older male
                        print(curr," tried proposing to ",currF, ",it worked")
                        print("She will now be leaving ",nMatches[x[0]][0]," for him")
                        myStack.append(nMatches[x[0]][0])
                        nMatches[x[0]][0] = curr
                        maleL[currInd[0]][i] = "_"
                        #removes this female from the male prefernce list
                        break
                        #female that just became matched will be purged from male preferences to ensure she is not proposed to again

                    else:
                        #if she prefers her current partner
                        print(curr," tried proposing to ",currF, ",it didnt work")
                        maleL[currInd[0]][i] = "_"
                        myStack.append(curr)
                        break
                else:
                    #if she is not matched
                    nMatches.append([curr,currF])
                    print(curr, " Proposes to", currF)
                    print("She accepts")
                    break
    for j in range(sizeL):
        #printing all of the matches
        print(nMatches[j][0]," is matched with ", nMatches[j][1])
                




def main():
    start = time.time()
    with open('names.txt') as f:
        lines = f.read().splitlines()
        #reads file of names into list. Ordered male first then female first
    size = (len(lines)/2)
    mL = []
    fL = []
    for i in range(len(lines)):
        if(i < size):
            mL.append(lines[i])
        if(i >= size):
            fL.append(lines[i])
        #splits list between male and female names
    print(mL)
    #prints the list of names
    print(fL)
    sizeG = size
    matchGenerator(mL, fL, sizeG)
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()
