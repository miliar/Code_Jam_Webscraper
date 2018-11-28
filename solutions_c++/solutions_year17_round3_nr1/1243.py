#include <iostream>
#include <queue>
#include <math.h>
#include <string.h>
using namespace std;
typedef long long LL;
const int N = 10005;
const LL INF = 0x3f3f3f3f;
const double Pi = acos(-1);

#define BUG

int n,m,k;
double a,b,x;
struct pancake
{
	double r,h;
	int id;
}s[N];
int vis[N];

void INIF()
{
#ifdef BUG
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
#endif
}

int cmp(pancake a,pancake b)
{
	return a.r*a.h > b.r*b.h;
}

void ini()
{
	memset(vis,0,sizeof(vis));
	memset(s,0,sizeof(s));
}


int main()
{

	INIF();
	int kk;
	scanf("%d",&kk);
	for (int cc=1;cc<=kk;cc++)
	{
		ini();
		scanf("%d%d",&n,&k);
		double ma=0;
		int p=0;
		for (int i=0;i<n;i++)
		{
			scanf("%lf%lf",&s[i].r,&s[i].h);
			s[i].id=i;
		}
		sort(s,s+n,cmp);
		int cnt=1;
		double ans=0;
		double res=0;
		for (p=0;p<n;p++)
		{
			vis[p]=1;
			double rid=s[p].r;
			ans=s[p].r*s[p].r*Pi+s[p].r*s[p].h*2*Pi;
			cnt=1;
			for (int i=0;i<n;i++)
			{
				if (cnt==k)
					break;
				if (vis[i])
					continue;
				if (s[i].r>rid)
					continue;
				cnt++;
				ans+=s[i].r*s[i].h*2*Pi;
			}
			res=max(res,ans);
			vis[p]=0;
		}
		printf("Case #%d: %.9f\n",cc, res);
	}
	return 0;
}
/*

4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4

*/
