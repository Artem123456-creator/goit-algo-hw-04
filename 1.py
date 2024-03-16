def total_salary(path):
    total_salary_developers = 0
    developers_count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_salary_developers += int(salary)
                developers_count += 1
    except FileNotFoundError:
        print("Oops... Your file not found")

    if developers_count > 0:
        average = total_salary_developers / developers_count
    else:
        average = 0 

    return total_salary_developers, average

total_salary_developers, average = total_salary("Шлях до файлу")
print(f"Загальна сума заробітної плати: {total_salary_developers}, Середня заробітна плата: {average}")
