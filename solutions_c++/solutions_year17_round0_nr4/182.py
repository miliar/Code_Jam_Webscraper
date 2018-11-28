#include<bits/stdc++.h>
using namespace std;
typedef pair<int, int> ii;
typedef pair<char, ii> cii;
int rook[105][105], bishop[105][105];
int n,m;
bool placeRook(int x,int y)
{
	for(int i=1; i<=n; i++)
		if(rook[x][i] || rook[i][y]) return false;
	return true;
}
bool placeBishop(int x,int y)
{
	for(int i=1; i<=n; i++)
	{
		int j = x+y-i;
		if(j>=1 && j<=n && bishop[i][j]) return false;
		j = i-x+y;
		if(j>=1 && j<=n && bishop[i][j]) return false;
	}
	return true;
}
void solveRook()
{
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++)
			if(placeRook(i, j)) rook[i][j] = 2;
}
void solveBishop()
{
	for(int diag=1; diag<=n; diag++)
		for(int i=1; i<=diag; i++)
		{
			int j = diag-i+1;
			if(placeBishop(i, j)) bishop[i][j] = 2;
			if(placeBishop(n-i+1, n-j+1)) bishop[n-i+1][n-j+1] = 2;
		}
}
void execute()
{
	scanf("%d %d",&n,&m);
	memset(rook, 0, sizeof(rook));
	memset(bishop, 0, sizeof(bishop));
	int x,y;
	char type;
	for(int i=1; i<=m; i++)
	{
		scanf(" %c %d %d",&type,&x,&y);
		if(type!='x') bishop[x][y]=1;
		if(type!='+') rook[x][y]=1;
	}
	solveRook();
	solveBishop();
	vector<cii> ans;
	int point = 0;
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++)
		{
			if(rook[i][j]) point++;
			if(bishop[i][j]) point++;
			if(rook[i][j] + bishop[i][j] >= 3) ans.push_back(cii('o',ii(i,j)));
			else if(rook[i][j]==2) ans.push_back(cii('x',ii(i,j)));
			else if(bishop[i][j]==2) ans.push_back(cii('+',ii(i,j)));
		}
	/*for(int i=1; i<=n; i++)
	{
		for(int j=1; j<=n; j++)
			if(rook[i][j] && bishop[i][j]) printf("o");
			else if(rook[i][j]) printf("x");
			else if(bishop[i][j]) printf("+");
			else printf("_");
		printf("\n");
	}*/
	printf("%d %d\n",point, ans.size());
	for(int i=0; i<ans.size(); i++) printf("%c %d %d\n",ans[i].first, ans[i].second.first, ans[i].second.second);
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d: ",tc);
		execute();
	}
	return 0;
}
