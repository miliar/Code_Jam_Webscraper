#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

const int maxn=105;

int n,p;

int f2[maxn],f3[maxn][maxn],f4[maxn][maxn][maxn];
void Pre(int n)
{
	fo(i,0,n)
	{
		if (i%2==0) f2[i]++;
		f2[i+1]=max(f2[i+1],f2[i]);
	}
	fo(i,0,n) if (i%2==0) f2[i]--;
	
	fo(i,0,n)
		fo(j,0,n)
		{
			if ((i+j*2)%3==0) f3[i][j]++;
			f3[i+1][j]=max(f3[i+1][j],f3[i][j]);
			f3[i][j+1]=max(f3[i][j+1],f3[i][j]);
		}
	fo(i,0,n)
		fo(j,0,n) if ((i+j*2)%3==0) f3[i][j]--;
	
	fo(i,0,n)
		fo(j,0,n)
			fo(k,0,n)
			{
				if ((i+j*2+k*3)%4==0) f4[i][j][k]++;
				f4[i+1][j][k]=max(f4[i+1][j][k],f4[i][j][k]);
				f4[i][j+1][k]=max(f4[i][j+1][k],f4[i][j][k]);
				f4[i][j][k+1]=max(f4[i][j][k+1],f4[i][j][k]);
			}
	fo(i,0,n)
		fo(j,0,n)
			fo(k,0,n) if ((i+j*2+k*3)%4==0) f4[i][j][k]--;
}

int T,a[100];
int main()
{
	//freopen("A.in","r",stdin);	
	//freopen("A.out","w",stdout);
	
	Pre(100);
	
	scanf("%d",&T);
	fo(Ti,1,T)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%d %d",&n,&p);
		memset(a,0,sizeof(a));
		fo(i,1,n)
		{
			int x;
			scanf("%d",&x);
			a[x%p]++;
		}
		
		if (p==2) printf("%d\n",f2[a[1]]+a[0]);
			else if (p==3) printf("%d\n",f3[a[1]][a[2]]+a[0]);
				else printf("%d\n",f4[a[1]][a[2]][a[3]]+a[0]);
	}
}