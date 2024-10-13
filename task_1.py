def total_salary(path):
    try:
        total=0
        count=0
        
        with open( path,"r",encoding="utf-8") as file:
            for line in file:
                _, salary = line.strip().r.split(",", 1)
                total += int(salary)
                count +=1
                
        average = total / count if count > 0 else 0
        
    except FileNotFoundError:
        print (f"Помилка: файл {path} не знайдено.")
        return None, None
    except IOError:
        print (f"Помилка: не вдалося прочитати файл {path}.")
        return None, None
    
        return total, average







