#1
name = input("Введите своё имя: ")
print("Здравствуй", name, "!", "Как поживаешь?")
h_a_y = input("Как поживаешь?")
print("Настолько", h_a_y, "?", "Хм, ну да ладно.", "А время не подскажешь?")
time = input("Подскажите время собеседнику: ")
print("Ха! Вот и неверно. Время осваивать новую профессию и научиться уже грамотно писать код ")

#2
enter_time = int(input("Введите время в секундах: "))
hours = enter_time // 3600
minutes = enter_time // 60 - hours * 60
seconds = enter_time % 60
convertions_time = (f"{hours:02}:{minutes:02}:{seconds:02}")
print(convertions_time)

#3



