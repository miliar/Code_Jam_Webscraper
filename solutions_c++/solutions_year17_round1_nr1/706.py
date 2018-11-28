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
 
int main(){
	ll T;
	cin>>T;
	rep(t,0,T){
		ll r,c;
		cin>>r>>c;
		vector<string> vs;
		rep(i,0,r){
			string s;
			cin>>s;
			vs.pb(s);
		}
		rep(y,0,r){
			rep(x,0,c-1){
				if(vs[y][x]!='?'&&vs[y][x+1]=='?'){
					vs[y][x+1]=vs[y][x];
				}
			}
		}
		rep(y,0,r){
			per(x,1,c){
				if(vs[y][x-1]=='?'&&vs[y][x]!='?'){
					vs[y][x-1]=vs[y][x];
				}			
			}
		}
		rep(y,0,r-1){
			per(x,0,c){
				if(vs[y][x]!='?'&&vs[y+1][x]=='?'){
					vs[y+1][x]=vs[y][x];
				}			
			}
		}
		per(y,1,r){
			per(x,0,c){
				if(vs[y][x]!='?'&&vs[y-1][x]=='?'){
					vs[y-1][x]=vs[y][x];
				}			
			}
		}
		printf("Case #%d:\n", t+1);
		rep(y,0,r){
			cout << vs[y] << endl;
		}
	}
	return 0;
}
