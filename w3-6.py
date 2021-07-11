'''Write a Python program to read a file line by line store it into a variable.'''

# my_file=open("w3-6.txt","r")
# a=my_file.read()
# print(a)


# def file_read(fname):
#     with open (fname, "r") as myfile:
#         data=myfile.readlines()
#         print(data)
# file_read('test.txt')

with open("w3-6.txt","r")as my_file:
    a=my_file.read()
    print(a,end="")
my_file.close()
