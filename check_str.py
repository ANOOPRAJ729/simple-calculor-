str="anpp00A234432BA"
my_dict={}

for char in str:
    if char in my_dict:
        my_dict[char]+=1
    else:
        my_dict[char]=1
for item in my_dict:
    if my_dict[item]==2:
        print(item)