f = open("que4.txt","r")
d = open("delhi","a")
s = open("shimla","a")
o = open("others","a")
data = f.read()
# print(data)
data_in = data.split("\n")
# print(data_in)
for i in range(0,len(data_in)):
    if "delhi" in data_in[i]:
        d.write(data_in[i])
        d.write("\n")
    elif "shimla" in data_in[i]:
        s.write(data_in[i])
        s.write("\n")
    else:
        o.write(data_in[i])
        o.write("\n")
d.close()
s.close()
o.close()
f.close()

