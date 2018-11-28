#include <map>
#include <set>
#include <ctime>
#include <stack>
#include <cmath>
#include <queue>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <iostream>
#include <algorithm>
#pragma comment(linker, "/STACK:1024000000,1024000000")

using namespace std;
#define   maxn          100000+10
#define   maxm          10000+10
#define   lson          l,m,rt<<1
#define   rson          m+1,r,rt<<1|1
#define   clr(x,y)      memset(x,y,sizeof(x))
#define   pii           pair<int,int>
#define   mp            make_pair
#define   FI            first
#define   SE            second
#define   IT            iterator
#define   PB            push_back
#define   Times         10

typedef   long long     ll;
typedef   unsigned long long ull;
typedef   long double   ld;

const double eps   = 1e-14;
const double  pi   = acos(-1.0);
const  ll    mod   = 1e9+7;
const  int   inf   = 0x3f3f3f3f;
const  ll    INF   = (ll)1e18+300;
const double delta = 0.98;

inline void RI(int& x)
{
    x=0;
    char c=getchar();
    while(!((c>='0'&&c<='9')||c=='-'))c=getchar();
    bool flag=1;
    if(c=='-')
    {
        flag=0;
    }
    while(c<='9'&&c>='0')
    {
        x=x*10+c-'0';
        c=getchar();
    }
    if(!flag)x=-x;
}

/*--------------------------------------------------*/

int dat[5];
int main(){
    freopen("D:\\acm\\A-large.in","r",stdin);
    freopen("D:\\acm\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		int n,p;
		scanf("%d %d",&n,&p);
		int ans=0;
		clr(dat,0);
		if(p==2){
			for(int i=0;i<n;i++){
				int a;
				scanf("%d",&a);
				if(a%2)dat[1]++;
				else dat[0]++;
			}
			ans+=dat[0];
			ans+=(dat[1]%2)?(dat[1]/2+1):(dat[1]/2);
		}
		else if(p==3){
			for(int i=0;i<n;i++){
				int a;
				scanf("%d",&a);
				dat[a%3]++;
			}
			ans+=dat[0];
			ans+=min(dat[1],dat[2]);
			int k=min(dat[1],dat[2]);
			dat[1]-=k;dat[2]-=k;
			if(dat[1])ans+=(dat[1]%3)?(dat[1]/3+1):(dat[1]/3);
			if(dat[2])ans+=(dat[2]%3)?(dat[2]/3+1):(dat[2]/3);
		}
		else{
			for(int i=0;i<n;i++){
				int a;
				scanf("%d",&a);
				dat[a%4]++;
			}
			ans+=dat[0];
			int k=min(dat[1],dat[3]);
			ans+=k;
			dat[1]-=k;dat[3]-=k;
			k=dat[1]+dat[3];
			int s=min(k/2,dat[2]);
			ans+=s;
			k-=s*2;dat[2]-=s;
			s=dat[2]/2;
			ans+=s;
			dat[2]-=s*2;
			s=k/4;
			ans+=s;
			k-=4*s;
			if(k+dat[2]){
				ans++;
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
    return 0;
}







