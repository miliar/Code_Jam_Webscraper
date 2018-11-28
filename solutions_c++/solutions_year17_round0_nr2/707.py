#include <bits/stdc++.h>
using namespace std;

#define FOR(i,l,r) for(int i = (int) (l);i < (int) (r);i++)
#define ALL(x) x.begin(),x.end()
template<typename T> bool chmax(T& a,const T& b){ return a < b ? (a = b,true) : false; }
template<typename T> bool chmin(T& a,const T& b){ return b < a ? (a = b,true) : false; }
typedef long long ll;

int T,N;
string S;

bool sorted(ll x)
{
	if(x < 0) return false;
	vector<int> v;
	do{
		v.push_back(x % 10);
	}while(x /= 10);
	FOR(i,1,v.size()){
		if(v [i] > v [i - 1]) return false;
	}
	return true;
}

ll my_pow(ll x,ll y)
{
	ll res = 1;
	while(y){
		if(y & 1) res *= x;
		x *= x;
		y >>= 1;
	}
	return res;
}

int main()
{
	scanf("%d",&T);
	FOR(testCase,1,T + 1){
		cin >> S;
		N = S.size();
		ll ans = 0;
		if(sorted(stoll(S))){
			chmax(ans,stoll(S));
		}
		FOR(i,1,N){
			string str = S;
			FOR(j,i,N){
				str [j] = '9';
			}
			if(sorted(stoll(str) - my_pow(10,N - i))){
				chmax(ans,stoll(str) - my_pow(10,N - i));
			}
		}
		printf("Case #%d: %lld\n",testCase,ans);
	}

	return 0;
}
