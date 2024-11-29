def total_salary(path):
    try:
        with open(path,'r', encoding='UTF-8')  as fh:
            sum = 0 
            workers= 0
            for el in fh.readlines():
                salary = el.split(',')[1]
                sum += int(salary)
                workers+=1
            return tuple({ sum, sum // workers })
    except FileNotFoundError:
            print("File does not exist.")
    

try:
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except TypeError:
    print("Enter the correct file path.")