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
const int SIZE=1005;
const LL p=7+1e9;
const LL INF=1<<30;
const LL INFLL=1LL<<30;
inline void IN(ut &x){cin >> x;}
inline void INA(ut n,ut x[]){REP(i,n) cin >> x[i];}
inline void INE(ut m,VI edges[]){
	ut a,b;
	REP(i,m){
		cin >> a >> b;
		edges[a].PB(b);
		edges[b].PB(a);
	}
}
inline void INEC(ut m,Vpr edges[]){
	ut a,b,c;
	REP(i,m){
		cin >> a >> b >> c;
		edges[a].PB(pr(c,b));
		edges[b].PB(pr(c,a));
	}
}
LL N,M,C;
VI edges[SIZE];
VI tickets[SIZE];
LL A[SIZE];
LL riders[SIZE];
LL sum[SIZE];
void solve(){
	LL P,B;
	cin >> N >> C >> M;
	LL maxim=(M+N-1)/N;
	LL needs=0;
	REP(i,SIZE){
		sum[i]=riders[i]=A[i]=0;
		tickets[i].clear();
	}
	REP(i,M){
		cin >> P >> B;
		tickets[B].PB(P);
		riders[P]++;
	}
	FOR(i,1,C+1){
		maxim=max(maxim,(LL)tickets[i].size());
	}
	FOR(i,1,N+1){
		sum[i]=sum[i-1]+riders[i];
		maxim=max(maxim,(sum[i]+i-1)/i);
	}
	FOR(i,1,N+1){
		needs+=max(0LL,riders[i]-maxim);
	}
	cout << maxim <<" " << needs<< endl;

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