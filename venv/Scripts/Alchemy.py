out = open("output.txt","w")
for test in range(int(input())):
    n = int(input())
    stones = input()
    count_a,count_b=0,0
    count_a = stones.count("A")
    count_b = stones.count("B")
    if(abs(count_a-count_b)<3):
        out.write(f"Case #{test+1}: Y")
    else:
        out.write(f"Case #{test+1}: N")
    out.write("\n")