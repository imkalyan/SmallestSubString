def SmallestSubString (s):
    m = len(set(s))
    n=9999999999
    i=0
    j=0
    while j<=len(s):
        if len(set(s[i:j+1]))==m:
            n=min(j+1-i, n)
            # break
            i+=1
        else:
            j+=1
    return n
    
S = input()
 
output = SmallestSubString(S)
print (output)