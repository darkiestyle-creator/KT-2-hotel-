money = input("Сколько у нас денег на месяц: ")

is_valid = True
for i in money:
  if not (
      i == "0"
      or i == "1"
      or i == "2"
      or i == "3"
      or i == "4"
      or i == "5"
      or i == "6"
      or i == "7"
      or i == "8"
      or i == "9"
  ):
    is_valid = False

while not is_valid or int(money) <= 0:
  print("Ты бедный. Приходи, когда заработаешь или введи нормально")
  money = input("Сколько у нас денег на месяц: ")
  is_valid = True
  for i in money:
    if not (
        i == "0"
        or i == "1"
        or i == "2"
        or i == "3"
        or i == "4"
        or i == "5"
        or i == "6"
        or i == "7"
        or i == "8"
        or i == "9"
    ):
      is_valid = False

money = int(money)
count = 0

while True:
  answer = input("Введи расход или слово стоп: ")

  if answer == "стоп":
    break

  if answer == "":
    print("Ты ничего не ввел")
    continue

  is_valid = True
  for i in answer:
    if not (
        i == "0"
        or i == "1"
        or i == "2"
        or i == "3"
        or i == "4"
        or i == "5"
        or i == "6"
        or i == "7"
        or i == "8"
        or i == "9"
    ):
      is_valid = False

  if is_valid:
    rashod = int(answer)

    if rashod <= 0:
      print("Расход должен быть больше нуля")
    elif rashod > money:
      print("Денег нет!")
    else:
      money = money - rashod
      count = count + 1
      print("Записал! Осталось:", money)
  else:
    print("сам пошел нахуй")

print("Успешных трат:", count)
print("Осталось денег:", money)