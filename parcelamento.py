v=int(input())
p=int(input())

if(v%p == 0):
    for x in range(p):
        print(int(v/p))
else:
    s=(v%p)
    for y in range(s):
        print(int((v-s)/p)+1)
    for k in range((p-s)):
        print(int((v-s)/p))