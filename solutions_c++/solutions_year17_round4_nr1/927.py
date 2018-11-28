#include <stdio.h>
void solve();
int main()
{
	freopen("largeA4.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
int x[110];
void solve()
{
	int a,b;
	scanf("%d%d",&a,&b);
	for(int i=1;i<=a;i++) scanf("%d",&x[i]);
	if(b==2)
	{
		int count = 0;
		for(int i=1;i<=a;i++) if(x[i]%2==0) count++;
		printf("%d\n",count+(a-count+1)/2);
		return;
	}
	if(b==3)
	{
		int count1 = 0, count2 = 0, count3 = 0;
		for(int i=1;i<=a;i++)
		{
			if(x[i]%3==0) count3++;
			if(x[i]%3==1) count1++;
			if(x[i]%3==2) count2++;
		}
		if(count1>count2) printf("%d\n",count3+count2+(count1-count2+2)/3);
		else printf("%d\n",count3+count1+(count2-count1+2)/3);
	}
	if(b==4)
	{
		int count1 = 0, count2 = 0, count3 = 0, count4 = 0;
		for(int i=1;i<=a;i++)
		{
			if(x[i]%4==0) count4++;
			if(x[i]%4==1) count1++;
			if(x[i]%4==2) count2++;
			if(x[i]%4==3) count3++;
		}
		if(count1>count3) count4+=count3, count1-=count3, count3 = 0;
		else count4+=count1, count3-=count1, count1 = 0;
		count4+=(count2/2), count2%=2;
		if(count1>0)
		{
			if(count2==0) printf("%d\n",count4+(count1+3)/4);
			else printf("%d\n",count4+(count1+5)/4);
		}
		else if(count3>0)
		{
			if(count2==0) printf("%d\n",count4+(count3+3)/4);
			else printf("%d\n",count4+(count3+5)/4);
		}
		else printf("%d\n",count4+count2);
	}
}
