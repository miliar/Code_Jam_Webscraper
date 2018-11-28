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

int t,n,k,res;
char s[1005];

int main(){
	scanf("%d",&t);
	REP(tc,1,t){
		res=0;
		scanf("%s %d",s,&k);
		n=strlen(s);
		REP(i,0,n-k) if(s[i]=='-'){
			REP(j,0,k-1)s[i+j]=(s[i+j]=='-')?'+':'-';
			res++;
		}
		REP(i,n-k,n-1) if(s[i]=='-')res=-1;
		if(res==-1)printf("Case #%d: IMPOSSIBLE\n",tc,res);
		else printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}
