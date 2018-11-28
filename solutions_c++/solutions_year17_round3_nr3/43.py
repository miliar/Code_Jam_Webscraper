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
	double u;cin>>u;
	vector<double> ps(n);
	REP(i,n)cin>>ps[i];
	if(n!=k)return;
	sort(ALL(ps));
	ps.PB(1);
	REP(i,n){
		double dif=ps[i+1]-ps[i];
		if(u<=dif*(i+1)){
			REP(j,i+1)ps[j]+=u/(i+1);
			break;
		}else{
			REP(j,i+1)ps[j]=ps[i+1];
			u-=dif*(i+1);
		}
	}
	double ans=1;
	REP(i,n)ans*=ps[i];
	cout<<fixed<<setprecision(20)<<ans<<endl;
}

signed main(){
	int t=read();
	REP(i,t){
		printf("Case #%lld: ",i+1);
		Solve();
	}
}
