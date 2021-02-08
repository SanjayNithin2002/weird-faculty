def exam(v):
    for k in range(len(v)):
        b,c=0,0
        for i in range(k):
            if v[i]==1:b+=1
            elif v[i]==0:b-=1
        for j in range(k,len(v)):
                if v[j]==1:c+=1
                elif v[j]==0:c-=1
        if b>c:
                return k

v=[int(input()) for i in range(int(input()))]
print(exam(v))

