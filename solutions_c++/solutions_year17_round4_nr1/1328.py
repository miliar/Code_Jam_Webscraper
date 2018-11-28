#include<cstdio>
#include<cstring>
#include<algorithm>

int T;
int n,p;
int g;
int a[5];
int dp1[110][110][4];
int dp2[110][110][110][5];
int A;

int solve1(int x,int y,int r)
{
	if(x==0&&y==0) return 0;

	if(dp1[x][y][r]==-1)
	{
		int A=0,B=0;
		if(x>0) A=solve1(x-1,y,(r+1)%3);
		if(y>0) B=solve1(x,y-1,(r+2)%3);
		dp1[x][y][r]=std::max(A,B)+(r%3==0);
	}
	return dp1[x][y][r];
}

int solve2(int x,int y,int z,int r)
{
	if(x==0&&y==0&&z==0) return 0;

	if(dp2[x][y][z][r]==-1)
	{
		int A=0,B=0,C=0;
		if(x>0) A=solve2(x-1,y,z,(r+1)%4);
		if(y>0) B=solve2(x,y-1,z,(r+2)%4);
		if(z>0) C=solve2(x,y,z-1,(r+3)%4);
		dp2[x][y][z][r]=std::max(A,std::max(B,C))+(r%4==0);
	}
	return dp2[x][y][z][r];
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&p);
		for(int k=0;k<p;k++) a[k]=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&g);
			a[g%p]++;
		}
		if(p==2)
		{
			A=a[0]+(a[1]+1)/2;
		}
		else if(p==3)
		{
			memset(dp1,-1,sizeof(dp1));
			A=a[0]+solve1(a[1],a[2],0);
		}
		else if(p==4)
		{
			memset(dp2,-1,sizeof(dp2));
			A=a[0];
			A=a[0]+solve2(a[1],a[2],a[3],0);
		}
		else printf("Case #%d: Input Error\n",t);

		printf("Case #%d: %d\n",t,A);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
