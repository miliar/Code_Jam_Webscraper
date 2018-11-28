#include <bits/stdc++.h>
using namespace std;

#define all(v) (v).begin(), (v).end()
typedef long long lld;

int T;
lld N, K;

vector<lld> div(lld n)
{
	if (n&1) return {n>>1, n>>1};
	return {(n>>1)-1, n>>1};
}

int main()
{
	for (scanf("%d", &T);T--;){
		static int ts = 0;
		printf("Case #%d: ", ++ts);

		scanf("%lld%lld", &N, &K);
		map <lld, lld> now, nxt;
		now[N] = 1;
		while (K){
			nxt.clear();
			for (auto it=now.rbegin();it!=now.rend();it++){
				auto v = div(it->first);
				if (it->second < K) K -= it->second;
				else{ printf("%lld %lld\n", v[1], v[0]); K = 0; break; }
				nxt[v[0]] += it->second;
				nxt[v[1]] += it->second;
			}
			now = nxt;
		}
	}
}