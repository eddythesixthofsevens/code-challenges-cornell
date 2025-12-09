n = int(input("Enter a number:"))
if n > 24:
    print("Denise slept ", n - 24, " hours.")
elif n < 24:
    print(f"Denise slept {24 - n } hours.")
else:
    print(f"Denise slept 0 hours.")