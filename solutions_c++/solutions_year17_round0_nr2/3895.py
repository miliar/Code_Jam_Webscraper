#include <iostream>
#include <cstdlib>
#include <cmath>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <random>

using namespace std;

bool isTidy(long long n)
{
	int prev = 10;
	while (n)
	{
		int c = n % 10;
		if (c > prev)
			return false;
		prev = c;
		n /= 10;
	}
	return true;
}
long long brute(long long n)
{
	while (n)
	{
		if (isTidy(n))
		{
			return n;
			break;
		}
		n--;
	}
	return n;
}
long long solve(long long n)
{
	while (n)
	{
		if (isTidy(n))
		{
			return n;
			break;
		}
		long long decr = 1;
		long long t = n;
		while (t % 10 == 9) {
			decr *= 10;
			t /= 10;
		}
		n -= decr;
	}
	return n;
}
void test()
{
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<long long> dis(1, 10000);

	for (int i = 0; i < 1000; i++)
	{
		long long n = dis(gen);
		long long b = brute(n);
		long long s = solve(n);
		cout << b << " " << s << (b==s?" PASS":" FAIL") << "\n";
	}
}
int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		cout << "Case #" << c << ": ";

		long long int n;
		cin >> n;
		
		cout << solve(n);

		cout << "\n";
	}
	return 0;
}