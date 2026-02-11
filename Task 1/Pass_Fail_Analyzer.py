#list of the student marks
marks = [45, 78, 90, 33, 60]

#initialize counters
pass_count = 0
fail_count = 0

#analyze each students marks
for mark  in marks:
    if mark >= 50:
        pass_count+= 1
    else:
        fail_count+=1


#result
print("Student Result Analysis:")
print("Total Students:",len(marks))
print("Total number of Pass Students:",pass_count)
print("Total Number of Fail Students:",fail_count)

