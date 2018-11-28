#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define ll long long
#define N 30

char g[N][N];
int mark_row[N];
int main()
{
	// freopen("A1.in","r",stdin);
	// freopen("A1.out","w",stdout);
	int t,i,j,k;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		int r,c;
		sd(r);sd(c);
		clr(mark_row);
		for(i=0;i<r;i++)
		{
			ss(g[i]);
			for(j=0;j<c;j++)
				if(g[i][j]!='?')
					mark_row[i]=1;
		}
		int prev_row = 0;
		for(i=0;i<r;i++)
		{
			if(!mark_row[i])	continue;
			// cout<<i<<"-------\n";
			for(j=prev_row;j<r;j++)
			{
				if(j!=i && mark_row[j])	break;
				for(k=0;k<c;k++)
					if(g[i][k]!='?')
						break;
				char c=g[i][k];
				for(k=0;k<c;k++)
				{
					if(g[i][k]!='?')
						c=g[i][k];
					g[j][k]=c;
					// cout<<c;
				}
				// cout<<'\n';
			}
			prev_row = j;
		}
		printf("Case #%d:\n",tt);
		for(i=0;i<r;i++)
			cout<<g[i]<<'\n';
	}
}