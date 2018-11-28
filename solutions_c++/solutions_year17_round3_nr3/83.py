#include <iostream>
#include <algorithm>

using namespace std;

long double p[100];

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		int n, k;
		cin >> n >> k;
		long double u;
		cin >> u;
		for (int i = 0; i < n; i++)
			cin >> p[i];
		sort(p, p + n);
		for (int i = 1; i < n; i++)
		{
			if (u >= (p[i] - p[i - 1]) * i)
			{
				for (int j = 0; j < i; j++)
				{
					u -= p[i] - p[j];
					p[j] = p[i];
				}
			}
			else
			{
				for (int j = 0; j < i; j++)
					p[j] += u / i;
				u = 0;
				break;
			}
		}
		for (int j = 0; j < n; j++)
			p[j] += u / n;
		long double res = 1;
		for (int j = 0; j < n; j++)
			res *= p[j];
		cout.precision(10);
		cout << "Case #" << tc << ": " << fixed << res << endl;
	}
}
