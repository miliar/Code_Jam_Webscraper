import itertools
import decimal
import math
from codejam import CodeJam

cj = CodeJam(debug=False)

three = decimal.Decimal(3)
five = decimal.Decimal(5).sqrt()
for case in cj.cases:
    n = cj.get_int()
    total = (three + five) ** n
    t = total.to_eng_string()
    entera = t.split('.', 1)[0]
    print entera, t
    cj.write_case(entera[-3:].zfill(3))
