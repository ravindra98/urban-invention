//program for R-category continuous perceptron traniing algorithm with sample data
import math//Impprted math library
def sgn(net):
    temp=math.e**(-net)
    return (1-temp)/(1+temp)
X=[[10,2],[2,-5],[-5,5]]
D=[[1,-1,-1],[-1,1,-1],[-1,-1,1]]
W=[[1,-2,0],
   [0,-1,2],
   [1,3,-1]]
Y=[]
for x in X:
    y=x
    y.append(-1)
    Y.append(y)
print "Y:",Y
print "W:",W
c=1.0
Emax=0.001
cycles=0
while(1):
    E=0
    for inp in range(len(Y)): 
        y=Y[inp]
        d=D[inp]
        o=[]
        k=0
        i=0
        for w in W:
            net=0
            for i in range(len(w)):
                net+=w[i]*y[i]
            o.append(round(sgn(net),3))
        print o
        print "======"
        for k in range(len(D[0])):
            diff=d[k]-o[k]
            if(diff!=0):
                for j in range(len(W[0])):
                    #print W[k][j]
                    (W[k][j])+=round(0.5*c*(diff)*y[j],3)
            for wei in range(len(W)):
                for wej in range(len(W[0])):
                    W[wei][wej]=round(W[wei][wej],3)
            print W
            E+=0.5*(diff*diff)
        cycles+=1
    if(round(E)<Emax):
        break
