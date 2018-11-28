#include <stdio.h>
void solve();
int main()
{
	freopen("largeB1.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
long long int func(int s, int t)
{
	long long int k = 1;
	for(int i=1;i<=t;i++) k*=10;
	k--;
	k/=9;
	return s*k;
}
long long int get(long long int a, int k)
{
	long long int s = 1;
	for(int i=1;i<k;i++) s*=10;
	return (a/s)%10;
}
int ans[20];
void solve()
{
	long long int a;
	int b;
	scanf("%lld",&a);
	for(int i=1;i<=18;i++)
	{
		if(func(1,i)>a)
		{
			b = i-1;
			goto v;
		}
	}
	b = 18;
	v:;
	if(func(9,b)<=a)
	{
		printf("%lld\n",func(9,b));
		return;
	}
	ans[b+1] = 0;
	ans[b] = get(a,b);
	for(int i=b-1;i>=1;i--)
	{
		ans[i] = get(a,i);
		if(ans[i]<ans[i+1])
		{
			while(ans[i]<ans[i+1]) ans[i+1]--,i++;
			for(int j=1;j<i;j++) ans[j] = 9;
			goto u;
		}
	}
	u:;
	for(int j=b;j>=1;j--) printf("%d",ans[j]);
	printf("\n");
	return;
}
