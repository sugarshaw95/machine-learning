def pre_deal():
    file1=open("imp.20131027.txt")
    file2=open("clk.20131027.txt")
    f_out=open("training.txt","w")
    file3=open("rawtest.txt")
    f_out2=open("test.txt","w")
        
    idset2=[]
    sum1=0
    sum2=0
    for line in file2.readlines():
        currline=line.strip().split()
        if(currline):
            sum1+=1
            #print(currline[0])
            idset2.append(currline[0])
    #统计click中出现的id,存在idset2中



    count1=0
    count2=0
    count3=0
    count4=0
    flags=[]
    for i in range(500):
        flags.append(0)

    
    for line in file1.readlines():
        currline= line.strip().split()
        c_len=len(currline)
        id=currline[0]
        res=0
        pre=0
        for it in idset2:
            if(id==it):
                res=1
                break
        ###看这个imp是不是在click里,是则res为1,否则为0
        if(res):
            sum2+=1
            #print(res)

        if((res==0) and count1>5000):
            continue
        
        lineArr=[]


         #区域ID
        d1={"0":0,"1":1,"2":2,"3":3,"15":4,"27":5,"40":6,"55":7,"65":8,"79":9,"80":10,"94":11,
            "106":12,"124":13,"134":14,"146":15,"164":16,"183":17,"201":18,"216":19,"238":20,
            "253":21,"275":22,"276":23,"298":24,"308":25,"325":26,"333":27,"344":28,"359":29,
            "368":30,"374":31,"393":32,"394":33,"395":34}
        
        if(currline[c_len-18] in d1):
            lineArr.append(str(d1[currline[c_len-18]]+pre))
        pre+=34
        if(d1[currline[c_len-18]]==19):
            count4+=1
        #城市ID
        if(int(currline[c_len-17])<=392):
            lineArr.append(str(int(currline[c_len-17])+pre))      
        pre+=392
        
        d3={"1":0,"2":1,"3":2,"4":3,"5":4}

        if(currline[c_len-16] in d3):
            lineArr.append(str(d3[currline[c_len-16]]+pre))
          #交易平台
        pre+=5
        #lineArr.append(currline[c_len-11]) #位宽

        #lineArr.append(currline[c_len-10]) #位高


        d4={"Na":0,"FirstView":1,"SecondView":2,"ThirdView":3,"FourthView":4,"FifthView":5,
            "SixthView":6,"SeventhView":7,"EighthView":8,"NinthView":9,"TenthView":10,"OtherView":11}
        
        if(currline[c_len-9] in d4):
            lineArr.append(str(d4[currline[c_len-9]]+pre))
        pre+=12
         #可见性

        d5={"Na":0,"Fixed":1,"Pop":2,"Float":3,"Background":4}

        if(currline[c_len-8] in d5):
            lineArr.append(str(d5[currline[c_len-8]]+pre))
        pre+=5
          #广告位形式

        #lineArr.append(currline[c_len-7]) #底价

        #lineArr.append(currline[c_len-5]) #出价
        #lineArr.append(currline[c_len-4]) #成交价格
        
        label=[]
        labels=[]
        for t in currline[len(currline)-1]:
            if(t==','):
                label="".join(label)
                labels.append(label)
                label=[]
            else:
                label.append(t)
        label="".join(label)
        labels.append(label) 
        #print(labels)  #用户标签,在labels里

        d6={"10006":0,"10024":1,"10031":2,"10048":3,"10052":4,"10057":5,"10059":6,"10063":7,"10067":8,"10074":9,
           "10075":10,"10076":11,"10077":12,"10079":13,"10083":14,"10093":15,"10102":16,"10684":17,"11092":18,
           "11278":19,"11379":20,"11423":21,"11512":22,"11576":23,"11632":24,"11680":25,"11724":26,"11944":27,
           "13042":28,"13403":29,"13496":30,"13678":31,"13776":32,"13800":33,"13866":34,"13874":35,"14273":36,
           "16593":37,"16617":38,"16661":39,"16706":40,"16751":41,"10110":42,"10111":43}
        for it in labels:
            if(it in d6):
                lineArr.append(str(d6[it]+pre))
                  #转化成one-hot...

        pre+=len(d6)
        #print(pre)

        #print(lineArr)

        if(res):
            lineArr.append("1")
        else:
            lineArr.append("0")

        
        for i in range(len(lineArr)):
            f_out.write(lineArr[i])
            f_out.write(" ")
        f_out.write("\n")

        if(res==0):
            count1+=1
        

    f_out.close()
    print("training count4:",count4)

    count2=0
    count3=0
    count4=0
    count5=0
    for line in file3.readlines():
        
        currline= line.strip().split()
        c_len=len(currline)
        id=currline[0]
        pre=0

        if(currline[c_len-2]=="0" and count2>1500):
            continue
        elif(currline[c_len-2]!="0" and count3>50):
            continue
             #控制test文件规模
        if(d1[currline[c_len-20]]==19 and count4>500):
            continue
        if(currline[c_len-2]=="0"):
            count2+=1
        else:
            count3+=1        
        lineArr=[]
        if(currline[c_len-2]!="0" and d1[currline[c_len-20]]!=19):
           count5+=1

         #区域ID
        d1={"0":0,"1":1,"2":2,"3":3,"15":4,"27":5,"40":6,"55":7,"65":8,"79":9,"80":10,"94":11,
            "106":12,"124":13,"134":14,"146":15,"164":16,"183":17,"201":18,"216":19,"238":20,
            "253":21,"275":22,"276":23,"298":24,"308":25,"325":26,"333":27,"344":28,"359":29,
            "368":30,"374":31,"393":32,"394":33,"395":34}
        
        if(currline[c_len-20] in d1):
            lineArr.append(str(d1[currline[c_len-20]]+pre))
        if(d1[currline[c_len-20]]==19):
            count4+=1
        pre+=34
        
        #城市ID
        if(int(currline[c_len-19])<=392):
            lineArr.append(str(int(currline[c_len-19])+pre))      
        pre+=392
        
        d3={"1":0,"2":1,"3":2,"4":3,"5":4}

        if(currline[c_len-18] in d3):
            lineArr.append(str(d3[currline[c_len-18]]+pre))
          #交易平台
        pre+=5
        #lineArr.append(currline[c_len-11]) #位宽

        #lineArr.append(currline[c_len-10]) #位高


        d4={"Na":0,"FirstView":1,"SecondView":2,"ThirdView":3,"FourthView":4,"FifthView":5,
            "SixthView":6,"SeventhView":7,"EighthView":8,"NinthView":9,"TenthView":10,"OtherView":11}
        
        if(currline[c_len-11] in d4):
            lineArr.append(str(d4[currline[c_len-11]]+pre))
        pre+=12
         #可见性

        d5={"Na":0,"Fixed":1,"Pop":2,"Float":3,"Background":4}

        if(currline[c_len-10] in d5):
            lineArr.append(str(d5[currline[c_len-10]]+pre))
        pre+=5
          #广告位形式

        #lineArr.append(currline[c_len-7]) #底价

        #lineArr.append(currline[c_len-5]) #出价
        #lineArr.append(currline[c_len-4]) #成交价格
        
        label=[]
        labels=[]
        for t in currline[len(currline)-3]:
            if(t==','):
                label="".join(label)
                labels.append(label)
                label=[]
            else:
                label.append(t)
        label="".join(label)
        labels.append(label) 
        #print(labels)  #用户标签,在labels里

        d6={"10006":0,"10024":1,"10031":2,"10048":3,"10052":4,"10057":5,"10059":6,"10063":7,"10067":8,"10074":9,
           "10075":10,"10076":11,"10077":12,"10079":13,"10083":14,"10093":15,"10102":16,"10684":17,"11092":18,
           "11278":19,"11379":20,"11423":21,"11512":22,"11576":23,"11632":24,"11680":25,"11724":26,"11944":27,
           "13042":28,"13403":29,"13496":30,"13678":31,"13776":32,"13800":33,"13866":34,"13874":35,"14273":36,
           "16593":37,"16617":38,"16661":39,"16706":40,"16751":41,"10110":42,"10111":43}
        for it in labels:
            if(it in d6):
                lineArr.append(str(d6[it]+pre))
                  #转化成one-hot...

        pre+=len(d6)
        #print(pre)

        #print(lineArr)
        if(currline[c_len-2]!="0"):
            lineArr.append("1")
        else:
            lineArr.append("0")
        
        for i in range(len(lineArr)):
            f_out2.write(lineArr[i])
            f_out2.write(" ")
        f_out2.write("\n")

        '''if(res==0):
            count1+=1       
        currline= line.strip().split()
        c_len=len(currline)        
        lineArr=[]
        if(currline[c_len-2]=="0"):
            count2+=1
        else:
            count3+=1

        if(currline[c_len-2]=="0" and count2>1200):
            continue
        elif(currline[c_len-2]!="0" and count3>80):
            continue


         #区域ID
        d1={"0":0,"1":1,"2":2,"3":3,"15":4,"27":5,"40":6,"55":7,"65":8,"79":9,"80":10,"94":11,
            "106":12,"124":13,"134":14,"146":15,"164":16,"183":17,"201":18,"216":19,"238":20,
            "253":21,"275":22,"276":23,"298":24,"308":25,"325":26,"333":27,"344":28,"359":29,
            "368":30,"374":31,"393":32,"394":33,"395":34}

        labels_ap=[]

        for i in range(35):
            labels_ap.append("0")

        if(currline[c_len-20] in d1):
            labels_ap[d1[currline[c_len-20]]]="1"
        for i in range(35):
            lineArr.append(labels_ap[i])

       
        #currline[c_len-17] #城市ID,先不弄了
        

            
        d3={"1":0,"2":1,"3":2,"4":3,"5":4}
        labels_ap=[]

        for i in range(5):
            labels_ap.append("0")
        if(currline[c_len-18] in d3):
            labels_ap[d3[currline[c_len-18]]]="1"
        for i in range(5):
            lineArr.append(labels_ap[i])  #交易平台

        #lineArr.append(currline[c_len-13]) #位宽

        #lineArr.append(currline[c_len-12]) #位高


        d4={"Na":0,"FirstView":1,"SecondView":2,"ThirdView":3,"FourthView":4,"FifthView":5,
            "SixthView":6,"SeventhView":7,"EighthView":8,"NinthView":9,"TenthView":10,"OtherView":11}
        labels_ap=[]

        for i in range(12):
            labels_ap.append("0")
        if(currline[c_len-11] in d4):
            labels_ap[d4[currline[c_len-11]]]="1"
        for i in range(12):
            lineArr.append(labels_ap[i]) #可见性

        d5={"Na":0,"Fixed":1,"Pop":2,"Float":3,"Background":4}
        labels_ap=[]

        for i in range(5):
            labels_ap.append("0")
        if(currline[c_len-10] in d5):
            labels_ap[d5[currline[c_len-10]]]="1"
        for i in range(5):
            lineArr.append(labels_ap[i])    #广告位形式

        #lineArr.append(currline[c_len-9]) #底价

        #lineArr.append(currline[c_len-7]) #出价
        #lineArr.append(currline[c_len-6]) #成交价格
        
        label=[]
        labels=[]
        for t in currline[len(currline)-3]:
            if(t==','):
                label="".join(label)
                labels.append(label)
                label=[]
            else:
                label.append(t)
        label="".join(label)
        labels.append(label) 
        #print(labels)  #用户标签,在labels里

        labels_ap=[]
        for i in range(44):
            labels_ap.append("0")
        d6={"10006":0,"10024":1,"10031":2,"10048":3,"10052":4,"10057":5,"10059":6,"10063":7,"10067":8,"10074":9,
           "10075":10,"10076":11,"10077":12,"10079":13,"10083":14,"10093":15,"10102":16,"10684":17,"11092":18,
           "11278":19,"11379":20,"11423":21,"11512":22,"11576":23,"11632":24,"11680":25,"11724":26,"11944":27,
           "13042":28,"13403":29,"13496":30,"13678":31,"13776":32,"13800":33,"13866":34,"13874":35,"14273":36,
           "16593":37,"16617":38,"16661":39,"16706":40,"16751":41,"10110":42,"10111":43}
        for it in labels:
            if(it in d6):
                labels_ap[d6[it]]="1"  #转化成one-hot...
        for i in range(44):
            lineArr.append(labels_ap[i])

        if(currline[c_len-2]!="0"):
            lineArr.append("1")
        else:
            lineArr.append("0")
        for i in range(len(lineArr)):
            f_out2.write(lineArr[i])
            f_out2.write(" ")
        f_out2.write("\n")'''
        
    f_out2.close()
    print("count2:",count2)
    print("count3:",count3)
    print("216:",count4)
    print("count5:",count5)
    

        


        
    #print("sum2:",sum2)
pre_deal()


