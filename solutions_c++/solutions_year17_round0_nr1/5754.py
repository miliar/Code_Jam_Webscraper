#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
typedef long long int ll;
using namespace std;

char reverse (char c)
{
	if (c == '-') return '+';
	else return '-';
}

int main (void)
{
	int t, k, ssize;
	int result;
	string s;

	cin >> t;
	for (int i=1; i<=t; i++)
	{
		cin >> s;
		cin >> k;
		ssize = s.size();
		result = 0;

		for (int j=0; j<=ssize-k; j++)
		{
			if (s[j] == '-')
			{
				result++;

				for (int num=0; num<k; num++)
				{
					s[j+num] = reverse(s[j+num]);
				}
			}
		}

		for (int j=ssize-k; j<ssize; j++)
		{
			if (s[j] == '-')
			{
				result = -1;
				break;
			}
		}

		printf("Case #%d: ", i);
		if (result == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", result);

	}
}