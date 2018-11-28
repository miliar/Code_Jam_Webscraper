#include <algorithm>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
 
using namespace std;
 
typedef long long ll;
 
#define sz size()
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(c) (c).begin(), (c).end()
#define rep(i,a,b) for(ll i=(a);i<(b);++i)
#define per(i,a,b) for(ll i=(b-1);i>=(a);--i)
#define clr(a, b) memset((a), (b) ,sizeof(a))
#define ctos(c) string(1,c)
#define print(x) cout<<#x<<" = "<<x<<endl;
 
#define MOD 1000000007

ll n,q;
ll d[55][55];

ll check(vector<ll> &vr, vector<vector<ll> > &vq, ll p){
	rep(i,1,1200000){
		ll b = vq[0][p];
		vector<ll> vindex;
		if(90LL*vr[0]*i <= 100LL*b && 100LL*b <= 110LL*vr[0]*i){
			vindex.pb(p);
			rep(j,1,n){
				ll a = vr[j]*i;
				long long low = 0;
				long long high = q-1;

				while(low < high){
					long long mid = (high + low) >> 1;

					if(90LL*a <= 100LL*vq[j][mid] && d[j][mid]==0){
						high = mid;
					}
					else{
						low = mid + 1;
					}
				}
				if(90LL*a <= 100LL*vq[j][low] && 100LL*vq[j][low] <= 110LL*a){
					vindex.pb(low);
				}
			}
			if(vindex.sz==n){
				rep(j,0,n){
					rep(k,0,q){
						if(k <= vindex[j]){
							d[j][k] = 1;
						}
					}
				}
				return 1;
			}
		}
	}
	return 0;
}

int main(){
	ll T;
	cin>>T;
	rep(t,0,T){
		cin>>n>>q;
		vector<vector<ll> > vq(n,vector<ll>());
		vector<ll> vr;
		rep(i,0,n){
			ll a;
			cin>>a;
			vr.pb(a);
		}
		rep(i,0,n){
			rep(j,0,q){
				ll a;
				cin>>a;
				vq[i].pb(a);
			}
			sort(all(vq[i]));
		}
		ll ans = 0;
		clr(d,0);
		rep(i,0,q){
			ans += check(vr,vq,i);
		}
		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}
