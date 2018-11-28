#include<bits/stdc++.h>
using namespace std;
int n,P,mod[5],f[101][101][101][4];
int dp(int a, int b,int c,int lo)
{
	if(f[a][b][c][lo] != -1) return f[a][b][c][lo];
	f[a][b][c][lo] = 0;
	if(a) f[a][b][c][lo] = max(f[a][b][c][lo], f[a-1][b][c][(lo+1)%4]);
	if(b) f[a][b][c][lo] = max(f[a][b][c][lo], f[a][b-1][c][(lo+2)%4]);
	if(c) f[a][b][c][lo] = max(f[a][b][c][lo], f[a][b][c-1][(lo+3)%4]);
	if(lo == 0) f[a][b][c][lo]++;
}
int solve()
{
	memset(f, -1, sizeof f);
	return mod[0] + dp(mod[1],mod[2],mod[3],0);
}
void execute()
{
	int x, ans = 0;
	memset(mod, 0, sizeof mod);
	scanf("%d %d",&n,&P);
	for(int i=1; i<=n; i++)
	{
		scanf("%d",&x);
		mod[x%P]++;
	}
	if(P==2) printf("%d\n",mod[0] + (mod[1]+1)/2);
	if(P==3)
	{
		ans = mod[0];
		x = min(mod[1], mod[2]);
		ans += x;
		mod[1] -= x;
		mod[2] -= x;
		ans += (mod[1]+2)/3;
		ans += (mod[2]+2)/3;
		printf("%d\n",ans);
	}
	if(P==4) printf("%d\n",solve());
}
int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d: ",tc);
		execute();
	}
	return 0;
}
