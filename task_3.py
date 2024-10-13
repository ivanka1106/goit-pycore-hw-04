# pip freeze > requirements.txt
# pip install -r requirements.txt

import sys
from colorama import Fore, Style, init
from pathlib import Path

init(autoreset=True)

def visualize_directory_structure(path) :
    try:
        dir_path = Path(path)
        
        if not dir_path.exists():
            print(f"{Fore.RED}Помилка: Шлях {path} не існує")
            return
        if not dir_path.is_dir():
            print(f"{Fore.RED}Помилка: {path} не є директорією")
            return
        
        for item in dir_path.glob('**/*') :
            relative_path = item.relative_to(dir_path)
            level = len(relative_path.parts) - 1
            indent = ' ' * 4 * level
            
            if "__pycache__" in item.parts or item.suffix == '.pyc':
                continue
                        
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
            
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
            
                
    except Exception as e:
        print (f"{Fore.RED}Невідома помилка: {e}")
        
if __name__== "__main__":
    if len(sys.argv) != 2:
        print (f"{Fore.YELLOW}Використання: python script.py <шлях до директорії>")
    else:
        directory_path = sys.argv [1]
        visualize_directory_structure(directory_path)




