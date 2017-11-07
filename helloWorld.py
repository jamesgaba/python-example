


print("Hello world!\n")
print("Additional test line\n")
print("Adding 3rd line...\n")

i=0
while i<10:
    print(i)
    i=i+1

while i<20:
    print(i,end=' ')
    i=i+1

print()

list = ['cat', 'dog', 'goat']
for w in list:
    print(w, len(w))

for w in list[:]:
    if len(w) > 3:
        list = [w] + list
print(list)


s = 'hahahahbahahah'
for c in s:
    print(c)

age=int(input("please enter your age: "))

if age < 20:
    print("man you're young!")
elif age > 40:
    print("man you're old!!")
else:
    print("you're in between!")

