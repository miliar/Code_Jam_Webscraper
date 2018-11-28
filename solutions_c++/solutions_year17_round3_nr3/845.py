#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef pair <int, int> ii;
typedef double ld;
typedef pair<ld, ld> pld;

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ZERO(x) memset((x), 0, sizeof(x))

const int MAXN = 1050;
const ld PI = 3.14159265358979323846;

ll dp[MAXN][MAXN];
const long double EPS = 1e-7;

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n, k;
		ld ans;
		cin >> n >> k;
		ld u;
		cin >> u;

		vector <ld> p(n);
		for (int i = 0; i < n; i++)
		{
			cin >> p[i];
		}

		while (u > EPS)
		{
			sort(p.begin(), p.end());
			ld min1 = p[0];
			int i = 0;
			while (i < n)
			{
				if (p[i] - min1 > EPS)
				{
					break;
				}
				i++;
			}

			if (i == n)
			{
				ld ost = u / n;
				for (int j = 0; j < n; j++)
				{
					p[j] += ost;
				}
				break;
			}
			else
			{
				ld delta = p[i] - min1;
				if (u >= (delta) * i)
				{
					u -= (delta) * i;
					for (int j = 0; j < i; j++)
						p[j] = p[i];
				}
				else
				{
					ld ost = u / i;
					for (int j = 0; j < i; j++)
						p[j] += ost;
					u = 0.0;
				}
			}
		}

		ans = p[0];
		for (int i = 1; i < n; i++)
		{
			ans *= p[i];
		}

		printf("Case #%d: %.10lf\n", t + 1, ans);
	}

	return 0;
}