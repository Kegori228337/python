# В первой строке входных данных записаны
# два целых числа n и k (1 ≤ n ≤ 10, 1 ≤ k ≤ 240) — количество задач в соревновании
# и количество минут, за которое Лимак доберётся от дома до места проведения вечеринки.
n = 10
k = 22
# (n, k) = map(int, input().split())
time = 4 * 60 - k
i = 0
print(f'INIT {i}, {time}')
while i < n and time > 5 * i:
	i = i + 1
	time = time - 5 * i
print(f'RESULT {i}')
