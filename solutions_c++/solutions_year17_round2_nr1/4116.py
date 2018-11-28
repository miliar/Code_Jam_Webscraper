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

int t,d,n;
pii dat[1005];
double in[1005];
double res,ret;

int main(){
	scanf("%d",&t);
	REP(tc,1,t){
		REP(i,0,1003){dat[i]=mp(0,0); in[i]=0.0;}
		scanf("%d %d",&d,&n);
		REP(i,1,n)scanf("%d %d",&dat[i].ff,&dat[i].ss);
		sort(dat+1,dat+1+n);
		ret=res=0.0;
		REV(i,n,1){
			ret=(double)(d-dat[i].ff)/(double)dat[i].ss;
			if(ret>res)res=ret;
			else{
				//find intersection
				in[i]=(double)dat[i+1].ff + (double)(dat[i+1].ff-dat[i].ff)*(double)dat[i+1].ss/(double)(dat[i].ss-dat[i+1].ss);
				res=(in[i]-(double)dat[i].ff)/(double)dat[i].ss + res - (in[i]-(double)dat[i+1].ff)/(double)dat[i+1].ss;
			}
		}
		res=(double)d/res;
		printf("Case #%d: %.6lf\n",tc,res);
	}
	return 0;
}
