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
LL N,P;
VI edges[SIZE];
LL A[SIZE];
LL mods[5];
void solve(){
	cin >> N >> P;
	REP(i,5) mods[i]=0;
	REP(i,N){
	 cin >> A[i];
	 mods[A[i]%P]++;
	}

	LL ans=0; 
	ans+=mods[0];
	if(P==2){
		ans+=(mods[1]+1)/2;
	}
	else if(P==3){
		LL c=min(mods[2],mods[1]);
		ans+=c;
		LL rest=max(mods[2],mods[1])-c;
		ans+=(rest+2)/3;
	}
	else{
		ans+=(mods[2])/2;
		LL c=min(mods[3],mods[1]);
		ans+=c;
		LL rest=max(mods[3],mods[1])-c;
		ans+=rest/4;
		if(rest%4 or mods[2]%2)
			ans++;
	}
	cout << ans << endl;
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