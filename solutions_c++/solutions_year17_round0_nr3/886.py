#include <bits/stdc++.h>

#define maxn 200100
#define sq 333
#define logn 23
#define inf 0x3F3F3F3F
#define linf 0x3F3F3F3F3F3F3F3FLL
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define mod 1000000007LL

using namespace std;

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef priority_queue<pii, vii, greater<pii> > pq;

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

int t;
ll n, qtd;
map<ll, ll> m;
map<ll, ll>::iterator it;

int main() {
	scanf("%d", &t);
	for(int cas = 1; cas <= t; ++cas) {
		scanf("%lld %lld", &n, &qtd);
		m.clear();
		m[n] = 1;
		ll maxi, mini;
		while(qtd > 0) {
			it = m.end(); it--;
			ll tam = it->first;
			ll sai = min(it->second, qtd);
			if(sai == it->second) {
				m.erase(it);
			}
			if(tam > 1) {
				m[tam/2] += sai;
				if(tam-1-(tam/2) > 0) {
					m[tam-1-(tam/2)] += sai;
				}
			}
			if(qtd == sai) {
				maxi = max(tam/2, tam-1-(tam/2));
				mini = min(tam/2, tam-1-(tam/2));
			}
			qtd -= sai;
		}
		printf("Case #%d: %lld %lld\n", cas, maxi, mini);
	}

	return 0;
}