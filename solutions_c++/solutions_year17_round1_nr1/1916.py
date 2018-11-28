#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

#define REP(a, b, c) for(int a=(b); a<(c); a++)
#define dREP(a, b, c) for(int a=(b); a>=(c); a--)

int T, R, C;

vector<string> g;

void solve(){
	dREP(i, (R-2), 0){
		REP(j, 0, C){
			if(g[i][j]=='?') g[i][j] = g[i+1][j];
		}
	}
	REP(i, 1, R){
		REP(j, 0, C){
			if(g[i][j]=='?') g[i][j] = g[i-1][j];
		}
	}
	dREP(j, (C-2), 0){
		REP(i, 0, R){
			if(g[i][j]=='?') g[i][j] = g[i][j+1];
		}
	}
	REP(j, 1, C){
		REP(i, 0, R){
			if(g[i][j]=='?') g[i][j] = g[i][j-1];
		}
	}
}

int main(){
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> R >> C;
		g.clear();
		string s;
		for(int i=0; i<R; i++){
			cin >> s;
			g.push_back(s);
		}
		solve();
		cout << "Case #" << t << ":\n";
		for(int i=0; i<R; i++)
			cout << g[i] << "\n";
	}
	return 0;
}
