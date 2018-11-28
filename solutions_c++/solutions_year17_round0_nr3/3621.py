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
	ll n,k,cnt=0;cin>>n>>k;
	//人から最も離れるように入る．
	//lognで出す
	//2つに分ける
	ll dec=1;
	vector<pl> v(2);
	v[0].fi=n;
	v[0].se=1;
	while(k>0){
		if(k-dec>0){
			k-=dec;
			map<ll,ll> temp;
			rep(i,2){
				if(v[i].se!=0){
					temp[floor(double(v[i].fi-1)/2)]+=v[i].se;
					temp[ceil(double(v[i].fi-1)/2)]+=v[i].se;
				}
			}
			ll j=0;
			foreach(itr,temp){
				v[j].fi=itr->fi;
				v[j].se=itr->se;
				j++;
			}
			temp.clear();
		}else{
			break;
		}
		dec*=2;
	}
	

	ll res;
	rep(i,2){
		if(v[i].se!=0){
			res=v[i].se-k;
		}
	}
	ll MAX,MIN;
	//大きい方はなくなり小さい方を砕いた
	if(res<0){
		MAX=ceil(double(v[0].fi-1)/2);
		MIN=floor(double(v[0].fi-1)/2);
	}else if(res==0){//大きい方がなくなった
		if(v[1].se!=0){
			MAX=ceil(double(v[1].fi-1)/2);
			MIN=floor(double(v[1].fi-1)/2);
		}else{
			MAX=ceil(double(v[0].fi-1)/2);
			MIN=floor(double(v[0].fi-1)/2);
		}
	}else{//大きいのがまだいる.
		if(v[1].se!=0){
			MAX=ceil(double(v[1].fi-1)/2);
			MIN=floor(double(v[1].fi-1)/2);
		}else{
			MAX=ceil(double(v[0].fi-1)/2);
			MIN=floor(double(v[0].fi-1)/2);
		}
	}
	// dbg(k);
	// rep(i,2){
	// 	cout<<i<<' '<<v[i].fi<<' '<<v[i].se<<endl;
	// }
	cout<< MAX << ' ' <<MIN;
	// cout << ans;
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














