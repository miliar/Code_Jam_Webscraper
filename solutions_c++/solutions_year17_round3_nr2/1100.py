//B
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<ctime>
#include<cassert>
#include<algorithm>
#include<cmath>

#include<cstring>
#include<string>
#include<cctype>
#include<utility>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<list>

typedef long long ll;
typedef std::pair<int,int> pii;
typedef std::pair<ll,ll> pll;
typedef std::vector<int> vi;

const int OO=(int)2e9;
const ll INF=(ll)4e18;
const double EPS=(double)1e-12;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front

#define INL(i,a,b) ((a<=i)&&(i<=b))
#define EXL(i,a,b) ((a< i)&&(i< b))
#define REPP(i,a,b,c) for(int i=a;i<=b;i+=c)
#define REP(i,a,b) REPP(i,a,b,1)
#define REVV(i,a,b,c) for(int i=a;i>=b;i-=c)
#define REV(i,a,b) REVV(i,a,b,1)
using namespace std;

int t,n,nc,nj,res;
pair<pii,int> dat[505];
int ret[5];

inline int diff(int a,int b){return b-a+(b>=a?0:24*60);}
inline void actions(int x){
	//check all before dat, assign all after (if its true)
	REP(i,1,n-1) if(dat[i].ss==-1){
		if(dat[i+1].ss==x&&dat[i-1].ss!=x){ret[x^1]-=diff(dat[i].ff.ff,dat[i].ff.ss); ret[x]+=diff(dat[i].ff.ff,dat[i].ff.ss); dat[i].ss==x;}
		if(dat[i-1].ss==x)dat[i].ss==x;
		if(ret[x]>=ret[x^1])return;
	}
	if(dat[0+1].ss==x&&dat[n-1].ss!=x){ret[x^1]-=diff(dat[n].ff.ff,dat[n].ff.ss); ret[x]+=diff(dat[n].ff.ff,dat[n].ff.ss); dat[n].ss==x;}
	if(dat[n-1].ss==x)dat[n].ss==x;
	if(ret[x]>=ret[x^1])return;
	//more actions needed, check all hamburger position (greedy)
	pii temp[505]; int p=0;
	REP(i,1,n) if(dat[i].ss==-1)temp[++p]=mp(diff(dat[i].ff.ff,dat[i].ff.ss),i);
	sort(temp+1,temp+1+p);
	while(p--){
		ret[x^1]-=diff(dat[temp[p+1].ss].ff.ff,dat[temp[p+1].ss].ff.ss); ret[x]+=diff(dat[temp[p+1].ss].ff.ff,dat[temp[p+1].ss].ff.ss);
		dat[temp[p+1].ss].ss=x;
		if(ret[x]>=ret[x^1])return;
	}
}

int main(){
	scanf("%d",&t);
	REP(tc,1,t){
		REP(i,0,505)dat[i]=mp(mp(0,0),-1);
		REP(i,0,3)ret[i]=0;
		res=0;
		scanf("%d %d",&nc,&nj); n=nc+nj;
		REP(i,   1,nc){scanf("%d %d",&dat[i].ff.ff,&dat[i].ff.ss); dat[i].ss=1;} //switch because 1 will take care
		REP(i,nc+1, n){scanf("%d %d",&dat[i].ff.ff,&dat[i].ff.ss); dat[i].ss=0;} //switch because 0 will take care
		//solution
		sort(dat+1,dat+1+n);
		REP(i,1,nc+nj){
			if(i==nc+nj){if(dat[i].ff.ss!=dat[1].ff.ff)dat[++n]=mp(mp(dat[i].ff.ss,dat[1].ff.ff),-1);}
			else{if(dat[i].ff.ss!=dat[i+1].ff.ff)dat[++n]=mp(mp(dat[i].ff.ss,dat[i+1].ff.ff),-1);}
		}
		sort(dat+1,dat+1+n);
		REP(i,1,n){
			if(dat[i].ss==0||(dat[i].ss==-1&&dat[i-1].ss==0))ret[0]+=diff(dat[i].ff.ff,dat[i].ff.ss);
			if(dat[i].ss==1||(dat[i].ss==-1&&dat[i-1].ss==1))ret[1]+=diff(dat[i].ff.ff,dat[i].ff.ss);
		}
		//check
		if(ret[0]!=ret[1]){
			if(ret[0]<ret[1])actions(0);
			else actions(1);
		}
		//assign all
		REP(i,2,n)if(dat[i].ss==-1)dat[i].ss=dat[i-1].ss;
		dat[n+1].ss=dat[1].ss;
		REP(i,1,n)if(dat[i].ss!=dat[i+1].ss)res++;
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}
