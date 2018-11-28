#include<bits/stdc++.h>
using namespace std;
typedef double db;
typedef long long LL;
const int maxn=100;
struct node
{
	int l,r;
	bool operator < (const node &o) const
	{
		return l<o.l||(l==o.l&&r<o.r);
	}
}nd[maxn][maxn];
int N,P,a[maxn],b[maxn][maxn],pos[maxn];
bool ok()
{
	for (int i=1;i<=N;i++) if (pos[i]>P) return 0;
	return 1;
}
bool check()
{
	int l=0,r=1e8;
	for (int i=1;i<=N;i++)
	{
		l=max(l,nd[i][pos[i]].l);
		r=min(r,nd[i][pos[i]].r);
	}
	return l<=r;
}
void change()
{
	int k=-1;
	for (int i=1;i<=N;i++) if (k==-1||nd[i][pos[i]].l<nd[k][pos[k]].l) k=i;
	pos[k]++;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
		scanf("%d%d",&N,&P);
		for (int i=1;i<=N;i++) scanf("%d",&a[i]);
		for (int i=1;i<=N;i++)
		    for (int j=1;j<=P;j++)
		        scanf("%d",&b[i][j]);
		for (int i=1;i<=N;i++)
		{
			for (int j=1;j<=P;j++)
			{
				nd[i][j].l=(int)ceil((db)b[i][j]/a[i]/1.1);
				//nd[i][j].l=max(nd[i][j].l,1);
				nd[i][j].r=(int)floor((db)b[i][j]/a[i]/0.9);
			}
			sort(nd[i]+1,nd[i]+P+1);
		}
		for (int i=1;i<=N;i++) pos[i]=1;
		int ans=0;
		while (ok())
		{
			if (!check()) change();
			else
			{
				ans++;
				for (int i=1;i<=N;i++) pos[i]++;
			}
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
	fclose(stdin);fclose(stdout);
}
