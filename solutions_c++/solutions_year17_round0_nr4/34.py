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
	int n=read(),m=read();
	vi a(n,0),b(n,0),c(2*n-1,0),d(2*n-1,0);
	map<pi,int> ans,org;
	REP(i,m){
		string s=readString();
		int y=read()-1,x=read()-1;
		if(s=="+"||s=="o"){
			ans[pi(y,x)]|=1;
			org[pi(y,x)]|=1;
			c[x-y+n-1]=1;
			d[x+y]=1;
		}
		if(s=="x"||s=="o"){
			ans[pi(y,x)]|=2;
			org[pi(y,x)]|=2;
			a[x]=1;
			b[y]=1;
		}
	}
	REP(y,n)if(!b[y])
		REP(x,n)if(!a[x]){
			b[y]=1;
			a[x]=1;
			ans[pi(y,x)]|=2;
			break;
		}
	REP(k,n){
		int ss[2]{k,2*n-2-k};
		for(auto s:ss)if(!d[s]){
			int t=n-1-k;
			while(t<=n-1+k){
				if(!c[t]){
					d[s]=1;
					c[t]=1;
					t-=(n-1);
					ans[pi((s-t)/2,(s+t)/2)]|=1;
					break;
				}
				t+=2;
			}
		}
	}
	int po=0,ch=0;
	for(auto kv:ans){
		po+=__builtin_popcount(kv.second);
		ch+=(kv.second!=org[kv.first]);
	}
	print(po,2),print(ch);
	for(auto kv:ans)
		if(kv.second!=org[kv.first]){
			if(kv.second==1)printf("+ ");
			if(kv.second==2)printf("x ");
			if(kv.second==3)printf("o ");
			print(kv.first.first+1,2);
			print(kv.first.second+1);
		}
}

signed main(){
	int t=read();
	FOR(i,1,t+1){
		printf("Case #%lld: ",i);
		Solve();
	}
}
