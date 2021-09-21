print("Student Average Calculator")
print("")
print("PRELIM GRADE: ")
prel = int(input())
print("MIDTERM GRADE: ")
midt = int(input())
print("SEMIFINAL GRADE: ")
semi = int(input())
print("FINAL GRADE: ")
final = int(input())


sum = prel + midt + semi + final
avg = sum/4

print("Your average is {}. Well done!".format(avg))

if avg >= 75:
    print("You passed!")
else:
    print("You Failed!")


    if avg>=99 and avg<=100:
    print("The equivalent of your average {} is A. Congrats!".format(avg))
elif avg>=90 and avg<99:
    print("The equivalent of your average {} is B. Congrats!".format(avg))
elif avg>=80 and avg<90:
    print("The equivalent of your average {} is C. Congrats!".format(avg))
elif avg>=71 and avg<80:
    print("The equivalent of your average {} is D.".format(avg))
elif avg>=61 and avg<71:
    print("The equivalent of your average {} is E.".format(avg))
elif avg>=60:
    print("The equivalent of your average {} is F.".format(avg))
else:
    print("Invalid Input!")