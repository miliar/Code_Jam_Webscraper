#include<cstdio>
//const int MAXN=1000+5;
int n,t/*,bits[MAXN]*/;
bool IsTidy(int x)
{
	int last=10;
	//printf("x=%d:\n",x);
	while(x!=0)
	{
		//printf("%d %d\n",x%10,last);
		if(x%10>last) return 0;
		last=x%10;
		x/=10;
	}
	return 1;
}
int main()
{
	freopen("o.txt","w",stdout);
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%d",&n);
		for(int i=n;i>=1;i--)
			if(IsTidy(i))
			{
				printf("Case #%d: %d\n",k,i);
				break;
			}
	}
	return 0;
}
