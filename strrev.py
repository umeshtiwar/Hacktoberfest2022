def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "umesh"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
