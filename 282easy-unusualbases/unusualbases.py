
def unusual_bases(base, num):
    #base = "F" or "T", representing base Fib or base 10
    #num  = the number in that base
    #returns the number in the other base (10 or Fib)
    if base == "T":
        x = convert_to_base_fib(num)
    else: 
        x = convert_to_base_ten(num)
    
    print("%d in base %s is equal to %d in the other base" % (num,base,x))

def convert_to_base_fib(n):
    f = 0
    for x in range(len(fiblist)-1,0,-1):
        if fiblist[x] <= n:
            f += int(str("1"+"0"*x))
            n -= fiblist[x]

    return f
    
def convert_to_base_ten(n):
    t = 0
    s = str(n)
    l = len(s)
    for x in range(l):
        i = int(s[x])
        if i > 0:
            t += fiblist[x]

    return t

def genFibs(maxi):
    for i in range(maxi-1):
        fiblist.append(fiblist[i]+fiblist[i+1])


fiblist = [1,1]

def main():
    genFibs(20) #generates first 100 fibonacci nums
    unusual_bases("T", 16)
    unusual_bases("T", 32)
    unusual_bases("F", 10)
    unusual_bases("F", 111111)

if __name__ == "__main__":
    main()
