english = 7
math = 6
programming = 8

average = (english + math + programming) / 3

if english < 4 or math < 4 or programming < 4:
    print("Failed!")
elif average >= 5.5:
    print("Passed!")
else:
    print("Failed!")

print("Average:", average)
