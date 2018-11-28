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
void solve2(LL N,LL K){
	N--;
	K--;
	if(K==0){
		cout << N/2+N%2 <<" "<< N/2 << endl;
	}
	else if(K%2) solve2(N/2+N%2,K/2+1);
	else solve2(N/2,K/2);
}
void solve(){
	LL N,K;
	cin >> N >> K;
	solve2(N,K);

}
int main(){
	int T;
	cin >> T;
	REP(i,T){
		cout << "Case #"<<i+1 <<": ";
		solve();
	}
	return 0;
}