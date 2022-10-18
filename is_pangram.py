def is_pangram(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    sorted_set = sorted(set(s.lower()))
    i = len(abc)-1
    j = 1
    while i >= 0:
        if abc[i].__eq__(sorted_set[len(sorted_set)-j]):
            counter += 1
        i-=1
        j+=1
    if counter == len(abc):
        return True
    else:
        return False


s = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(s))