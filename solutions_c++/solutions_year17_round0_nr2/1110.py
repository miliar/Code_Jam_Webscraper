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

ll solve(string s){
	const int n=s.size();
	ll dp[20][10][2];
	rep(i,20)rep(j,10)rep(k,2) dp[i][j][k]=-1LL;
	dp[0][0][0]=0LL;

	rep(i,n)rep(j,10)rep(le,2){
		const ll cur=dp[i][j][le];
		if(cur==-1LL) continue;
		
		rep(d,10){
			const int ni=i+1;
			if(d<j) continue;
			const int nj=d;
			int nle=le,tar=s[i]-'0';
			if(nle==0 and d > tar) continue;
			if(d < tar) nle=1;
			chmax(dp[ni][nj][nle],10LL*cur+d);
		}
	}

	ll ans=0LL;
	rep(j,10)rep(k,2) chmax(ans,dp[n][j][k]);
	return ans;
}

int main(void){
	int T;
	cin >> T;	
	rep(testcase,1,T+1){
		string n;
		cin >> n;
		cout << "Case #" << testcase << ": " << solve(n) << endl;
	}
	return 0;
}