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

string ntos(long long n){
  string s;
  stringstream ss;
  ss << n;
  ss >> s;
  return s;
}

long long ston(string s){
  long long n;
  sscanf(s.c_str(), "%lld", &n);
  return n;
}

int main(){
	ll T;
	cin>>T;
	rep(t,0,T){
		string s;
		cin>>s;
		s += "9";
		while(1){
			int flag = 1;
			rep(i,0,s.sz-1){
				if(s[i]>s[i+1]){
					flag = 0;
					s[i] = ((s[i]-'0')-1)+'0';
					rep(j,i+1,s.sz){
						s[j] = '9';
					}
				}
			}
			if(flag == 1)break;
		}
		s = ntos(ston(s));
		string ans;
		rep(i,0,s.sz-1){
			ans += s[i];
		}
		printf("Case #%d: %s\n", t+1, ans.c_str());
	}
	return 0;
}