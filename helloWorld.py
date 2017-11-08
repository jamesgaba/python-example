
def prime_finder(start=9000, end=10000):
    # prime finder...
    for n in range(start, end):
        for x in range(2, n):
            if n % x == 0:
                # print(n, 'can be factored as', x, 'x', n//x)
                break
        else:
            print(n, 'is a prime number')


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

for i in range(len(list)):
    print(bin(i),list[i])

for w in list[:]:
    if len(w) > 3:
        list = [w] + list
print(list)


s = 'hahahahbahahah'
for c in s:
    print(c)

for x in range(33,55):
    print(x)

#age=int(input("please enter your age: "))
age=0

if age < 20:
    print("man you're young!")
elif age > 40:
    print("man you're old!!")
else:
    print("you're in between!")

prime_finder(800, 900)
