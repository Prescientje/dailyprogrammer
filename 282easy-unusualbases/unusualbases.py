
def unusual_bases(base, num):
    #base = "F" or "T", representing base Fib or base 10
    #num  = the number in that base
    #returns the number in the other base (10 or Fib)
    if base == "T":
        x = 4
    else: 
        x = 5
    
    print("%d in base %s is equal to %d in the other base" % (num,base,x))


def genFibs(maxi):
    for i in range(maxi-1):
        fiblist.append(fiblist[i]+fiblist[i+1])



fiblist = [0,1]

def main():
    genFibs(100) #generates first 100 fibonacci nums
    unusual_bases("T", 16)
    unusual_bases("T", 32)
    unusual_bases("F", 10)
    unusual_bases("F", 111111)

if __name__ == "__main__":
    main()
