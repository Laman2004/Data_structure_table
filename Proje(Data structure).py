# for lists
list_methods=[]
for method in dir(list):
    if method.startswith("__"):     # python-un xususi funksiyalarini elave etmesin
        continue
    list_methods.append(method)

# for set
set_methods=[]
for method in dir(set):
    if method.startswith("__"):     # python-un xususi funksiyalarini elave etmesin
        continue
    set_methods.append(method)

# for tuple
tuple_methods=[]
for method in dir(tuple):
    if method.startswith("__"):     # python-un xususi funksiyalarini elave etmesin
        continue
    tuple_methods.append(method)

# for string
string_methods=[]
for method in dir(str):
    if method.startswith("__"):     # python-un xususi funksiyalarini elave etmesin
        continue
    string_methods.append(method)

# for dictionary
dict_methods=[]
for method in dir(dict):
    if method.startswith("__"):     # python-un xususi funksiyalarini elave etmesin
        continue
    dict_methods.append(method)

adlar=["List Methods","Set Methods","Tuple Methods","String Methods","Dict Methods"]
classes=[list_methods,set_methods,tuple_methods,string_methods,dict_methods]

max_len=0
for class1 in classes:
    if len(class1)>=max_len:               # en cox funksiyali methoda esasen cap etmek
        max_len=len(class1)

with open("data.txt","w") as data:
    for ad in adlar:
        print(ad,end="")                     # title-lari cap etmek
        print(" "*(30-len(ad)),end="")
        data.write(ad)
        data.write(" "*(30-len(ad)))

    for i in range(max_len):
        print()
        data.write("\n")
        for class1 in classes:
            if i>=len(class1):
                print("-------",end="")
                print(" "*23,end="")
                data.write("-------")
                data.write(" "*23)
            else:
                print(class1[i],end="")
                print(" "*(30-len(class1[i])),end="")          # seliqeli gorunus ucun
                data.write(class1[i])
                data.write(" "*(30-len(class1[i])))

