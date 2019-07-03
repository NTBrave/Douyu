import re
s = '""<script>window.$DATA = {"tabTagPath":"/gapi/rkc/directory/c_tag/2_1/list","pageCount":21,"gameSet":{},"cateInfo":{"cat"'
p = re.compile(r'(?:pageCount":)\d*')
sss = re.findall(r'\d+', "  ".join(re.findall(p, s)))
print(sss[0])

p1= re.compile(r'(?:tabTagPath":)\D*')
sss1 = re.findall(p1, s)
print(sss1)