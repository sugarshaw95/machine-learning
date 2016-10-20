file1=open("horse-colic.data.txt")
new1=open("training.txt","w")
file2=open("horse-colic.test.txt")
new2=open("test.txt","w")
for line in file1.readlines():
    currline= line.strip().split()   
    lineArr=[]
    for i in range(22):
        if(currline[i]=="?"):
            lineArr.append("0")
        elif (i!=2):
            lineArr.append(currline[i])
    #print(lineArr)
    if(currline[22]!="?"):
        if(currline[22]!="1"):
            lineArr.append("0")
        else:
            lineArr.append("1")
        for i in range(22):
            new1.write(lineArr[i])
            new1.write(" ")
        new1.write("\n")
new1.close()

for line in file2.readlines():
    currline= line.strip().split()   
    lineArr=[]
    for i in range(22):
        if(currline[i]=="?"):
            lineArr.append("0")
        elif (i!=2):
            lineArr.append(currline[i])
   # print(lineArr)
    if(currline[22]!="?"):
        if(currline[22]!="1"):
            lineArr.append("0")
        else:
            lineArr.append("1")
        for i in range(22):
            new2.write(lineArr[i])
            new2.write(" ")
        new2.write("\n")
new2.close()
