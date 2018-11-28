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
		string s;
		cin>>s;
		ll k;
		cin>>k;
		ll c = 0;
		rep(i,0,s.sz-k+1){
			if(s[i]=='-'){
				c++;
				rep(j,i,i+k){
					if(s[j]=='-')s[j]='+';
					else s[j]='-';
				}
			}
		}
		int flag = 1;
		rep(i,0,s.sz){
			if(s[i]=='-')flag=0;
		}

		if(flag == 0){
			printf("Case #%d: IMPOSSIBLE\n", t+1);
		}
		else{
			printf("Case #%d: %d\n", t+1, c);
		}
	}
	return 0;
}