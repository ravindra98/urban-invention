import math
import random
y=int(raw_input("Enter number of inputs: "))
x=[]
d=[]
w=[]
print("Enter the input vectors:")
for i in range(y):
    line=raw_input()
    x1=[float(a) for a in line.split()]
    x.append(x1)
for x1 in x:
    x1.append(-1)
print("Enter the desired class of each input vector")
for i in range(y):
    line=raw_input()
    d1=[int(a) for a in line.split()]
    d.append(d1)
print("Enter Weight vector")
for i in range(y):
    line=raw_input()
    w1=[float(a) for a in line.split()]
    w.append(w1)
flag=True
Trainingcycle=1
while(flag):
    flag=False
    print "Trainingcycle:",Trainingcycle
    for i in range(len(w)):
        print "step:",(i+1)
        output=[]
        for j in range(len(x)):
            sum1=0
            for m in range(len(w[j])):
                sum1=sum1+(w[j][m]*x[i][m])
            if sum1>0:
                out=1
            elif sum1<0:
                out=-1
            output.append(out)
        print output,d[i]
        desired=True
        for k in range(len(output)):
            if output[k]!=d[i][k]:
                desired=False
                break;
        if desired==False:
                for l in range(len(w)):
                    w[k][l]=w[k][l]+(((d[i][k]-output[k])/2)*x[i][l])
        for p in w:
            print p
    if desired==False:
        flag=True
    Trainingcycle+=Trainingcycle
