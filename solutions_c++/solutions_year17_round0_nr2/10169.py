#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

#define LARGE 1
#define SMALL 0

#define FILE SMALL
#if FILE == SMALL
//#define IN_FILE "A-small-practice.in"
#define IN_FILE "B-small-attempt1.in"
#define OUT_FILE "B-small-attempt1.out"
#define N 1000
#else
//#define IN_FILE "A-large-practice.in"
#define IN_FILE "A-large.in"
#define OUT_FILE "A-large.out"
#define N pow(10, 18)
#endif

unsigned long long solve(unsigned long long num);
unsigned long long find_digits(unsigned long long num);
unsigned long long nthdigit(unsigned long long x, int n);

int main()
{
	unsigned int num_tc, cur_tc;
	unsigned long long number = 0, result = 0;

	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	scanf("%d\n", &num_tc);	//number of test cases

	for (cur_tc = 0; cur_tc < num_tc; cur_tc++)
	{
		printf("Case #%d: ", cur_tc + 1);
		scanf("%lld", &number);
		result = solve(number);
		printf("%lld\n", result);
	}
}


unsigned long long solve(unsigned long long num)
{
	unsigned int i = 0;
	unsigned long long result = 0;
	unsigned int digits = find_digits(num);

	if (num < 10) return num;
	
	for (i = 0; i < digits; i++)
	{
		if (nthdigit(num, digits - i) > nthdigit(num, digits - i - 1))
		{
			return solve(result + (nthdigit(num, digits - i) * pow(10, digits - i)) - 1);
		}
		else
		{
			result += nthdigit(num, digits - i) * pow(10, digits-i) ;
		}
	}
	return num;
}

unsigned long long nthdigit(unsigned long long x, int n)
{
	while (n--) {
		x /= 10;
	}
	return (x % 10);
}

unsigned long long find_digits(unsigned long long num)
{
	unsigned int i = 1;
	while(num >= pow(10, i) )
	{
		i++;
	}
	return i-1;
}
/*
unsigned int flip(unsigned char *in_s, unsigned int start, unsigned int end)
{
unsigned int i = 0;
for (i = start; i <= end; i++)
{
if (in_s[i] == '+')
{
in_s[i] = '-';
}
else if (in_s[i] == '-')
{
in_s[i] = '+';
}
}
}*/
