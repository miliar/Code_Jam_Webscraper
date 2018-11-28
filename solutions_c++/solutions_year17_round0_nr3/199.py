#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

typedef long long LL;

const int oo = 0x3f3f3f3f;

LL n, K;

int main()
{
#ifdef matthew99
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int case_count;
	scanf("%d", &case_count);
	for (int case_id = 1; case_id <= case_count; ++case_id)
	{
		printf("Case #%d: ", case_id);
		scanf("%I64d%I64d", &n, &K);
		map<LL, LL, greater<LL> > all;
		++all[n];
		for (auto u : all)
		{
			if (u.y >= K) 
			{
				printf("%I64d %I64d\n", u.x >> 1, (u.x - 1) >> 1);
				break;
			}
			K -= u.y;
			all[u.x >> 1] += u.y;
			all[(u.x - 1) >> 1] += u.y;
		}
	}
	return 0;
}
