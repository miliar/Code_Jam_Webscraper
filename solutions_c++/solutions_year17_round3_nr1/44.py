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

void Solve(){
	int n=read(),k=read();
	vector<pi> rh;
	REP(i,n){
		int r=read(),h=read();
		rh.PB(pi(r,h));
	}
	sort(ALL(rh));
	int ans=0;
	FOR(i,k-1,n){
		sort(rh.begin(),rh.begin()+i,[](pi a,pi b){
			return a.first*a.second>b.first*b.second;
		});
		int w=Sq(rh[i].first)+rh[i].first*rh[i].second*2;
		REP(j,k-1)w+=rh[j].first*rh[j].second*2;
		chmax(ans,w);
	}
	printf("%.20lf\n",M_PI*ans);
}

signed main(){
	int t=read();
	REP(i,t){
		printf("Case #%lld: ",i+1);
		Solve();
	}
}
