#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<vector>
#include<cstdio>
#include<iomanip>

using namespace std;

int n;
int red, yellow, blue, violet, green, orange;
//N, R, O, Y, G, B, and V
int main()
{
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("B-small-attempt3.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n >> red >> orange >> yellow >> green >> blue >> violet;
		cout << "Case #" << i << ": ";
		if (red > n / 2 || yellow > n / 2 || blue > n / 2)
			cout << "IMPOSSIBLE" << endl;
		else
		{
			
			string res;
			res.resize(n);
			for (int j = 0; j < n; j++)
			{
				if (red && red >= yellow && red >= blue && (!j || res[j - 1] != 'R'))
					res[j] = 'R', red--;
				else if (yellow && yellow >= blue && (!j || res[j - 1] != 'Y'))
					res[j] = 'Y', yellow--;
				else if (blue && (!j || res[j - 1] != 'B'))
					res[j] = 'B', blue--;
				else if (red && (!j || res[j - 1] != 'R'))
					res[j] = 'R', red--;
				else if (yellow && (!j || res[j - 1] != 'Y'))
					res[j] = 'Y', yellow--;
				else
					res[j] = 'B', blue--;
			}

			if (res.back() == res[0])
			{
				swap(res[res.size() - 1], res[res.size() - 2]);
				int x = res.size() - 2;
				while (res[x] == res[x + 1] || res[x] == res[x - 1])
					swap(res[x], res[x - 1]), x--;
			
			}
			
			cout << res << endl;
		}
	}
	return 0;
}
