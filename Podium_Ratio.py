def big_line():
    print('-=' * 36)

drivers = [
    ('Max Verstappen', 2023, 22, 21),
    ('Michael Schumacher', 2002, 171, 17),
    ('Sebastian Vettel', 2011, 19, 17),
    ('Lewis Hamilton', 2015, 19, 17)
]

big_line()
print('Highest Podium Ratio of Some Formula 1 Drivers - Format Specifiers'.center(72).upper())
big_line()

print(f'| {'NAME':^18} | {'YEAR':^8} | {'STARTS':^8} | {'PODIUMS':^8} | {'PODIUM %':^12}|')

for name, year, starts, podiums in drivers:
    ratio = (podiums / starts) * 100
    print(f'| {name:^18} | {year:^8} | {starts:^8} | {podiums:^8} | {ratio:>10.2f}  |')

big_line()

