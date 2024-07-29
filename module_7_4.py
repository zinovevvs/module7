score_1 = 40
score_2 = 39
tasks_total = 82
time_avg = 350.4
team2_time = 2153.31451
team1_num = 5
tea2_num = 6
team1_time = 18015.2
print('В команде %s участников: %s' % ('Мастера кода', 5))
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s' % {'team1_num': '5', 'team2_num': 6}, "!")
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f"Результат битвы: {result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")


