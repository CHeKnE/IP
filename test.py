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



sorted_data = quicksort(data)

for entry in sorted_data:
    print(entry)
