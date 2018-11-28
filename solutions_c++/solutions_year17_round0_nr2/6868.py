#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS

int T;
long long int N;

vector<int> digits;

void subtract_one(int digitNo)
{
	int selected_digit = digitNo;
	while (digits[selected_digit] == 0)
	{
		selected_digit++;
	}
	digits[selected_digit]--;
	for (int i = 0; i < selected_digit; i++)
	{
		digits[i] = 9;
	}
}

int main()
{
	FILE* file;
	freopen_s(&file, "input.txt", "r", stdin);
	FILE* file_2;
	freopen_s(&file_2, "output.txt", "w", stdout);
	scanf_s("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf_s("%lld", &N);
		digits.clear();
		while (N > 0)
		{
			digits.push_back(N % 10);
			N = N / 10;
		}

		for (int i = 0; i < digits.size() - 1; i++)
		{
			if (digits[i] < digits[i + 1])
			{
				subtract_one(i + 1);
			}
		}

		long long int result = 0;

		for (int i = digits.size() - 1; i >= 0; i--)
		{
			result = result * 10;
			result = result + digits[i];
		}

		printf_s("Case #%d: %lld\n", i + 1, result);
	}
	return 0;
}