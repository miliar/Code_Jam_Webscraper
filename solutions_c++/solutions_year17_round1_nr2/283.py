#include <bits/stdc++.h>
using namespace std;

#define FOR(i,l,r) for(int i = (int) (l);i < (int) (r);i++)
#define ALL(x) x.begin(),x.end()
template<typename T> bool chmax(T& a,const T& b){ return a < b ? (a = b,true) : false; }
template<typename T> bool chmin(T& a,const T& b){ return b < a ? (a = b,true) : false; }
typedef long long ll;

int T,N,P;
const ll MAX = 1e7;

int main()
{
	scanf("%d",&T);
	FOR(testCase,1,T + 1){
		scanf("%d%d",&N,&P);
		vector<ll> A(N);
		FOR(i,0,N){
			scanf("%lld",&A [i]);
		}
		vector< vector<ll> > Q(N,vector<ll>(P));
		FOR(i,0,N){
			FOR(j,0,P){
				scanf("%lld",&Q [i] [j]);
			}
			sort(ALL(Q [i]));
		}
		vector<ll> idx(N,0);
		ll ans = 0;
		while(true){
			ll l = -MAX,r = MAX;
			bool ok = true;
			FOR(i,0,N){
				ll p = (10 * Q [i] [idx [i]] + A [i] * 11 - 1) / (A [i] * 11);
				ll q = (10 * Q [i] [idx [i]]) / (A [i] * 9); 
				chmax(l,p);
				chmin(r,q);
				if(l > r){
					ok = false;
					break;
				}
			}
			if(ok){
				ans++;
				bool flag = false;
				FOR(i,0,N){
					if(++idx [i] == P){
						flag = true;
						break;
					}
				}
				if(flag) break;
			}
			else{
				ll mn = MAX,mnIdx = -1;
				FOR(i,0,N){
					ll q = (10 * Q [i] [idx [i]]) / (A [i] * 9);
					if(q < mn){
						mn = q;
						mnIdx = i;
					}
				}
				if(++idx [mnIdx] == P) break;
			}
		}
		printf("Case #%d: %lld\n",testCase,ans);
	}

	return 0;
}
