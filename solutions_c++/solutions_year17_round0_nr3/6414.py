#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
typedef long long ll;
struct node{
	ll x,y;
};
bool cmp(const node a,const node b)
{
	return a.x>b.x;
}
node a[1000];
ll top;
void add(ll x,ll y)
{
	fo(i,1,top)
	if (a[i].x==x)
	{
		a[i].y+=y;
		return;
	}
	a[++top].x=x;
	a[top].y=y;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	ll n,k;
	int p=0;
	while (T--)
	{
		scanf("%lld%lld",&n,&k);
		k--;
		printf("Case #%d: ",++p);
		if (n==k)
		{
			printf("0 0\n");
			continue;
		}
		a[1].x=n;
		a[1].y=1;
		top=1;
		while (1)
		{
			sort(a+1,a+1+top,cmp);
			ll x=a[1].x,y=a[1].y;
			if (y>k) 
			{
				printf("%lld %lld\n",x/2,(x-1)/2);
				break;
			}
			k-=y;
			add((x-1)/2,y);
			add(x-1-(x-1)/2,y);
			a[1].x=a[1].y=0;
		}
	}
}
