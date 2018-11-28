#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define fo(i,s,t) for(int i = s; i <= t; ++ i)
#define fd(i,s,t) for(int i = s; i >= t; -- i)

const int maxn = 1005;
const double pi = acos(-1.0);

int T, n, k, top;
struct node{long long h, r;}g[maxn], c[maxn];
double ans;

bool cmp(node a, node b){return a.r < b.r;}
bool cmp2(node a, node b){return a.r*a.h > b.r*b.h;}

void init()
{
	scanf("%d%d",&n,&k);
	fo(i,1,n) scanf("%lld%lld",&g[i].r,&g[i].h);
	sort(g+1,g+n+1,cmp);
}

void work()
{
	ans = 0;
	double cur;
	fo(i,k,n)
	{
		top = 0; cur = pi*g[i].r*g[i].r+2.0*pi*g[i].r*g[i].h;
		fo(j,1,i-1) c[++top] = g[j];
		sort(c+1,c+top+1,cmp2); 
		fo(j,1,k-1) cur += 2.0*pi*c[j].r*c[j].h;
		ans = max(ans, cur);
	}
	printf("%.9lf\n",ans);
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	fo(i,1,T)
	{
		init();
		printf("Case #%d: ",i);
		work();
	}
	return 0;
}
