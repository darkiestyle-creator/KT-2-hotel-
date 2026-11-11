money = int(input("Сколько у нас денег на месяц: "))
while money <= 0:
      print("Ты бедный. Приходи, когда заработаешь")
      money = int(input("Сколько у нас денег на месяц: "))
count = 0

while True:
    answer = input("Введи расход или слово стоп: ")

    if answer == "стоп":
        break

    if answer == "":
        print("Ты ничего не ввел")
    else:
        rashod = int(answer)

        if rashod <= 0:
            print("Расход должен быть больше нуля")
        elif rashod > money:
            print("Денег нет!")
        else:
            money = money - rashod
            count = count + 1
            print("Записал! Осталось:", money)
print("Успешных трат:", count)
print("Осталось денег:", money)