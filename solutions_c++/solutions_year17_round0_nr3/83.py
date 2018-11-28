#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;
char c[100];

void Solve()
{
	long long n, k;
	cin >> n >> k;
	long long len1 = n, num1 = 1LL, num2 = 0LL;
	while (true)
	{
		if (len1 & 1LL)
		{
			if (k <= num1)
			{
				cout << len1 / 2LL << ' ' << len1 / 2LL << endl;
				return;
			}
			else if (k <= num1 + num2)
			{
				cout << len1 / 2LL << ' ' << len1 / 2LL - 1LL << endl;
				return;
			}
			else
			{
				k = k - num1 - num2;
				len1 = len1 / 2LL;
				num1 = num1 * 2LL + num2;
			}
		}
		else
		{
			if (k <= num1)
			{
				cout << len1 / 2LL << ' ' << len1 / 2LL - 1LL << endl;
				return;
			}
			else if (k <= num1 + num2)
			{
				cout << len1 / 2LL-1LL << ' ' << len1 / 2LL - 1LL << endl;
				return;
			}
			else
			{
				k = k - num1 - num2;
				len1 = len1 / 2LL;
				num2 = num2 * 2LL + num1;
			}
		}
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}