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
const ld PI = 3.14159265358979323846;

ll dp[MAXN][MAXN];

bool cmp(const pair<ll, ll>& a, const pair<ll, ll>& b)
{
	if (a.first == b.first)
		return a.second > b.second;
	return a.first > b.first;
}

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
		vector < pair<ll, ll> > pnk;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
		{
			ll r, h;
			cin >> r >> h;
			pnk.push_back(mp(r, h));
		}
		sort(pnk.begin(), pnk.end(), &cmp);

		vector <pair <ll, ll>> w;
		for (int i = 0; i < n; i++)
		{
			w.push_back(mp(2*pnk[i].first * pnk[i].second, i));
		}
		sort(w.begin(), w.end(), &cmp);

		ll ans = 0;
		for (int i = 0; i < n - k + 1; i++)
		{
			ll cur_ans = pnk[i].first * pnk[i].first + 2*pnk[i].first * pnk[i].second;
			int pas = 0;
			for (int j = 0; j < n; j++)
			{
				if (pas == k - 1)
					break;

				if (w[j].second > i)
				{
					pas++;
					cur_ans += w[j].first;
				}
			}
			ans = max(ans, cur_ans);
		}
		printf("Case #%d: %.10lf\n", t + 1, PI*ans);
	}

	return 0;
}