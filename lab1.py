from datetime import datetime, time
file_path = "D:\\lab\\IP.txt"# Путь к файлу
application_name = "Skype"
def print_protocol_by_application(file_path, application_name):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip("()\n").split(", ")
                if len(data) >= 6 and data[5].strip() == application_name:  # Убираем лишние пробелы вокруг названия программы
                    print(line.strip())
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

def read_data_from_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                start_time, end_time, _, _, _, program_name = line.strip().split(", ")
                data.append((start_time, end_time, program_name))
            except ValueError:
                print(f"Ошибка при обработке строки: {line}")
    return data

def print_protocol_after_time(file_path, target_time_str):
    try:
        target_time = datetime.strptime(target_time_str, "%H:%M:%S").time()

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip("()\n").split(", ")
                if len(data) >= 6:
                    current_time = datetime.strptime(data[0], "%H:%M:%S").time()
                    if current_time > target_time:
                        
                        print(line.strip())

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

file_path = "D:\\lab\\IP.txt"
target_time_str = "08:00:00"







from datetime import datetime
# Метод сортировки по убыванию времени использования сети Интернет
def insertion_sort_by_time_desc(file_path):
    try:
        # Reading data from the file
        with open(file_path, "r", encoding="utf-8") as file:
            data = [line.strip("()\n").split(", ") for line in file]

        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and (datetime.strptime(data[j][1], "%H:%M:%S") - datetime.strptime(data[j][0], "%H:%M:%S")) < (datetime.strptime(key[1], "%H:%M:%S") - datetime.strptime(key[0], "%H:%M:%S")):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

        print("Отсортированные данные по времени (по убываниюри):")
        for item in data:
            print(item)
    except Exception as e:
        print(f"Произошла ошибка при сортировке по времени: {e}")

# Метод сортировки по возрастанию названия программы и убыванию суммарного количества байт
def insertion_sort_by_name_and_bytes(file_path):
    try:
        # Reading data from the file
        with open(file_path, "r", encoding="utf-8") as file:
            data = [line.strip("()\n").split(", ") for line in file]

        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and len(data[j]) >= 6 and len(key) >= 6 and (data[j][5], -int(data[j][3]) - int(data[j][4])) > (key[5], -int(key[3]) - int(key[4])):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

        print("Отсортированные данные по программам и байтам:")
        for item in data:
            print(item)
    except Exception as e:
        print(f"Произошла ошибка при сортировке по программам и байтам: {e}")


data = [
    ("08:00:00", "08:15:23", "00:15:23", 10240, 20480, "Facebook Messenger"),
    ("10:30:10", "10:45:55", "00:15:45", 14336, 30720, "Telegram"),
    ("12:20:05", "12:35:40", "00:15:35", 8192, 16384, "Skype"),
    ("14:55:12", "15:10:28", "00:15:16", 12288, 24576, "TikTok"),
    ("16:40:30", "16:55:45", "00:15:15", 9216, 18432, "WhatsApp"),
    ("18:25:40", "18:40:55", "00:15:15", 11264, 22528, "Skype"),
    ("20:15:20", "20:30:35", "00:15:15", 13312, 26624, "Telegram"),
    ("22:00:15", "22:15:30", "00:15:15", 10240, 20480, "Vkontakte"),
    ("23:45:00", "00:00:15", "00:15:15", 8192, 16384, "TikTok"),
    ("01:30:50", "01:45:05", "00:15:15", 14336, 28672, "WhatsApp")
]

def get_time_diff(record):
    start_time = record[0]
    end_time = record[1]
    diff = (int(end_time.split(":")[0]) * 3600 + int(end_time.split(":")[1]) * 60 + int(end_time.split(":")[2])) - \
           (int(start_time.split(":")[0]) * 3600 + int(start_time.split(":")[1]) * 60 + int(start_time.split(":")[2]))
    return diff

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = get_time_diff(arr[len(arr) // 2])
    left = [x for x in arr if get_time_diff(x) < pivot]
    middle = [x for x in arr if get_time_diff(x) == pivot]
    right = [x for x in arr if get_time_diff(x) > pivot]
    return quick_sort(right) + middle + quick_sort(left)










def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    less = [x for x in data if compare(x, pivot) < 0]
    equal = [x for x in data if compare(x, pivot) == 0]
    greater = [x for x in data if compare(x, pivot) > 0]
    return quicksort(less) + equal + quicksort(greater)

def compare(entry1, entry2):
    # Сравниваем записи по названию программы, а внутри одной программы
    # по убыванию суммарного количества переданных и полученных байт
    program1, program2 = entry1[5], entry2[5]
    if program1 < program2:
        return -1
    elif program1 > program2:
        return 1
    else:
        total1 = entry1[3] + entry1[4]
        total2 = entry2[3] + entry2[4]
        return total2 - total1







while True:
    try:    
        choice = input("Выберите опцию:\n1. Вывести протокол использования сети Интернет программой Skype.\n2. Вывести протокол использования сети Интернет после 8:00:00.\n3. Сортировка вставками, сортировка данных по времени.\n4. Сортировка вставками, сортировка данных по программам и байтам. \n5. Быстрая сортировка, по убыванию времени использования сети Интернет \n6. Быстрая сортировка, по возрастанию названия программы, а в рамках одной программы по убыванию суммарного количества переданных и полученных байт\nq. Выйти\n")
        if choice.lower() == "q":
            break

        if choice == "1":
            print_protocol_by_application(file_path, application_name)
        elif choice == "2":
            print_protocol_after_time(file_path, target_time_str)
        elif choice == "3":
            sorted_data = insertion_sort_by_time_desc(file_path)
        elif choice == "4":
            sorted_data = insertion_sort_by_name_and_bytes(file_path)
        elif choice == "5":
            data_sorted = quick_sort(data)

            for record in data_sorted:
                print(record)
           
        elif choice == "6":
            sorted_data = quicksort(data)

            for entry in sorted_data:
                print(entry)
        else:
            print("Некорректный выбор. Выберите 1, 2, 3, 4 или q.")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")