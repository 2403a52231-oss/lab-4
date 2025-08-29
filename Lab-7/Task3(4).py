f = open("numbers.txt","r")
nums = f.readlines()
squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n)*int(n))
f2 = open("squares.txt","w")
for sq in squares:
    f2.write(str(sq)+"\n")
print("squares written")    
# You can create a text file in Python using the open() function with "w" (write) mode.
# For example, to create "numbers.txt" and write some numbers to it:

with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n4\n5\n")

print("numbers.txt created with sample numbers.")

# Now you can run the rest of your code to read and process this file.


         