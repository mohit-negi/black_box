def duval(n, s):
    '''
    params:
     'n' - length of the string 
     's' - string itself
     returns the 0-indexed position of the lexicographically smallest cyclic shift of the string.
    '''
    assert n >= 1
    i = 0
    ans = 0
    while i < n:
        ans = i
        j = i + 1
        k = i
        while j < n + n and not s[j % n] < s[k % n]:
            if s[k % n] < s[j % n]:
                k = i
            else:
                k += 1
            j += 1
        while i <= k:
            i += j - k
    return ans

def duval(s):
    return duval(len(s), s)

# Example usage:
s = "abracadabra"
print(duval(s))  # Output will be the 0-indexed position of the least cyclic shift
