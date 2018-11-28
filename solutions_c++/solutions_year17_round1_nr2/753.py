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
typedef priority_queue<ut,VI,greater<ut> > PQ;
const int SIZE=105;
const int MAX=1e6+5;
const int INF=1145141919;
const double EPS=1e-9;
int R[SIZE];
int Q[SIZE][SIZE];
Vpr packs[MAX];
void measure(int a,int b){
	int minim,maxim;
	int s=1,e=MAX;
	while(s<=e){
		int f=(s+e)/2;
		if((double)(f*0.9*R[a]-EPS)<=(double)(Q[a][b])){
			s=f+1;
		}
		else
			e=f-1;
	}
	minim=e;
	s=1;e=MAX;
	while(s<=e){
		int f=(s+e)/2;
		if((double)(f*1.1*R[a])+EPS>=(double)(Q[a][b])){
			e=f-1;
		}
		else
			s=f+1;
	}
	maxim=s;
	if(minim>=maxim){
		packs[maxim].PB(pr(a,minim));
	}

}
void solve(){
	int N,M;
	REP(i,MAX) packs[i].clear();
	REP(i,SIZE) REP(j,SIZE) Q[i][j]=0;
	REP(i,SIZE) R[i]=0;
	cin >>N >> M;
	REP(i,N) cin >> R[i];
	REP(i,N){
		REP(j,M){
			cin >> Q[i][j];
			measure(i,j);
		}
	}
	int ans=0;
	PQ qu[100];
	FOR(i,1,MAX){
		REP(j,packs[i].size()) qu[packs[i][j].first].push(packs[i][j].second);
		bool sellout=false;
		while(true){
			REP(j,N)
				if(qu[j].empty()) sellout=true;
			if(sellout) break;
			REP(j,N) qu[j].pop();
			ans++;
		}
		REP(j,N) while(!qu[j].empty() && qu[j].top()<=i) qu[j].pop();
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