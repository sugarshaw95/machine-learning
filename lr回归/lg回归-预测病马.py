import numpy as np

def loadDataSet(s):
	dataMat=[];labelMat=[]
	frTrain =open(s)
	for line in frTrain.readlines():
		lineArr = line.strip().split(" ")
		lineArr=np.array(lineArr)
		dataMat.append([float(lineArr[i]) for i in range(21)])
								
		labelMat.append(float(lineArr[21]))
	dataMat=np.array(dataMat)
	labelMat=np.array(labelMat)
	return dataMat,labelMat
def judge(x,weights):
		prob=sigmoid(np.sum(x*weights))
		if prob>0.5:
				return 1.0
		else:
				return 0.0
def sigmoid(m):
		return 1.0/(1+np.exp(-m))
def bgd(feature,target,alpha = 0.001,iterateTimes = 500):  
	'... batch gradient descent ...'  
	theta = np.zeros(feature.shape[1])	
	for it in range(iterateTimes):	#max iteratetimes is 200  
		for i in range(feature.shape[0]):	#for each sample  
			error = target[i] - sigmoid(np.sum(feature[i]*theta))  
			theta += alpha*error*feature[i]/feature.shape[0]	   
	predict = [sigmoid(np.sum(theta*sample)) for sample in feature]
	mse = np.sum((predict - target)**2)/feature.shape[0]
	print ('bgd_mse:',mse)	 
	return theta    

def sgd(feature,target,alpha = 0.001,iterateTimes = 1000):#101000	 
	'... stochastic gradient descent ...'  
	theta = np.zeros(feature.shape[1])#num of theta = num of feature atrribute	
	for it in range(iterateTimes):	#max iteratetimes is 200  
		i = it%feature.shape[0]	 #quyu
		error = target[i] - sigmoid(np.sum(feature[i]*theta))#
		theta += alpha*error*feature[i]	 
		   
		predict = [sigmoid(np.sum(feature[i]*theta)) for sample in feature]	 
		mse = np.sum((predict - target)**2)/feature.shape[0]	 
		#if(mse < 21.8498395893):  
			#break	
	print ('sgd_mse : ',mse)  
		  
	return theta


def L2_sgd(feature,target,alpha = 0.001,Lambda = 10 ,iterateTimes = 1000):#L2正则化SGD,lambda为正则项系数
	'... stochastic gradient descent ...'  
	theta = np.zeros(feature.shape[1])#num of theta = num of feature atrribute
	for it in range(iterateTimes):	#max iteratetimes is 200  
		i = it%feature.shape[0]	 
		error = target[i] - sigmoid(np.sum(feature[i]*theta))#对应元素相乘，都是行array  
		theta = ((1.0-alpha*Lambda)*theta)+alpha*error*feature[i]	 
		   
		predict = [sigmoid(np.sum(feature[i]*theta)) for sample in feature]	 
		mse = np.sum((predict - target)**2)/feature.shape[0]	 
		#if(mse < 21.8498395893):  
			#break	
	print ('L2_sgd_mse : ',mse)	 
		  
	return theta  


def L2_sgd_ColicTest():
		trainingset =[]; traininglabels=[]
		PrecStrength =[]; testlabels=[]
		trainingset,traininglabels=loadDataSet("training.txt")
		
		
		trainweights=L2_sgd(np.array(trainingset),np.array(traininglabels))
		print("trainweights:",trainweights)
		print("预测结果与实际对比:")
		frtest=open("test.txt")
		errornum=0; numtest=0.0
		print("index predict truth")
		for line in frtest.readlines():
				numtest+=1.0
				currline=line.strip().split(" ")
				linearr=[]
				linearr.append([float(currline[i]) for i in range(21)])
				#print(judge(np.array(linearr),trainweights)," ",int(currline[21]))
				PrecStrength.append(sigmoid(np.sum(np.array(linearr)*trainweights)))
				print(int(numtest-1),"   ",judge(np.array(linearr),trainweights),"   ",int(currline[21]))
				testlabels.append(float(currline[21]))
				if int(judge(np.array(linearr),trainweights))!=int(currline[21]):
										errornum+=1
		errorrate= (float(errornum)/numtest)
		testlabels=np.array(testlabels)
		print("error rate is %f" % errorrate)
		plotROC(np.array(PrecStrength),testlabels)

		return errorrate,PrecStrength

def sgd_ColicTest():
		trainingset =[]; traininglabels=[]
		trainingset,traininglabels=loadDataSet("training.txt")
		
		
		trainweights=sgd(np.array(trainingset),np.array(traininglabels))
		print("trainweights:",trainweights)
		print(type(trainweights))
		frtest=open("test.txt")
		errornum=0; numtest=0.0
		for line in frtest.readlines():
				numtest+=1.0
				currline=line.strip().split(" ")
				linearr=[]
				linearr.append([float(currline[i]) for i in range(21)])
				#print(judge(np.array(linearr),trainweights)," ",int(currline[21]))
				
				if int(judge(np.array(linearr),trainweights))!=int(currline[21]):
										errornum+=1
		errorrate= (float(errornum)/numtest)
		print("error rate is %f" % errorrate)
		
		return errorrate

def bgd_ColicTest():
		trainingset =[]; traininglabels=[]
		trainingset,traininglabels=loadDataSet("training.txt")
		
		
		trainweights=bgd(np.array(trainingset),np.array(traininglabels))
		print("trainweights:",trainweights)
		print(type(trainweights))
		frtest=open("test.txt")
		errornum=0; numtest=0.0
		for line in frtest.readlines():
				numtest+=1.0
				currline=line.strip().split(" ")
				linearr=[]
				linearr.append([float(currline[i]) for i in range(21)])
				print(judge(np.array(linearr),trainweights)," ",int(currline[21]))
				
				if int(judge(np.array(linearr),trainweights))!=int(currline[21]):
										errornum+=1
		errorrate= (float(errornum)/numtest)
		print(errornum,numtest)
		print("error rate is %f" % errorrate)
		return errorrate

def plotROC(predStrengths,classLabels):
	import matplotlib.pyplot as plt
	cur =(1.0,1.0)
	ysum=0.0
	numpos=0
	for n in classLabels:
		if n==1.0:
			numpos+=1
	print(len(classLabels),numpos)
	ystep=1.0/float(numpos)
	xstep=1.0/float(len(classLabels)-numpos)
	sortedIndex=predStrengths.argsort()
	fig=plt.figure()
	fig.clf()
	ax=plt.subplot(111)
	print(sortedIndex.tolist())
	pnum=0;
	for index in sortedIndex.tolist() :
		if classLabels[index] == 1.0:
			delx=0; dely=ystep;
		else:
			delx=xstep; dely=0;
			ysum+=cur[1]
		pnum+=1;
		ax.plot([cur[0],cur[0]-delx],[cur[1],cur[1]-dely],'o-b')
		cur=(cur[0]-delx,cur[1]-dely)
	print(pnum)
	ax.plot([0,1],[0,1],'b--')
	plt.xlabel("FPR(False Positive Rate)"); plt.ylabel("TPR(True Positive Rate)")
	plt.title("ROC & AUC for Logistic回归")
	ax.axis([0,1,0,1])
	print("AUC is",ysum*xstep)
	plt.show()
	
	

				
		


  
#a=np.array([[1,2,3,4],[2,3,4,5],[4,5,6,7],[9,10,11,12]])
#a=np.random.rand(20,5)
#b=np.random.rand(20,1)
#print(bgd(a,b))
#print(L2_sgd(a,b))
#print(sgd(a,b))

#trainingset,traininglabels=loadDataSet("training.txt")
#print(np.shape(trainingset))
#print(np.shape(traininglabels))
errorrate,prec=L2_sgd_ColicTest()


#print(prec)
#plotROC()
#sgd_ColicTest()
#bgd_ColicTest()
