out = open("out.txt","w")
for test in range(int(input())):
    out.write(f"Case #{test+1}:")
    out.write("\n")
    n = int(input())
    ic = list(input())
    oc = list(input())
    arr = [["N" for i in range(n)]for i in range(n)]
    for i in range(n):
        k = i-1
        while(k>=0and ic[k]=="Y" and oc[k+1]=="Y"):
            arr[i][k] = "Y"
            k-=1
        k = i+1
        while(k<n and ic[k]=="Y" and oc[k-1]=="Y"):
            arr[i][k] ="Y"
            k+=1
        arr[i][i] ="Y"
    for i in range(n):
        for j in range(n):
            out.write(arr[i][j])
        out.write("\n")


