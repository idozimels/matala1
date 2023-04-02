##1.
def my_func(x1, x2, x3):
    if not all(isinstance(i, float) for i in [x1, x2, x3]):
        print("Error: parameters should be float")
        return None

    if x1 + x2 + x3 == 0:
        print("Not a number – denominator equals zero")
        return None

    result = ((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3)
    return float(result)
# print(my_func(1.0, 5.0, 'n'))
# print(my_func(1.0, 5.0, True))
# print(my_func(1.0, 5.0, 4))
# print(my_func(1.0, 5.0, 4.0))


##2a.
def revword(word: str) -> str:
    return word[::-1].lower()

#print(revword('odi'))

##2b.
def countword() -> int:
    # Opening the file and reading the contents
    with open("C:/Users/idozi/.spyder-py3/anat/text.txt", 'r') as file:
        content = file.readlines()
    word = content[0].strip()
    count = 1
    for sentence in content[1:]:
        words = sentence.strip().split()
        for i in words:
            i = revword(i)
            if i == word:
                count += 1
    return count

#print(countword())