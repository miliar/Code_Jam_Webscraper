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
#define FOR(i,a,b) for(ll i=(a);i<(b);++i)
#define rep(i,n) for(ll i=0;i<(n);++i)
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
	ll r,c; cin>>r>>c;
	vector<string> s(r);
	map<char,ll> flag;
	rep(i,r){
		cin>>s[i];
	}

	rep(i,r){
		// dbg(i);
		rep(j,c){
			// dbg(j);
			if(s[i][j]!='?'&& flag[s[i][j]]==0){
				ll up=i,lf=j,dn=i,rt=j;
				rep(k,r){
					rep(l,c){
						if(s[k][l]==s[i][j]){
							up=min(up,k);
							lf=min(lf,l);
							dn=max(dn,k);
							rt=max(rt,l);
						}
					}
				}

				FOR(k,up,min(dn+1,r)){
					FOR(l,lf,min(rt+1,c)){
						s[k][l]=s[i][j];
					}
				}
				
				for(ll l=min(lf-1,c-1);l>=0;l--){
					bool flag2=true;
					FOR(k,up,min(dn+1,r)){
						if(s[k][l]!='?'){
							flag2=false;
						}
					}
					if(flag2){
						FOR(k,up,min(dn+1,r)){
							s[k][l]=s[i][j];
							lf=l;
						}
					}else{
						break;
					}
				}

				for(ll l=min(rt+1,c-1);l<c;l++){
					bool flag2=true;
					FOR(k,up,min(dn+1,r)){
						if(s[k][l]!='?'){
							flag2=false;
						}
					}
					if(flag2){
						FOR(k,up,min(dn+1,r)){
							s[k][l]=s[i][j];
							rt=l;
						}
					}else{
						break;
					}
				}

				for(ll k=min(up-1,r-1);k>=0;k--){
					bool flag2=true;
					FOR(l,lf,min(rt+1,c)){
						if(s[k][l]!='?'){
							flag2=false;
						}
					}
					if(flag2){
						FOR(l,lf,min(rt+1,c)){
							s[k][l]=s[i][j];
							up=k;
						}
					}else{
						break;
					}
				}
		
				for(ll k=min(dn+1,r-1);k<r;k++){
					// dbg(k);
					bool flag2=true;
					FOR(l,lf,min(rt+1,c)){
						if(s[k][l]!='?'){
							flag2=false;
						}
					}
					if(flag2){
						FOR(l,lf,min(rt+1,c)){
							s[k][l]=s[i][j];
							dn=k;
						}
					}else{
						break;
					}
				}
				// dbg("fin");
				// dbg(2);
				flag[s[i][j]]++;
			}
			// dbg("ok");
		}
	}
	rep(i,r){
		cout<<s[i]<<endl;
	}
	// //L字にならなければいい.
	// //まず四角にする.
	// rep(i,r){
	// 	rep(j,c){
	// 		//?じゃない場所を見つける
	// 		if(s[i][j]!='?'){
	// 			//その場所の手前から？じゃ無くなるところまで
	// 			//Gがあるところにでてきたら
	// 			ll lf=0,rt=j;
	// 			rep()
	// 		}
	// 	}
	// }
	return;
}

//正方領域のcheckを行う.
void bps(int i, int j){

}

int main(void){

	int T;
	cin >> T;
	for(int tcnt=1;tcnt<=T;tcnt++){
		cout << "Case #" << tcnt << ": ";
		cout<<endl;
		solve();
		// cout << endl;
	}
	return 0;
}














