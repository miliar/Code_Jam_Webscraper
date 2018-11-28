#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <functional>
#include <list>
#include <cmath>
#include <string>
#include <cstring>
#include <set>
#include <map>
#define PI 3.14159265359
typedef long long ll;
using namespace std;

inline ll up(ll R) {
	return R*R;
}

inline ll side(ll R, ll H) {
	return 2 * R*H;
}
int main() {
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("R1C_A_large.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		int N, K;
		ll r, h;
		scanf("%d %d", &N, &K);
		vector<pair<ll, ll > > p;
		for (int i = 0; i < N; ++i) {
			scanf("%lld %lld", &r, &h);
			p.push_back(make_pair(r, h));
		}
		vector<pair<ll, ll> > v;
		for (int i = 0; i < p.size(); ++i)
			v.push_back(make_pair(up(p[i].first), side(p[i].first, p[i].second)));

		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());
		ll us_max = 0;
		for (int i = 0; i <= N - K; ++i)
		{
			vector<ll> tmp;
			ll sum_su = v[i].second + v[i].first;
			for (int j = i + 1; j < N; ++j)
				tmp.push_back(v[j].second);
			sort(tmp.begin(), tmp.end());
			reverse(tmp.begin(), tmp.end());
			for (int j = 0; j < K - 1; ++j)
				sum_su += tmp[j];
			us_max = max(us_max, sum_su);
		}
		printf("Case #%d: %.9lf\n", t, (double)us_max*PI);
	}
}

