#include <bits/stdc++.h>
using namespace std;

const int MAX_V = 105;
int T, HD, AD, HK, AK, B, D;
long long dp[MAX_V][MAX_V][MAX_V][MAX_V]; // hd, ad, hk, ak

struct state{
	int hd, ad, hk, ak;
	state(int _hd, int _ad, int _hk, int _ak) :
		hd(_hd), ad(_ad), hk(_hk), ak(_ak) {}
};

queue<state> que;

state transform(state s){
	int hd = min(MAX_V-1, max(0, s.hd));
	int ad = min(MAX_V-1, max(0, s.ad));
	int hk = min(MAX_V-1, max(0, s.hk));
	int ak = min(MAX_V-1, max(0, s.ak));
	return state(hd, ad, hk, ak);
}

long long get(state s){
	s = transform(s);
	return dp[s.hd][s.ad][s.hk][s.ak];
}

void put(state s, long long v){
	s = transform(s);
	if(get(s) == -1){
		que.push(s);
		dp[s.hd][s.ad][s.hk][s.ak] = v;
	}
}

int main(){
	if(fopen("test.in","r")){
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t){
		cin >> HD >> AD >> HK >> AK >> B >> D;
		memset(dp, -1, sizeof(dp));
		while(!que.empty()) que.pop();
		long long best = INT_MAX;
		put(state(HD, AD, HK, AK), 0);
		while(!que.empty()){
			state s = que.front();
			que.pop();
			long long v = get(s);
			++v;

			state attack = s;
			attack.hk -= attack.ad;
			if(attack.hk <= 0){
				best = min(best, v);
				// break;
			}
			attack.hd -= attack.ak;
			if(attack.hd > 0) put(attack, v);

			state buff = s;
			buff.ad += B;
			buff.hd -= buff.ak;
			if(buff.hd > 0) put(buff, v);

			state cure = s;
			cure.hd = HD;
			cure.hd -= cure.ak;
			if(cure.hd > 0) put(cure, v);

			state debuff = s;
			debuff.ak -= D;
			debuff.hd -= debuff.ak;
			if(debuff.hd > 0) put(debuff, v);
		}
		cout << "Case #" << t << ": ";
		if(best == INT_MAX) cout << "IMPOSSIBLE";
		else cout << best;
		cout << endl;
	}
}
