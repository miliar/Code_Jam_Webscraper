#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
const int N=110;
int dp[N][N][N];
int n,p,a[10];
int fx[100][5],top;
int get(int x,int y,int z)
{
	int b[4];
	b[1]=x; b[2]=y; b[3]=z;
	if (x<0 || y<0 || z<0) return -10000000;
	if (dp[x][y][z]!=-1) return dp[x][y][z];
	int re=0;
	fo(i,1,top)
		{
			fo(j,1,3) b[j]-=fx[i][j];
			re=max(re,get(b[1],b[2],b[3])+1);
			fo(j,1,3) b[j]+=fx[i][j];
		} 		
	return dp[x][y][z]=re;
}
int work()
{
	top=0;
	fo(i,0,4)
		fo(j,0,4)
			fo(k,0,4)
			if ((i+j*2+k*3)%p==0 && i+j+k)
			{
				fx[++top][1]=i;
				fx[top][2]=j;
				fx[top][3]=k;
			}
	memset(dp,-1,sizeof dp);
	return get(a[1],a[2],a[3])+a[0];
}
int main()
{
	freopen("a.in","r",stdin);freopen("a.out","w",stdout);
	int cs=0;
	int T;
	scanf("%d",&T);
	while (T--)
	{
		memset(a,0,sizeof a);
		scanf("%d%d",&n,&p);
		fo(i,1,n)
		{
			int x;
			scanf("%d",&x);
			x%=p;
			a[x]++;
		}
		int ans=0;
		fo(i,0,p-1)
		if (a[i]) a[i]--,ans=max(work(),ans),a[i]++;
		printf("Case #%d: %d\n",++cs,ans+1);
	}
} 
