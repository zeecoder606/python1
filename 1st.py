while(1):
 n= int(raw_input())
 if(n==0):
         break
 a=[]
 count=0
 for i in range(n):
  m=int(raw_input())
  a.append(m)   
 a.sort()
 for k in range(n-1):
  for i in range(k,n-1):
    x=a[k]+a[i+1]
    for j in range(i+2,n):
   	  if(a[j]>x):
   	    count=count+(n-j)
   	    break
 print count



   


    