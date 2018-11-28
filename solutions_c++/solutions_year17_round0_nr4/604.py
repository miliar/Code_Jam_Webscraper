#include<bits/stdc++.h>
#define X first
#define Y second
using namespace std;
char s[105][105],str[5],ori[105][105];
bool e[405][405],hsh[405];
vector<pair<int,int> > res;
bool dfs(int u,int t)
{
	if(u==t) return 1;
	hsh[u]=1;
	for(int i=0;i<=t;i++)
	{
		if(e[u][i]&&!hsh[i]&&dfs(i,t))
		{
			e[u][i]=0;
			e[i][u]=1;
			return 1;
		}
	}
	return 0;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("new_outputlarge_D.txt","w",stdout);
	int t,n,m,i,x,y,ct,num=1,j;
	scanf("%d",&t);
	while(t--)
	{
		res.clear();
		ct=0;
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
				s[i][j]=ori[i][j]='.';
			s[i][n+1]=ori[i][n+1]='\0';
		}
		while(m--)
		{
			scanf("%s%d%d",str,&x,&y);
			s[x][y]=str[0];
			ori[x][y]=str[0];
		}

		memset(e,0,sizeof e);
		for(i=1;i<=n;i++)
		{
			e[0][i]=1;
			e[n+i][n+n+1]=1;
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(s[i][j]=='.'||s[i][j]=='+')
					e[i][j+n]=1;
				else e[0][i]=0,e[j+n][n+n+1]=0;
			}
		}
		memset(hsh,0,sizeof hsh);
		while(dfs(0,n+n+1)) memset(hsh,0,sizeof hsh);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				if(e[j+n][i])
				{
					if(s[i][j]=='+') s[i][j]='o';
					else s[i][j]='x';
				}


		memset(e,0,sizeof e);
		for(i=1;i<=2*n-1;i++) e[0][i]=1;
		for(i=2*n;i<=4*n-2;i++) e[i][4*n-1]=1;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
			{
				if(s[i][j]=='.'||s[i][j]=='x')
					e[i-j+n][i+j+2*n-2]=1;
				else e[0][i-j+n]=0,e[i+j+2*n-2][4*n-1]=0;
			}
		memset(hsh,0,sizeof hsh);
		while(dfs(0,4*n-1)) memset(hsh,0,sizeof hsh);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				if(e[i+j+2*n-2][i-j+n])
				{
					if(s[i][j]=='x') s[i][j]='o';
					else s[i][j]='+';
				}
		// for(i=1;i<=n;i++) printf("%s\n",ori[i]+1);
		// for(i=1;i<=n;i++) printf("%s\n",s[i]+1);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(s[i][j]!=ori[i][j]) 
					res.emplace_back(i,j);
				if(s[i][j]=='o') ct+=2;
				else if(s[i][j]=='+'||s[i][j]=='x') ct++;
			}
		}
		printf("Case #%d: %d %d\n",num++,ct,res.size());
		for(i=0;i<res.size();i++) printf("%c %d %d\n",s[res[i].X][res[i].Y],res[i].X,res[i].Y);

	}
}