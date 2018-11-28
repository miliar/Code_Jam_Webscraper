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

ll dp[110][110][110];
 
int main() {
  ll T;
  cin>>T;
  rep(t,0,T){
    ll n,p;
    cin>>n>>p;
    vector<ll> v;
    rep(i,0,n){
    	ll a;
    	cin>>a;
    	v.pb(a);
    }
    ll ans = 0;
    if(p==2){
    	ll odd = 0;
    	ll even = 0;
    	rep(i,0,v.sz){
    		if(v[i]%2==1)odd++;
    		else even++;
    	}
    	ans += odd/2;
    	ans += even;
    	ans += odd%2;
    }
    else if(p==3){
    	ll zero = 0;
    	ll one = 0;
    	ll two = 0;
    	rep(i,0,v.sz){
    		if(v[i]%3==1)one++;
    		else if(v[i]%3==2)two++;
    		else zero++;
    	}
    	ans += zero;
    	ll mx = 0;
    	rep(i,0,min(one,two)+1){
    		ll one1 = one-i;
    		ll two1 = two-i;
    		ll x = i+(one1/3)+(two1/3);
    		ll one2 = one1%3;
    		ll two2 = two1%3;
    		if(one2==0){
    			if(two2>0){
    				x+=1;
    			}
    		}
    		if(one2==1){
    			if(two2>1)x+=2;
    			else x+=1;
    		}
    		if(one2==2){
    			if(two2==0)x+=1;
    			else x+=2;
    		}
    		mx = max(mx,x);
    	}
    	ans += mx;
    }
    else if(p==4){
    	ll zero = 0;
    	ll one = 0;
    	ll two = 0;
    	ll three = 0;
    	rep(i,0,v.sz){
    		if(v[i]%4==1)one++;
    		else if(v[i]%4==2)two++;
    		else if(v[i]%4==3)three++;
    		else zero++;
    	}
    	ans += zero;
    	clr(dp,0);
    	rep(i,0,110){
    		rep(j,0,110){
    			rep(k,0,110){
    				ll one1 = one-i;
    				ll two1 = two-j;
    				ll three1 = three-k;
    				if(one1<0)continue;
    				if(two1<0)continue;
    				if(three1<0)continue;
    				if(one1>=4){
    					dp[i+4][j][k] = max(dp[i+4][j][k],dp[i][j][k]+1);
    				}
    				if(two1>=2){
    					dp[i][j+2][k] = max(dp[i][j+2][k],dp[i][j][k]+1);
    				}
    				if(one1>=2&&two1>=1){
    					dp[i+2][j+1][k] = max(dp[i+2][j+1][k],dp[i][j][k]+1);
    				}
    				if(one1>=1&&three1>=1){
						dp[i+1][j][k+1] = max(dp[i+1][j][k+1],dp[i][j][k]+1);
    				}
					if(two1>=1&&three1>=2){
    					dp[i][j+1][k+2] = max(dp[i][j+1][k+2],dp[i][j][k]+1);
    				}  
    				if(three1>=4){
    					dp[i][j][k+4] = max(dp[i][j][k+4],dp[i][j][k]+1);
    				}    				
    			}
    		}
    	}
    	ll mx = 0;
    	rep(i,0,110){
    		rep(j,0,110){
    			rep(k,0,110){
    				ll one1 = one-i;
    				ll two1 = two-j;
    				ll three1 = three-k;
    				if(one1<0)continue;
    				if(two1<0)continue;
    				if(three1<0)continue;
    				int flag = 1;
    				if(one1>=4){
    					flag=0;
    				}
    				if(two1>=2){
    					flag=0;
    				}
    				if(one1>=2&&two1>=1){
    					flag=0;
    				}
    				if(one1>=1&&three1>=1){
						flag=0;
    				}
					if(two1>=1&&three1>=2){
    					flag=0;
    				}  
    				if(three1>=4){
    					flag=0;
    				}
    				if(flag == 1){
    					if(one1>0||two1>0||three1>0){
    						mx = max(mx,dp[i][j][k]+1);
    					}
    					else{
    						mx = max(mx,dp[i][j][k]);
    					}
    				}			
    			}
    		}
    	}
    	ans += mx;
    }
    printf("Case #%d: %d\n", t+1, ans);
  }
	return 0;
}