n=int(input("enter number of processes: "))
lis=[]
l=[]
for x in range(n):
    lis.append(tuple(map(int, input("Enter two integers separated by space (ARRIVAL TIME(AT) AND BURST TIME(BT)): ").split())))  #AT AND BT
x5 = sorted(lis, key=lambda x: x[0])
l.append(x5[0])
x5.pop(0)
x = sorted(x5, key=lambda x: x[1])
at=[]
bt=[]
at.append(l[0][0])
bt.append(l[0][1])
for u in x:
    at.append(u[0])
for v in x:
    bt.append(v[1])
count1=len(x)
x.insert(0,l[0])
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
    print("the process's arrival time ",at[r],"waited for",rse)
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
    print("the process's arrival time ",at[r1],"completed in",rse1)
    r1=r1+1



#TAT CALCULATION

r2=0
cu=0
for d in ct:
    print("the process's arrival time ",at[r2],"turn around time is",d-at[cu])
    cu=cu+1
    r2=r2+1
