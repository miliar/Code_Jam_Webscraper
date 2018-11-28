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

int num[1010];int cnt[1010];
int p[1010];int b[1010];
int main(){
    freopen("D:\\acm\\B-large.in","r",stdin);
    freopen("D:\\acm\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		clr(num,0);clr(cnt,0);
		int n,c,m;
		scanf("%d %d %d",&n,&c,&m);
		for(int i=1;i<=m;i++){
			scanf("%d %d",&p[i],&b[i]);
			cnt[b[i]]++;
			num[p[i]]++;
		}
		int ans=0;
		int pro=0;
		for(int i=1;i<=c;i++){
			ans=max(ans,cnt[i]);
		}
		//cout<<ans<<endl;
		int k=0;
		for(int i=1;i<=n;i++){
			k=k+num[i];
			ans=max(ans,(k+i-1)/i);
		}
		for(int i=1;i<=n;i++){
			pro=pro+max(0,num[i]-ans);
		}
		printf("Case #%d: %d %d\n",cas,ans,pro);
	}
    return 0;
}







