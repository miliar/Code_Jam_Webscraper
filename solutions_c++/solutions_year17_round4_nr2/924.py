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

ll d1[1010];
ll d2[1010];
 
int main() {
  ll T;
  cin>>T;
  rep(t,0,T){
    ll n,c,m;
    cin>>n>>c>>m;
    ll ans1 = 0;
   	ll ans2 = 0;
    if(c==2){
    	ll c1 = 0;
    	ll c2 = 0;
    	clr(d1,0);
    	clr(d2,0);
   		rep(i,0,m){
    		ll a,b;
    		cin>>a>>b;
    		a--;b--;
    		if(b==0){
    			c1++;
    			d1[a]++;
    		}
    		else{
    			c2++;
    			d2[a]++;
    		}
    	}
    	if(c2>c1){
    		swap(c1,c2);
    		rep(i,0,1010){
    			swap(d1[i],d2[i]);
    		}
    	}
    	rep(i,1,m+1){
    		ll space = 0;
    		ll change = 0;
    		int flag = 1;
    		if(i<c1)continue;
    		rep(j,0,n){
    			ll a = d1[j];
    			ll b = i-a;
    			ll c = d2[j];
    			if(c>b){
    				ll d = c-b;
    				if(space>=d){
    					change += d;
    					space -= d;
    				}
    				else{
    					flag = 0;
    					break;
    				}
    			}
    			else{
    				space += b-c;
    			}
    		}
    		if(flag == 1){
    			ans1 = i;
    			ans2 = change;
    			goto g1;
    		}
    	}
    }
    g1:;
    printf("Case #%d: %d %d\n", t+1, ans1, ans2);
  }
	return 0;
}