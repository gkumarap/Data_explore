string1 = 'reading'
string2 = 'study'

length = len(string1)
print(string1[length - 3:])

length = len(string1)
if length < 3:
    print(string1 + 'has less than or equal to 3 chars, enter more than 3 chars')
else:
    print(string1[length - 3:])
    if string1[length - 3:] == 'ing':
        # newstring = string1.append('ly')
        # print(newstring)
        newstring2 = string1.replace(string1[length - 3:], 'ingly')
        print(newstring2)
