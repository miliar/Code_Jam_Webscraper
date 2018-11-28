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


auto divide(ll n){
	n--;
	const ll a=n/2,b=n-a;
	return make_tuple(a,b);
}

int main(void){
	int T;
	cin >> T;	
	rep(testcase,1,T+1){
		ll n,k;
		cin >> n >> k;
		
		map<ll,ll> cand;
		cand[n]=1LL;

		ll a,b;			
		while(k>0){
			auto it=rbegin(cand);
			tie(a,b)=divide(it->first);
			ll num=min(it->second,k);
			cand.erase(it->first);
			cand[a]+=num,cand[b]+=num,k-=num;
		}

		cout << "Case #" << testcase << ": " << max(a,b) << " " << min(a,b) << endl;
	}
	return 0;
}