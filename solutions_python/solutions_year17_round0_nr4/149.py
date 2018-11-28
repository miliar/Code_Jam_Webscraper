#!/bin/bash

rm -f dd[0-9]
echo started
./d.py  1 10  < d.in > d0.out && touch dd0 &
./d.py 11 20  < d.in > d1.out && touch dd1 &
./d.py 21 30  < d.in > d2.out && touch dd2 &
./d.py 31 40  < d.in > d3.out && touch dd3 &
./d.py 41 50  < d.in > d4.out && touch dd4 &
./d.py 51 60  < d.in > d5.out && touch dd5 &
./d.py 61 70  < d.in > d6.out && touch dd6 &
./d.py 71 80  < d.in > d7.out && touch dd7 &
./d.py 81 90  < d.in > d8.out && touch dd8 &
./d.py 91 100 < d.in > d9.out && touch dd9 &


while [ `ls dd[0-9] 2>/dev/null | wc -w` -lt 10 ]
do
    echo `grep "Case" d[0-9].out | wc -l` `ls dd[0-9] 2>/dev/null`
    sleep 3 
done

cat d[0-9].out > d.out

rm -f dd[0-9]

echo ok
