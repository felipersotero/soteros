N = int(input())
S = [int(i) for i in input().split()]

picos = 0

c = 1
while c < N-1:
    if S[c]>S[c-1] and S[c]>S[c+1]:
        picos+=1
        c+=2
    else:
        c+=1

print("S" if picos>1 else "N")