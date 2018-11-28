// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <unordered_set>

using namespace std;

template<typename T>
void Print(T obj)
{
	cout << obj;
}

template<typename... T>
void PrintCase(int i, T... Objs)
{
	using expand_type = int[];
	cout << "Case #" << i + 1 << ": ";

	expand_type{ 0, (Print(Objs), 0)... };

	cout << endl;
}

int CountDigits(long long n)
{
	int count = 0;
	do
	{
		count++;
	} while (n = n / 10);
	return count;
}

int GetDigitFromNumber(long long n, int i)
{
	long long factor = std::pow(10, CountDigits(n) - i);
	return (n / factor) % 10;
}

void EvolveNumber(long long & n, int i)
{
	long long factor = std::pow(10, CountDigits(n) - i + 1);
	n = (n / factor) - 1;
	if (n < 0)
		n = factor / 10 - 1;
	else
		n = n*factor + factor - 1;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		long long n;
		cin >> n;

		for (int j = 1; j <= CountDigits(n)-1;)
		{
			if (GetDigitFromNumber(n, j) > GetDigitFromNumber(n, j + 1))
			{
				EvolveNumber(n, j + 1);
				j = 1;
			}
			else
				j++;
		}
		PrintCase(i, n);
	}

	return 0;
}

