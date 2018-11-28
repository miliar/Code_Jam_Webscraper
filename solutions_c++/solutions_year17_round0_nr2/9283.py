#include <bits/stdc++.h>
using namespace std;
int main()
{
	/*
	Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest.
	One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order.
	Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy. 
	She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?
	
	
	Задача B "Обсессивно-компульсивное расстройство"
	Ее игрушки отсортированы от малого к большему, ее карандаши - с короткого к длинному, ее компьютеры - от старого к новому.
	Однажды она практиковалась в подсчете. И заметила, что некоторые целые числа, записанные в системе счисления 10 без ведущих нулей, содержат цифры в неубывающем порядке.
	Например: 8, 123, 555, 224488.
	Назовём эти числа хорошими.
	Она только что закончила считать все положительные числа от 1 до N. Каким было последнее хорошее число, которое она назвала?
	
	132
	2: всё ок
	32: не ок, ближайшее число - 29
	129: всё ок
	Ответ: 129
	
	1000
	0: ок
	00: ок
	000: ок
	1000: не ок, ближайшее число - 999.
	Ответ: 999.
	7
	7: ок
	Ответ: ок
	
	11111111111111 1110
	0: ок
	10: не ок, ответ 09
	109: не ок, ответ 099
	1099: не ок, ответ 0999 
	10999: не ок, ответ 09999
	
	Ну и так далее, пока не дойдём до
	099999999999999999
	
	
	А по какому принципу мы это делаем?
	Занимаем один десяток у соседа слева, заменяем текущий разряд на 9.
	
	Ах да, если я рассматриваю всё справа налево, то сосед слева для "OK" должен быть НЕ БОЛЬШЕ (меньше или равен).
	
	ну-ка, контрпримерчик плиз
	532
	32: превращаем в 29 -> 529
	52: превращаем в 49 -> 499
	
	4301
	1: ок
	01: ок
	30: не ок, превращаем в 29 -> 4291
	91 тоже не ок, превращаем в 4289
	42: не ок, превращаем в 3989, теперь фиксим 989
	9: ок
	89: ок
	98: не ок, превращаем в 899
	89: ок
	итого получаем 3899
	
	
	агааа, нам нужна рекурсия!
	1: ок
	01: ок
	30: не ок, делаем 4291 и верифицируем всё от единицы до двойки.
		1: ок
		91: не ок, делаем 89 и верифицируем последние две цифры.
			9: ок
			89: ок
		28: ок
	к этому моменту у нас число 4289.
	
	42: не ок, делаем 39 и получаем 3989.
		Делаем проверку 989.
		9: ок
		89: ок
		98: не ок, делаем 89.
	Итого получили 3899.
	
	
	Пока что кажется, что можно и без рекурсии.
	Просто сравниваем два числа: текущее и то, что справа. Если всё ок, продолжаем, если нет - меняем местами и фиксим возникшие трудности справа.
	
	1000
	0: ок
	00: ок
	00: ок
	10: не ок, делаем 09 и имеем 900.
	Но: так как старший бит обернулся в ноль, то мы можем смело взять 1 * k - 1 в качестве результата.
	
	111111111111111110
	10: 09, фиксируем ничего
	10: 09, фиксируем 99
	10: 09, фиксируем 999
	
	307:
	07: ок
	30: не ок, делаем 29
		97: не ок, делаем 89
	итого 289
	а это неправильно, на самом деле мы взяли из старшего, так что ответ - <старший> возведенный в свою степень минус один.
	
	*/
	
	short arr[18] = {0};
	int64_t input, copy;
	int64_t result;
	int t;
	cin >> t;
	int length = 0;
	bool bigDecreased, bigTurnedZero;
	int biggestNum;
	for(int j = 1; j <= t; j++)
	{
		length = 0;
		cin >> input;
		//cout << input << endl;
		bigDecreased = false;
		bigTurnedZero = false;
		if(input / 10 == 0)
		{
			cout << "Case #" << j << ": " << input << endl;
			continue;
		}
		copy = input;
		for(int i = 17; copy != 0; i--)
		{
			length++;
			arr[i] = copy % 10;
			copy /= 10;
		}
		for(int i = 1; i < length; i++)
		{
			int index = 17 - i;
			if(arr[index] <= arr[index+1])
			{
				bigDecreased = false;
				continue;		//всё ок
			}
			//делаем соседа справа девяткой, у себя ставим на 1 меньше.
			if(arr[index] == 1)
				bigTurnedZero = true;
			else
				bigTurnedZero = false;
			bigDecreased = true;
			arr[index]--;
			arr[index+1] = 9;
			//и корректируем всё, что справа.
			for(int k = 1; k < i; k++)
			{
				int index2 = 17 - k;
				if(arr[index2] <= arr[index2+1])
					continue;
				arr[index2]--;
				arr[index2+1] = 9;
			}
			result = 0;
			for(int i = 18-length; i < 18; i++)
			{
				result *= 10;
				result += arr[i];
			}
			
		}
		result = 0;
		if(bigDecreased == true)
		{
			if(!bigTurnedZero)
			{
				result = arr[18-length]+1;
				for(int i = 1; i < length; i++)
					result *= 10;
			}
			else
			{
				result = 10;
				for(int i = 1; i < length-1; i++)
					result *= 10;
			}
			result--;
		}
		else
			for(int i = 18-length; i < 18; i++)
			{
				result *= 10;
				result += arr[i];
			}
		cout << "Case #" << j << ": " << result << endl;
	}

	return 0;
}