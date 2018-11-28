#include<cstdio>
#include<algorithm>
#include<cstring>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
int a[4][10],ans[1100];
int main()
{
	freopen("b.in","r",stdin);freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	int c=0;
	while (T--)
	{
		int N, R, O, Y, G, B, V;
		scanf("%d%d%d%d%d%d%d",&N, &R, &O, &Y, &G, &B, &V);
		printf("Case #%d: ",++c);
		int b=O,r=G,y=V;
		a[1][1]=R;
		a[1][2]=r;
		a[1][3]='R';
		a[1][4]='G';
		a[2][1]=B;
		a[2][2]=b;
		a[2][3]='B';
		a[2][4]='O';
		a[3][1]=Y;
		a[3][2]=y;
		a[3][3]='Y';
		a[3][4]='V';
		fo(i,1,3)
			fo(j,i+1,3)
			if (a[i][1]<a[j][1]) swap(a[i],a[j]);
		if (a[1][1]+a[1][2]==N)
		{
			if (N%2==0 && a[1][1]==a[1][2])
			{
				fo(i,1,N/2) printf("%c%c",a[1][3],a[1][4]);
				printf("\n");
				continue;
			}
			printf("IMPOSSIBLE\n");
			continue;
		}
		bool re=0;
		fo(i,1,3)
		if ((a[i][1] || a[i][2]) && a[i][1]<=a[i][2])
		{
			printf("IMPOSSIBLE\n");
			re=1;
			break;		
		} else a[i][1]-=a[i][2];
		if (re) continue;
		int tot=0,num=0;
		fo(i,1,3)
			fo(j,i+1,3)
			if (a[i][1]<a[j][1]) swap(a[i],a[j]);
		fo(i,1,3) num+=a[i][1];
		if (a[1][1]>num/2)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		memset(ans,0,sizeof ans);
		for(int i=1;a[1][1];i+=2,a[1][1]--) ans[i]=a[1][3];
		bool ok=0;
		fd(i,num,1)
		if (ans[i]==0)
		{
			if (ans[i+1]!=a[2][3] && a[2][1])
			{
				ans[i]=a[2][3];
				a[2][1]--;
			} else
			if (ans[i+1]!=a[3][3] && a[3][1])
			{
				ans[i]=a[3][3];
				a[3][1]--;
			} else
			{
				ok=1;
				break;
			}
		}
		if (ok)
		{
			printf("IMPOSSIBLE\n");
			continue;			
		}
		fo(i,1,num)
		{
			printf("%c",ans[i]);
			fo(j,1,3)
			if (ans[i]==a[j][3])
			{
				while (a[j][2])
				{
					a[j][2]--;
					printf("%c%c",a[j][4],a[j][3]);
				}
			}
		}
		printf("\n");
	}
}
