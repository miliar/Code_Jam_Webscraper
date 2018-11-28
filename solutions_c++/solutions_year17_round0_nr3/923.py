#include <cstdio>
#include <cstring>

using namespace std;

const int MAXL = 20001;

long long ns[MAXL], cs[MAXL];
long long n, K, ans;

long long solve()
{
	if (n <= K)
		return 0;
	int h = 0, t = 0;
	ns[0] = n; cs[0] = 1;
	while (h <= t){
		if (cs[h] >= K) return ns[h];
		K -= cs[h];
		if (ns[h] & 1){//odd
			if (ns[t] > ns[h]/2){
				ns[++ t] = ns[h]/2;
				cs[t] = 0;
			}
			cs[t] += cs[h] * 2;
		} else {//even
			if (ns[t] > ns[h]/2){
				ns[++ t] = ns[h]/2;
				cs[t] = 0;
			}
			cs[t] += cs[h];
			if (ns[t] > ns[h]/2-1){
				ns[++ t] = ns[h]/2-1;
				cs[t] = 0;
			}
			cs[t] += cs[h];
		}
		h ++;
	}
	return ns[t];
}

int main()
{
	freopen("c2.in", "r", stdin);
	freopen("c2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++)
	{
		scanf("%lld%lld", &n, &K);
		ans = solve();
		printf("Case #%d: %lld %lld\n", t, ans/2, (ans-1)/2);
	}
	return 0;
}
