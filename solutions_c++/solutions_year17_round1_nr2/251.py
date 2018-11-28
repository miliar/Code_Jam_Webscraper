#include <bits/stdc++.h>

#define _overload(_1,_2,_3,name,...) name
#define _rep(i,n) _range(i,0,n)
#define _range(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload(__VA_ARGS__,_range,_rep,)(__VA_ARGS__)

#define _rrep(i,n) _rrange(i,n,0)
#define _rrange(i,a,b) for(int i=int(a)-1;i>=int(b);--i)
#define rrep(...) _overload(__VA_ARGS__,_rrange,_rrep,)(__VA_ARGS__)

#define _all(arg) begin(arg),end(arg)
#define uniq(arg) sort(_all(arg)),(arg).erase(unique(_all(arg)),end(arg))
#define getidx(ary,key) lower_bound(_all(ary),key)-begin(ary)
#define clr(a,b) memset((a),(b),sizeof(a))
#define bit(n) (1LL<<(n))
#define popcount(n) (__builtin_popcountll(n))

template<class T>bool chmax(T &a, const T &b) { return (a<b)?(a=b,1):0;}
template<class T>bool chmin(T &a, const T &b) { return (b<a)?(a=b,1):0;}

using namespace std;
using ll=long long;

int main(void){
	int T;
	cin >> T;	
	rep(testcase,1,T+1){
		int N,P;
		cin >> N >> P;
		
		ll ing[55];
		rep(i,N) cin >> ing[i];
		ll pack[55][55];
		rep(i,N)rep(j,P) cin >> pack[i][j];


		using pll=pair<ll,ll>;
		pll plimit[55][55];
		
		const ll limit=1000010;
		
		rep(i,N)rep(j,P){
			plimit[i][j].first=limit;
			plimit[i][j].second=0;
			
			ll cur=pack[i][j];

			for(ll k=1;k<limit;++k){
				const ll pro=ing[i]*k;
				const ll low=(9*pro+10-1)/10;
				const ll high=(11*pro)/10;

				if(low <= cur and cur <=high){
					chmin(plimit[i][j].first,k);
					chmax(plimit[i][j].second,k);
				}
			}
		}

		int ans = 0;
		priority_queue<pll,vector<pll>,greater<pll>> pq[55];

		rep(i,N)rep(j,P){
			if(plimit[i][j].first==limit) continue;
			pq[i].push(plimit[i][j]);
		}

		while(1){
			bool can = true;
			rep(i,N) if(pq[i].empty()) can=false;
			if(can == false) break;

			pll cur = pll(0,limit);
			rep(i,N){
				pll in = pq[i].top();
				chmax(cur.first,in.first);
				chmin(cur.second,in.second);
			}

			if(cur.first > cur.second){
				ll cmin = limit,idx = 0;
				rep(i,N) if(chmin(cmin,pq[i].top().second)) idx = i;
				pq[idx].pop();
			}else{
				ans++;
				rep(i,N) pq[i].pop();
			}
		}

		
		cout << "Case #" << testcase << ": " << ans << endl;
	}
	return 0;
}