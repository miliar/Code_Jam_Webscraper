#include <bits/stdc++.h>
#define FOR(i,a,b) for(ut i=(a);i<(ut)(b);i++)
#define REP(i,b) FOR(i,0,b)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define cat //cout << __LINE__ << endl;
using namespace std;
typedef long long LL;
typedef double ld;
typedef LL ut;
typedef vector<ut> VI;
typedef pair<ut,ut> pr;
typedef vector<pr> Vpr;
typedef pair<ut,ut> prs;
const int SIZE=5+5*1e5;
int maps[100][100];


void solve(){
	int N,M;
	cout << endl;
	cin >> N >> M ;
	REP(i,N){
		string s;
		cin >> s;
		REP(j,M){
			if(s[j]=='?') {
				maps[i][j]=0;
				if(j) maps[i][j]=maps[i][j-1];
			}
			else maps[i][j]=s[j]-'A'+1;
		}
		REP(j,M){
			int k=M-j-1;
			if(maps[i][k]==0 && j) maps[i][k]=maps[i][k+1];
		}
		if(maps[i][0]==0){
			if(i) REP(j,M) maps[i][j]=maps[i-1][j];
		}
	}
	REP(i,N){
		int k=N-i-1;
		if(maps[k][0]==0){
			if(i) REP(j,M) maps[k][j]=maps[k+1][j];
		}
	}
	REP(i,N){

		REP(j,M){
			cout << (char)(maps[i][j]-1+'A');
		}
		cout << endl;
	}

}
int main(){
	int T;
	cin >> T;
	REP(i,T){
		cout << "Case #"<<i+1 <<":";
		solve();
	}
	return 0;
}