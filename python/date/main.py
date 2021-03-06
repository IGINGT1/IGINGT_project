import datetime
import sys

if len(sys.argv) > 1:
    now = datetime.datetime.now()
    print(now.strftime(sys.argv[1]))
else:
    print(datetime.datetime.now())



# %a — будний день сокращенно (Пн, Вт,…)
# %A — будний день полностью (Понедельник, Вторник,…)
# %w — будний день, как десятичное число (1, 2, 3,…)
# %d — день месяца в числах (01, 02, 03,…)
# %b — месяцы сокращенно (Янв, Фев,…)
# %B — название месяцев полностью (Январь, Февраль,…)
# %m — месяцы в числах (01, 02, 03,…)
# %y — года без века (19, 20, 21)
# %Y — года с веком (2019, 2020, 2021)
# %H — 24 часа в сутки (с 00 до 23)
# %I — 12 часов в сутки (с 01 до 12)
# %p — AM и PM (00-12 и 12-00)
# %M — минуты (от 00 до 59)
# %S — секунды (от 00 до 59)
# %f — миллисекунды (6 десятичных чисел)

