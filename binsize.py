import statistics as st
print("enter the values to bin")
a=list(map(int,input().split()))
bins=[]
print("\n Enter the no f bins")
n=int(input())
k=0
ar=[]
for i in range(n):
    print("\n enter bin ",i,"size")
    size=int(input())
    bins.append(a[k:k+size])
    k+=size
for i in bins:
    for j in i:
        ar.append(st.mean(i))
    print("\n bin",i,"mean is")
    print(st.mean(i))
    print("\n After bining elements od  bin", i ,"are:")
    for m in i:
        print(m,end="  ")