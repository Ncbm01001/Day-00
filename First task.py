# Задание №1
# Требуется определить количество рабочих часов четырех сотрудников работающих по графику 2 через 2 по 12 часов.
# Первый работник приступает к работе первого числа, второй - второго, третий - третьего, а четвертый - четвертого.
# Рассматриваемый период - февраль. Праздники отсутствуют.
#
# Результатом выполнения кода должна быть информация о том,
# сколько часов каждый из сотрудников отработал за месяц, а также общее количество отработанных часов.

# Важный дисклеймер. Прочитав задание я решил, что условные четыре человека работают по очереди  друг за другом.
# Так же я решил добавить остальные месяцы, ибо мне писать это все понравилось)
# Позже, погда все это написал, посмотрел твое решение и оказалось, что я усложнил себе задачу.

print("1 — январь, 2 — февраль, 3 — март,\n"
      "4 — апрель, 5 — май, 6 — июнь,\n"
      "7 — июль, 8 — август, 9 — сентябрь,\n"
      "10 — октябрь, 11 — ноябрь, 12 — декабрь\n"
      "Введите порядковый номер месяца:")

day_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_numder_function = input()

while not months_numder_function.isnumeric() or not (1 <= int(months_numder_function) <= 12):
    print("Некорректный ввод. Воспользуйтесь справкой выше и попробуйте еще раз.")
    months_numder_function = input()

months_numder_function = int(months_numder_function)
days = day_in_months[months_numder_function - 1]

while True:
    print("Интересующий вас год высокосный? Ответьте, пожалуйста, словами <Да> или <Нет>.")
    leap_year = input()
    if leap_year.lower() == 'да':
        days = 29
        break
    elif leap_year.lower() == 'нет':
        days = 28
        break

    print("Некорректный ввод. Попробуйте, пожалуйста, еще раз.")

total_working_time = days * 12
print("Общее рабочее время этом месяце составляет", total_working_time, "ч.")

workers = [0, 0, 0, 0]

while total_working_time > 0:
    for worker_index in range(len(workers)):
        total_working_time = total_working_time - 12
        workers[worker_index] += 12
        if total_working_time < 1:
            break

print("Первый рабочий отработал в этом месяце", workers[0], "ч.")
print("Второй рабочий отработал в этом месяце", workers[1], "ч.")
print("Третий рабочий отработал в этом месяце", workers[2], "ч.")
print("Четвертый рабочий отработал в этом месяце", workers[3], "ч.")
