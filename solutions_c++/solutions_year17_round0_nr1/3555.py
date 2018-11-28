#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <stack>
#include <numeric>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <functional>

using namespace std;
typedef long long ll;
#define pl pair<ll,ll>
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n) for(int i=0;i<(n);++i)
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin(); itr!=c.end(); itr++)
#define dbg(x) cout << #x"="<< (x) << endl
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back(a) 
#define in(x) cin >> x;
#define all(x) (x).begin(), (x).end()
#define INF 2147483600
#define fi first
#define se second
const ll MODP = 1000000007;

void solve(void){
	string s;
	ll k,ans=0;
	cin>>s>>k;
	vector<ll> v(s.size());
	rep(i,s.size()){
		if(s[i]=='+'){
			v[i]=1;
		}else if(s[i]=='-'){
			v[i]=-1;
		}
	}
	//左から順番に見ていこう.
	//2ループでも解ける
	rep(i,s.size()){
		if(v[i]==-1){
			ans++;
			FOR(j,i,k+i){
				if(k+i>s.size()){
					cout<<"IMPOSSIBLE";
					return;
				}{
					v[j]*=-1;
				}
			}
		}
	}
	cout << ans;
	return;
}

int main(void){

	int T;
	cin >> T;
	for(int tcnt=1;tcnt<=T;tcnt++){
		cout << "Case #" << tcnt << ": ";
		solve();
		cout << endl;
	}
	return 0;
}














