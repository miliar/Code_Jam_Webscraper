//A
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
const double PI=(double)acos(-1);
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

int t,n,k;
pair<pll,pii>rett,dat[1005];
ll ret,res;

int main(){
	scanf("%d",&t);
	REP(tc,1,t){
		rett.ss.ss=ret=res=0;
		scanf("%d %d",&n,&k);
		REP(i,1,n){
			scanf("%d %d",&dat[i].ss.ss,&dat[i].ss.ff);
			dat[i].ff.ss=(ll)dat[i].ss.ss*(ll)dat[i].ss.ss; //area
			dat[i].ff.ff=2*(ll)dat[i].ss.ss*(ll)dat[i].ss.ff; //+(dat[i].ff.ss); //surface
			if(rett.ss.ss<dat[i].ss.ss)rett=dat[i]; //max radius
		}
		sort(dat+1,dat+1+n); reverse(dat+1,dat+1+n);
		REP(i,1,k-1){res+=dat[i].ff.ff; ret=max(ret,dat[i].ff.ss); if(dat[i]==rett)rett.ss.ss=-1;}
		if(rett.ss.ss>=0){
			//look at impact
			if(rett.ff.ff+max(rett.ff.ss,ret)>dat[k].ff.ff+max(dat[k].ff.ss,ret)){
				res+=rett.ff.ff; ret=max(ret,rett.ff.ss);
			}
			else rett.ss.ss=-1;
		}
		if(rett.ss.ss< 0){res+=dat[k].ff.ff; ret=max(ret,dat[k].ff.ss);}
		res+=ret;
		printf("Case #%d: %.6lf\n",tc,PI*(double)res);
	}
	return 0;
}
