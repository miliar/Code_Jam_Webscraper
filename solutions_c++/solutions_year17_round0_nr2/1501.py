#include<cstdio>
#include<cstring>

int t;
long long n;
int a[20];
int b[20];
int d;

bool solve(int prev,int p)
{
	if(p==d) return true;

	if(a[p]<prev)
	{
		for(int i=p;i<d;i++) b[i]=9;
		return false;
	}

	if(solve(a[p],p+1))
	{
		b[p]=a[p];
		return true;
	}

	b[p]=a[p]-1;
	if(b[p]<prev)
	{
		b[p]=9;
		return false;
	}
	else return true;
}

int main()
{
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);

	scanf("%d",&t);
	for(int test_case=1;test_case<=t;test_case++)
	{
		memset(a,0,20);
		memset(b,0,20);
		d=0;

		scanf("%lld",&n);
		for(long long t=n;t>0;t/=10) a[d++]=t%10;
		for(int i=0;2*i<d;i++) if(a[i]!=a[d-1-i]) a[i]^=a[d-1-i]^=a[i]^=a[d-1-i];

		solve(0,0);

		printf("Case #%d: ",test_case);
		for(int i=(b[0]==0);i<d;i++) printf("%d",b[i]);
		printf("\n");
	}
	return 0;
}
