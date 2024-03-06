#WT CALCULATION

n=int(input("enter number of processes: "))
l=[]
for x in range(n):
    l.append(tuple(map(int, input("Enter two integers separated by space (ARRIVAL TIME(AT) AND BURST TIME(BT)): ").split())))  #AT AND BT    
x = sorted(l, key=lambda x: x[0])
at=[]
bt=[]
for u in x:
    at.append(u[0])
ats=sorted(at)
for v in x:
    bt.append(v[1])
count1=len(x)-1
x1=0   
res=0
le=[]
for y in range(count1):
    acc=bt[y]
    res=res+acc
    le.append(res)
result=[]
k=1
for z in le:
    result.append(z-at[k])
    k=k+1
y=1
r=0
result.insert(0,0)
for rse in result:
    print("the process's arrival time ",ats[r],"waited for",rse)
    y=y+1
    r=r+1

#CT CALCULATION

BT1=[]
for v in x:
    BT1.append(v[1])
count1=len(BT1)
x1=0   
res2=0
ct=[]
for y2 in range(count1):
    acc=BT1[y2]
    res2=res2+acc
    ct.append(res2)
r1=0
for rse1 in ct:
    print("the process's arrival time ",ats[r1],"completed in",rse1)
    r1=r1+1



#TAT CALCULATION

r2=0
cu=0
for d in ct:
    print("the process's arrival time ",ats[r2],"turn around time is",d-at[cu])
    cu=cu+1
    r2=r2+1





    
    
    
