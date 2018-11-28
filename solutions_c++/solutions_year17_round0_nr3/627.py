#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < int(n); i++)
#define FOREACH(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define SIZE(v) ((int)(v).size())
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define ll long long
#define pii pair<int, int>

int main(){
	int T;
	scanf("%d", &T);
	REP(t, T){
		ll N, K;
		scanf("%lld %lld", &N, &K);
		if(N == K){
			printf("Case #%d: 0 0\n", t + 1);
		}
		else{
			map<ll, ll, greater<ll> > dic;
			dic[N] = 1ll;
			ll cnt = 0ll, L;
			while(true){
				map<ll, ll, greater<ll> >::iterator it = dic.begin();
				ll l = it->st;
				ll cnt0 = it->nd;
			
				if(cnt + cnt0 >= K){
					L = l;
					break;
				}
				
				dic.erase(l);
				
				if(l == 1ll) continue;
				else if(l == 2ll) dic[1ll] += cnt0;
				else{
					dic[l/2ll] += cnt0;
					if(l%2ll == 1ll) dic[l/2ll] += cnt0;
					else dic[l/2ll - 1ll] += cnt0;
				}
				
				cnt += cnt0;
			}
			printf("Case #%d: %lld %lld\n", t + 1,  L/2ll, L/2ll - (L%2ll == 0ll ? 1ll : 0ll)); 
		}
	}
}
