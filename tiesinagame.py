players = int(input("Enter player number (between 1 and 10): "))
games = int(input("Enter amount of matches played: "))
point_list = []
x = 1
print()
while x <= players:
    point_list.append(int(input("Enter point amount: ")))
    x +=1
print()
for i in point_list:
    if (i % 42) = 