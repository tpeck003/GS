import random


def generatePref(first, second, size):
    random.seed()
    newLi = []
    #2d array of preferences to be generated
    jk = 0
    while(jk < size):
        jk += 1
        column = []
        for i in range(size + 1):
            column.append("_")
        newLi.append(column)
    for i in range(len(first)):
        usedN = []
        newLi[i][0] = first[i]
        for z in range(len(first)):
            name = second(random.randint(0, ((len(second)) - 1)))
            while (name in usedN ):
                name  = second(random.randint(0, ((len(second)) - 1)))
            newLi[i][z] = name
            usedN.append(name)
    return newLi


def findInd(inList, name):
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
        return 0



def matchGenerator(mL,fL, size):
    inMale = []
    inFemale = []
    sizeL = size
    nMatches = []
    for j in range(sizeL):
        column = []
        for i in range(2):
            column.append(0)
        nMatches.append(column)
    
    
    maleL = generatePref(inMale,inFemale, sizeL)
    femaleL = generatePref(inFemale, inMale, sizeL)
    myStack = []
    for i in range(sizeL):
        myStack.append(mL[i])
    while ((len(myStack)) != 0):
        curr = myStack.pop()
        currInd = findInd(maleL, curr)
        for i in range(len(maleL[0])):
            currF = maleL[currInd][i]
            if (currF != 0):
                x = findInd(nMatches, currF)
                if(x):
                    m1 = findInd(femaleL,curr)
                    m2 = findInd(femaleL,nMatches[x[0]][0])
                    if(m1 > m2):
                        print(curr," tried proposing to ",currF, ",it worked")
                        print("She will now be leaving ",nMatches[x[0]][0]," for him")
                        myStack.append(nMatches[x[0]][0])
                        nMatches[x][0] = curr
                        maleL[currInd][i] = 0
                        #female that just became matched will be purged from male preferences to ensure she is not proposed to again

                    else:
                        print(curr," tried proposing to ",currF, ",it didnt work")
                        maleL[currInd][i] = 0
                        myStack.append(curr)
                else:
                    nMatches[x][0] = curr
                    nMatches[x][1] = currF
                    print(curr, " Proposes to", currF)
                    print("She accepts")
    for j in range(sizeL):
        print(nMatches[j][0]," is matched with ", nMatches[j][1])
                


#test

def main():
    mL = ["j","p","b"]
    fL = ["n","t","c"]
    sizeG = 3
    matchGenerator(mL, fL, sizeG)

if __name__ == "__main__":
    main()
