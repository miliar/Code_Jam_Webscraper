#include <stdio.h>
#include <queue>
#include <vector>
void solve();
int main()
{
	freopen("largeB3.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
std::priority_queue<int, std::vector<int> , std::greater<int> > Q1;
std::priority_queue<int, std::vector<int> , std::greater<int> > Q2;
int x[3010];
int ans = 0;
int func(int k)
{
	for(int i=k;;i++)
	{
		if(x[i]==0&&x[i+1]!=0)
		{
			if(x[k-1]==x[i+1])
			{
				if(x[k-1]==1) Q1.push(i-k+1);
				else Q2.push(i-k+1);
			}
			return i;
		}
	}
}
void solve()
{
	ans = 0;
	while(!Q1.empty()) Q1.pop();
	while(!Q2.empty()) Q2.pop();
	int a,b,c,d;
	scanf("%d%d",&a,&b);
	for(int i=0;i<1440;i++) x[i] = 0;
	for(int i=1;i<=a;i++)
	{
		scanf("%d%d",&c,&d);
		for(int j=c;j<d;j++) x[j] = 2;
	}
	for(int i=1;i<=b;i++)
	{
		scanf("%d%d",&c,&d);
		for(int j=c;j<d;j++) x[j] = 1;
	}
	for(int i=1440;i<2880;i++) x[i] = x[i-1440];
	
	int i;
	for(i=1;i<=1440;i++) if(x[i]==0&&x[i-1]!=0) break;
	for(int j=i;j<i+1440;j++)
	{
		if(x[j]==0&&x[j-1]!=0) ans++,j = func(j);
		if(x[j]+x[j-1]==3) ans++;
	}
	int s1 = 0, s2 = 0;
	for(int i=1;i<=1440;i++)
	{
		if(x[i]==1) s1++;
		if(x[i]==2) s2++;
	}
	while(!Q1.empty()&&s1+Q1.top()<=720) ans--,s1+=Q1.top(),Q1.pop();
	while(!Q2.empty()&&s2+Q2.top()<=720) ans--,s2+=Q2.top(),Q2.pop();
	printf("%d\n",ans+Q1.size()+Q2.size());
}
