import re
html='fdsfsdf4568dfsdf'
result=re.search('sd.*?(\d+)',html)
print(result.group(1))