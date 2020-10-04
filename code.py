import numpy as np
import matplotlib.pyplot as plt
x=[1,2,5,3,6,7,3.5]; y=[4,6,7,7,9,10,9]
def S(x,x1,y,y1): #create the function to calculate the sumation
    n=0
    for i in range(0,len(x)):
        n=n+x[i]**x1*y[i]**y1
    return(n)
def R(n):
  plt.scatter(x,y,color='k')
  for k in range(0,n):
    M=[]
    for j in range(0,k+2):
        M0=[]
        for i in range(0,k+2):
            M0.append(S(x,j+i,y,0))
        M.append(M0) 
    M=np.array(M)
    B=[]
    for j in range(0,k+2) :
        B.append([S(x,j,y,1)])
    B=np.array(B)
    Minv=np.linalg.inv(M)
    a=Minv.dot(B)
    xplot=np.linspace(min(x),max(x),100)
    yplot=0
    for i in range(0,k+2):
        yplot=yplot+a[i]*xplot**i
    plt.plot(xplot,yplot)
#input in funtion R will give polynomail degree 1 to n where n is input    
print(R(4))
