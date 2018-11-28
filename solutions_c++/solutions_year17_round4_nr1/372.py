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

const int Nmax=114;
int dp3[Nmax][Nmax];
int dp4[Nmax][Nmax][Nmax];

void Solve(){
	int n=read(),p=read();
	vi cnt(p,0);
	REP(i,n)cnt[read()%p]++;
	if(p==2){
		cout<<cnt[0]+(cnt[1]+1)/2<<endl;
	}else if(p==3){
		memset(dp3,0,sizeof(dp3));
		dp3[0][0]=cnt[0];
		REP(i,cnt[1]+1)REP(j,cnt[2]+1){
			if(i-1>=0)chmax(dp3[i][j],dp3[i-1][j]+!(((i-1)+j*2)%3));
			if(j-1>=0)chmax(dp3[i][j],dp3[i][j-1]+!((i+(j-1)*2)%3));
		}
		cout<<dp3[cnt[1]][cnt[2]]<<endl;
	}else{
		memset(dp4,0,sizeof(dp4));
		dp4[0][0][0]=cnt[0];
		REP(i,cnt[1]+1)REP(j,cnt[2]+1)REP(k,cnt[3]+1){
			if(i-1>=0)chmax(dp4[i][j][k],dp4[i-1][j][k]+!(((i-1)+j*2+k*3)%4));
			if(j-1>=0)chmax(dp4[i][j][k],dp4[i][j-1][k]+!((i+(j-1)*2+k*3)%4));
			if(k-1>=0)chmax(dp4[i][j][k],dp4[i][j][k-1]+!((i+j*2+(k-1)*3)%4));
		}
		cout<<dp4[cnt[1]][cnt[2]][cnt[3]]<<endl;
	}
}

signed main(){
	int t=read();
	REP(i,t){
		printf("Case #%lld: ",i+1);
		Solve();
	}
}
