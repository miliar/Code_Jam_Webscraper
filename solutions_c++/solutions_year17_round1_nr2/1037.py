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

void Muri(){
	printf("IMPOSSIBLE\n");
}

void Solve(){
	int n=read(),p=read();
	vi need(n);REP(i,n)need[i]=read();
	map<int,vector<pi>> qs;
	REP(i,n)REP(j,p){
		int x=read(),b,e;
		{
			int l=0,r=1141919;
			while(r-l>1){
				int m=(l+r)/2;
				if(need[i]*m*11<x*10)l=m;
				else r=m;
			}
			b=r;
		}
		{
			int l=0,r=1141919;
			while(r-l>1){
				int m=(l+r)/2;
				if(need[i]*m*9<=x*10)l=m;
				else r=m;
			}
			e=r;
		}
		qs[b].PB(pi(i,e));
	}
	int ans=0;
	vector<queue<int>> es(n);
	for(auto kv:qs){
		for(auto v:kv.second)es[v.first].push(v.second);
		bool use=true;
		while(use){
			REP(i,n){
				while(!es[i].empty()&&es[i].front()<=kv.first)es[i].pop();
				if(es[i].empty())use=false;
			}
			if(use){
				REP(i,n)es[i].pop();
				ans++;
			}
		}
	}
	cout<<ans<<endl;
}

signed main(){
	int t=read();
	FOR(i,1,t+1){
		printf("Case #%lld: ",i);
		Solve();
	}
}
