#include<bits/stdc++.h>
#define X first
#define Y second
using namespace std;
pair<int,int> a[4];
int num[1005];
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("output_B-small-attempt1.txt","w",stdout);
	int r,o,y,g,v,b,i,t,n,ct=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		n-=2*o+2*g+2*v;
		if(n==0&&r+y==0)
		{
			printf("Case #%d: ",ct++);
			while(o--) printf("BO");
			printf("\n");
			continue;
		}
		if(n==0&&b+y==0)
		{
			printf("Case #%d: ",ct++);
			while(g--) printf("RG");
			printf("\n");
			continue;
		}
		if(n==0&&r+b==0)
		{
			printf("Case #%d: ",ct++);
			while(v--) printf("YV");
			printf("\n");
			continue;
		}
		b-=o;
		r-=g;
		y-=v;
		if(b<0||r<0||y<0||n<=0)
		{
			printf("Case #%d: IMPOSSIBLE\n",ct++);
			continue;
		}
		a[0]={b,0};
		a[1]={r,1};
		a[2]={y,2};
		sort(a,a+3);
		memset(num,-1,sizeof num);
		for(i=0;i<n-1&&a[0].X>0;i+=2,a[0].X--)
			num[i]=0;
		if(a[0].X>0)
		{
			printf("Case #%d: IMPOSSIBLE\n",ct++);
			continue;
		}
		if(i>=n) i=1;
		for(;i<n&&a[1].X>0;i+=2,a[1].X--)
		{
			num[i]=1;
			if(i+2>=n) i=-1;
		}
		for(i=0;i<n;i++)
		{
			if(num[i]==-1)
				num[i]=2;
		}
		for(i=0;i<n;i++)
			if(num[i]==num[(i+1)%n]||num[i]==num[(i+n-1)%n])
				break;
		if(i<n)
		{
			printf("Case #%d: IMPOSSIBLE\n",ct++);
			continue;
		}
		printf("Case #%d: ",ct++);
		for(i=0;i<n;i++)
		{
			if(a[num[i]].Y==0) 
			{
				printf("B");
				while(o>0) printf("OB"),o--;
			}
			else if(a[num[i]].Y==1)
			{
				printf("R");
				while(g>0) printf("GR"),g--;
			}
			else if(a[num[i]].Y==2)
			{
				printf("Y");
				while(v>0) printf("VY"),v--;
			}
		}
		printf("\n");
	}

}