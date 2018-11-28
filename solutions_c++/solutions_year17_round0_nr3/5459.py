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
typedef long double ld;
typedef pair<ld, ld> pld;

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ZERO(x) memset((x), 0, sizeof(x))

const int MAXN = 1050;

int l[MAXN], r[MAXN];
bool used[MAXN];

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
		cin >> n >> k;

		for (int i = 0; i < n + 1; i++)
		{
			used[i] = false;
			l[i] = 0;
			r[i] = 0;
		}

		used[0] = true;
		used[n + 1] = true;
		int lf, rt;
		int x, y;

		for (int z = 0; z < k; z++)
		{
			int cx, cy;
			lf = 0;
			for (int i = 1; i <= n + 1; i++)
				if (used[i])
				{
					rt = i;
					break;
				}

			for (int i = 1; i <= n; i++)
			{
				if (used[i]) // rt == i
				{
					lf = rt;
					for (int j = i + 1; j <= n + 1; j++)
						if (used[j])
						{
							rt = j;
							break;
						}
					continue;
				}

				l[i] = i - lf - 1;
				r[i] = rt - i - 1;
			}

			int maxmin = -1;
			for (int i = 1; i <= n; i++)
			{
				if (used[i])
					continue;
				maxmin = max(maxmin, min(l[i], r[i]));
			}
			int maxmax = -1;
			for (int i = 1; i <= n; i++)
			{
				if (used[i])
					continue;
				if (min(l[i], r[i]) == maxmin)
					maxmax = max(maxmax, max(l[i], r[i]));
			}

			for (int i = 1; i <= n; i++)
			{
				if (used[i])
					continue;
				if (min(l[i], r[i]) == maxmin && max(l[i], r[i]) == maxmax)
				{
					used[i] = true;
					cx = maxmax;
					cy = maxmin;
					break;
				}
			}

			x = cx;
			y = cy;
		}
		cout << "Case #" << t + 1 << ": " << x << " " << y << "\n";
	}

	return 0;
}