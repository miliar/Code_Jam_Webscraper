#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;

using ll=long long;
#define int ll

#define FOR(i,a,b) for(int i=int(a);i<int(b);i++)
#define REP(i,b) FOR(i,0,b)
#define MP make_pair
#define PB push_back
#define ALL(x) x.begin(),x.end()
#define REACH cerr<<"reached line "<<__LINE__<<endl
#define DBG(x) cerr<<"line "<<__LINE__<<" "<<#x<<":"<<x<<endl

using pi=pair<int,int>;
using vi=vector<int>;
using ld=long double;

template<class T,class U>
ostream& operator<<(ostream& os,const pair<T,U>& p){
	os<<"("<<p.first<<","<<p.second<<")";
	return os;
}

template<class T>
ostream& operator <<(ostream& os,const vector<T>& v){
	os<<"[";
	REP(i,(int)v.size()){
		if(i)os<<",";
		os<<v[i];
	}
	os<<"]";
	return os;
}

int read(){
	int i;
	scanf("%lld",&i);
	return i;
}

void printSpace(){
	printf(" ");
}

void printEoln(){
	printf("\n");
}

void print(int x,int suc=1){
	printf("%lld",x);
	if(suc==1)
		printEoln();
	if(suc==2)
		printSpace();
}

string readString(){
	static char buf[3341919];
	scanf("%s",buf);
	return string(buf);
}

char* readCharArray(){
	static char buf[3341919];
	static int bufUsed=0;
	char* ret=buf+bufUsed;
	scanf("%s",ret);
	bufUsed+=strlen(ret)+1;
	return ret;
}

template<class T,class U>
void chmax(T& a,U b){
	if(a<b)
		a=b;
}

template<class T,class U>
void chmin(T& a,U b){
	if(a>b)
		a=b;
}

template<class T>
T Sq(const T& t){
	return t*t;
}

const int inf=LLONG_MAX/3;
int dp[2][721][2];
void Solve(){
	vi use(1440,3);
	int a=read(),b=read();
	REP(i,a){
		int c=read(),d=read();
		FOR(j,c,d)use[j]&=1;
	}
	REP(i,b){
		int c=read(),d=read();
		FOR(j,c,d)use[j]&=2;
	}
	int ans=inf;
	REP(t,2){
		int cur=0;
		REP(i,721)REP(j,2)dp[cur][i][j]=inf;
		dp[cur][0][t]=1;
		REP(i,1440){
			int nx=cur^1;
			REP(j,721)REP(k,2)dp[nx][j][k]=inf;
			if(use[i]&1){
				REP(j,720)chmin(dp[nx][j+1][0],dp[cur][j][0]);
				REP(j,720)chmin(dp[nx][j+1][0],dp[cur][j][1]+1);
			}
			if(use[i]&2){
				REP(j,721)chmin(dp[nx][j][1],dp[cur][j][0]+1);
				REP(j,721)chmin(dp[nx][j][1],dp[cur][j][1]);
			}
			cur^=1;
		}
		chmin(ans,dp[cur][720][t]-1);
		chmin(ans,dp[cur][720][t^1]);
	}
	assert(ans<inf);
	print(ans);
}

signed main(){
	int t=read();
	REP(i,t){
		printf("Case #%lld: ",i+1);
		Solve();
	}
}
