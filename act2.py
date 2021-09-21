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