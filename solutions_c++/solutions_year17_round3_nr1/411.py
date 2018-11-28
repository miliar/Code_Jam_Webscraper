#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<queue>
using namespace std;

const double pi = 3.1415926535897932;
const int N = 100050;
int n,k;

struct ck
{
	long long r,h;
	int id;
}	a[N],b[N];

bool cmp(ck a,ck b)
{
	if(a.r==b.r) return a.h>b.h;
	else return a.r>b.r;
}
bool cmp1(ck a,ck b)
{
	double x = 1.0*a.r*a.h;
	double y = 1.0*b.r*b.h;
	if(x==y) return a.r>b.r;
	return x>y;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-l.out","w",stdout);
	int TT;
	scanf("%d",&TT);
	
	for(int tt=1;tt<=TT;tt++)
	{
		cin>>n>>k;
		for(int i=1;i<=n;i++) 
		{	
			scanf("%lld %lld",&a[i].r,&a[i].h);a[i].id=i;
			b[i].r=a[i].r;b[i].h=a[i].h;b[i].id=i;
		}
		sort(a+1,a+1+n,cmp);
		sort(b+1,b+1+n,cmp1);
		//for(int i=1;i<=n;i++) cout<<b[i].r<<' ';
		long long ans=0.0;
		long long temp=0.0;
		int cnt=0;
		for(int j=1;j<=n;j++)
		{
			temp=0;
			cnt=0;
			temp+=a[j].r*a[j].r;
			temp+=2LL*a[j].r*a[j].h;
			for(int i=1;i<=n;i++) 
			{
				if(cnt==k-1) break;
				if(b[i].id==a[j].id) continue;
				if(b[i].r<=a[j].r) 
				{
					temp+=2.0*b[i].r*b[i].h;
					cnt++;
				}
				
			}
			//cout<<temp<<' ';
			ans = max(ans,temp);
			
		}
		printf("Case #%d: %.12lf\n",tt,1.0*pi*ans);
	}

	return 0;
}
