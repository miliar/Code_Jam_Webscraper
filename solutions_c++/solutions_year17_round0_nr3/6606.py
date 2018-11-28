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

map<ll,ll> ma1;

void f(ll n){
	if(n<1)return;
	if(ma1[n]!=0)return;
	ma1[n] = 1;
	ll a = n-1;
	if(a%2==0){
		f(a/2);
	}
	else{
		f(a/2);
		f(a/2+1);
	}
}

ll d[1000];

int main(){
	ll T;
	cin>>T;
	rep(t,0,T){
		ll n,k;
		cin>>n>>k;
		ma1.clear();
		f(n);
		vector<ll> v;
		map<ll,ll>::iterator itr = ma1.begin();
		while(itr!=ma1.end()){
			ll a = (*itr).fi;
			ll b = (*itr).se;
			v.pb(a);
			itr++;
		}
		sort(all(v));
		reverse(all(v));
		map<ll,ll> ma;
		map<ll,ll> mi;
		rep(i,0,v.sz){
			ma[i] = v[i];
			mi[v[i]] = i;
		}
		clr(d,0);
		d[0] = 1;
		rep(i,0,v.sz){
			ll a = ma[i];
			ll b = a-1;
			if(b%2==0){
				if(b/2>0)d[mi[b/2]] += d[i]*2;
			}
			else{
				if(b/2>0)d[mi[b/2]] += d[i];
				d[mi[b/2+1]] += d[i];
			}
		}
		rep(i,0,1000){
			k -= d[i];
			if(k<=0){
				ll a = ma[i];
				ll b = a-1;
				if(b%2==0){
					printf("Case #%d: %d %d\n", t+1, b/2, b/2);
				}
				else{
					printf("Case #%d: %d %d\n", t+1, b/2+1, b/2);
				}
				break;
			}
		}
	}
	return 0;
}


