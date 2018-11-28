#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
const int N=100;
int a[N][N],ans[N][N],ok[N],num[N];
int main()
{
	int T;
	scanf("%d",&T);
	int s=0;
	while (T--)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		memset(a,0,sizeof a);
		memset(num,0,sizeof num);
		fo(i,1,n)
		{
			fo(j,1,m)
			{
				char ch;
				while (ch=getchar(),(ch<'A' || ch>'Z') && ch!='?');
				if (ch>='A' && ch<='Z') a[i][j]=ch-'A'+1,num[i]=1; else a[i][j]=0;
			}
		}
		for(int l=1;l<=n;)
		{
			int r=l;
			while (num[r]==0) r++;
			while (r+1<=n && num[r+1]==0) r++;
			memset(ok,0,sizeof ok);
			fo(i,l,r)
				fo(j,1,m)
				if (a[i][j]) ok[j]=a[i][j];
			for(int i=1;i<=m;)
			{
				int j=i;
				while (ok[j]==0) j++;
				int now=ok[j];
				while (j+1<=m && ok[j+1]==0) ++j;
				fo(k,l,r)
					fo(p,i,j) ans[k][p]=now;
				i=j+1;
			}
			l=r+1;
		}
		printf("Case #%d:\n",++s);
		fo(i,1,n)
		{
			fo(j,1,m) printf("%c",ans[i][j]+'A'-1);
			printf("\n");
		}
	}
}
