x = "Amit_ml@gmail.edu"

if '@' and '.' in x:
    print(True)
else:
    print("Invalid email") 
if True:
    y = x.split('@') 
    z = x.split('.')
    print("Extract Username:" , y[0])
    print("Extract Domain:" ,z[1])
    
if z[1] == "edu":
    print("Educational Domain")
elif z[1] == "com":
    print("Commercial Domain")
else:
    print("Other Domain")
     

