import re
import pandas

import matplotlib.pyplot

import emoji

file = open(r'./Data.txt',mode='r',encoding='utf8')

data = file.read()

file.close()


pattern = re.compile('(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)(\s\w+)*(:)')
messengers = re.findall(pattern,data)
print(messengers)


messages = []
couter = 0

for i in messengers:
    if i in messengers:
        messages.append(i)
        ++couter
print(messages)
print(couter)


# count_messages ={}
# for each in messengers:
#     if each in count_messages.keys():
#         count_messages[each]+=1
#     else:
#         count_messages[each]=1
# print(count_messages)



