import sys
def create_prefix_array(pattern):
    i = 0
    j = 1
    prefix_array = [0]
    while i < len(pattern) and j < len(pattern):
        if pattern[i] == pattern[j]:
            prefix_array.append(i + 1)
            i += 1
            j += 1
        else:
            while i > 0 and pattern[i] != pattern[j]:
                i = prefix_array[i - 1]
            if pattern[i] != pattern[j]:
                prefix_array.append(i)
            else:
                prefix_array.append(i + 1)
            j += 1
    return prefix_array:q
def kmp(pattern, text):
    prefix_array = create_prefix_array(pattern)

    j = 0
    for i, char in enumerate(text):
        if char == pattern[j]:
            j += 1
        else:
            if j > 0:
                j = prefix_array[j - 1]
            if char == pattern[j]:
                j += 1
        if j == len(prefix_array):
            return i - (j - 1)
        print("j", j)
    return -1

pattern = "bcgl"
print("prefix array", create_prefix_array(pattern))
text = "abcbcglx"
print("match between", pattern, text, ":", kmp(pattern, text)) 
def main():
    pattern = sys.argv[1] 
    text = sys.argv[2]
    print(kmp(pattern, text))

main()
