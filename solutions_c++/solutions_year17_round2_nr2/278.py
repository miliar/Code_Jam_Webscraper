#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = a; i < (b); ++i)
#define rrep(i,a,b) for(int i = b; i --> (a);)
#define all(v) v.begin(),v.end()
#define trav(x,v) for(auto &x : v)
#define sz(v) (int)(v).size()
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

string roy = "RYBGVO";

void solve(){
	int n;
	int cnt[2][3] = {};
	cin >> n;
	cin >> cnt[0][0] >> cnt[1][2] >> cnt[0][1];
	cin >> cnt[1][0] >> cnt[0][2] >> cnt[1][1];
	rep(t,0,3) if(cnt[0][t] + cnt[1][t] == n){
		if(cnt[0][t] != cnt[1][t]) cout << "IMPOSSIBLE" << endl;
		else {
			rep(_,0,cnt[0][t]) cout << roy[t] << roy[t+3];
			cout << endl;
		}
		return;
	}
	rep(t,0,3) if(cnt[1][t] > max(0,cnt[0][t]-1)){
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	vi v(3);
	rep(t,0,3) v[t] = cnt[0][t] - cnt[1][t];
	rep(t,0,3) if(v[t]*2 > n){
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	vi ans;
	int prev = -1;
	rep(t,0,3){
		if(v[t] != 0){
			ans.push_back(t);
			--v[t];
			prev = t;
			break;
		}
	}
	while(true){
		int mx = 0;
		rep(t,0,3) if(t != prev) mx = max(mx, v[t]);
		if(mx == 0) break;
		rep(t,0,3) if(t != prev && v[t] == mx){
			ans.push_back(t);
			prev = t;
			--v[t];
			break;
		}
	}
	vector<bool> klar(3);

	string svar;

	trav(t, ans){
		svar.push_back(roy[t]);
		if(!klar[t]){
			rep(_,0,cnt[1][t]){
				svar.push_back(roy[t+3]);
				svar.push_back(roy[t]);
			}
		}
		klar[t] = 1;
	}
	//rep(t,0,3) assert(count(all(svar), roy[t]) == cnt[0][t]);
	//assert(sz(svar) == n);
	//rep(i,0,n) assert(svar[i] != svar[(i+1)%n]);
	cout << svar << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int n;
	cin >> n;
	rep(i,1,n+1){
		cout << "Case #" << i << ": ";
		solve();
	}
}