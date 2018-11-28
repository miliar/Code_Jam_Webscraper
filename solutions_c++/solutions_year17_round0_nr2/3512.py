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
	ll n;cin>>n;
	string s=to_string(n);
	vector<ll> v(s.size());
	rep(i,s.size())v[i]=stoi(s.substr(i,1));

	for(ll i=s.size()-2;i>=0;i--){
		if(v[i+1]<v[i]){
			v[i]--;
			FOR(j,i+1,s.size()){
				v[j]=9;
			}
		}
	}

	ll ans=0;
	rep(i,s.size()){
		ll temp=v[i];
		rep(j,s.size()-i-1){
			temp*=10;
		}
		ans+=temp;
	}

	//昇順で数えた時の最後の数は何か.
	//下がった箇所を見つけて，以降を9に
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














