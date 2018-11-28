#include <iostream>
using namespace std;

long long maximize(int len);
long long dfy(int len);
long long tidy(long long n);

void main()
{
	int t;
	long long n;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n;
		cout << "Case #" << i << ": " << tidy(n) << endl;

	}
}

long long maximize(int len)
{
	long long res = 9;

	for (int i = 1; i < len; i++)
	{
		res = res * 10 + 9;
	}

	return res;
}

long long dfy(int len)
{
	long long res = 10;

	for (int i = 1; i < len; i++)
	{
		res *= 10;
	}

	return res;
}

long long tidy(long long n)
{
	if (n == 0) return 0;

	int r1, r2, count;
	long long res;

	res = r2 = n % 10;
	n /= 10;
	count = 1;

	while (n != 0)
	{
		r1 = n % 10;

		if (r1 > r2)
		{
			r1--;
			res = r1 * dfy(count) + maximize(count);
		}
		else
		{
			res = r1 * dfy(count) + res;
		}

		r2 = r1;
		n /= 10;
		count++;
	}


	return res;
}