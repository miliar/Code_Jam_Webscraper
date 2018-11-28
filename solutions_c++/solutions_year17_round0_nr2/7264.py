#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <stdlib.h>
using namespace std;

bool chk(long long num)
{
	string st=to_string(num);
	for (int i = 1; i < st.length(); i++)
	{
		if (st[i-1] > st[i]) return true;
		if (st[i] == '0') return true;
	}
	return false;
}

int main()
{
#ifdef SMALL
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int T, t;
	for (scanf("%d", &T), t = 0; t < T; t++)
	{
		long long number;
		scanf("%lld", &number);
		while (chk(number))
		{
			number--;
		}
		printf("Case #%d: %lld\n", t + 1, number);

	}
#else
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, t;
	for (scanf("%d", &T), t = 0; t < T; t++)
	{
		long long number;
		scanf("%lld", &number);
		string st = to_string(number);
		while (1)
		{
			bool chk = true;
			for (int i = 1; i < st.length(); i++)
			{
				if (st[i - 1] > st[i] || st[i]=='0')
				{
					if (chk)
					{
						st[i] = '9';
						st[i - 1]--;
						chk = false;
					}
					else
					{
						st[i] = '9';
					}
				}

			}
			if (chk) break;
		}
		number = atoll(st.c_str());
		printf("Case #%d: %lld\n", t + 1, number);

	}
#endif
}