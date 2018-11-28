#include <bits/stdc++.h>
using namespace std;

const int MAXN=27; 
const int MOD=1000000007; 
const int INF=2147483647;
const double EPS=1e-8;

int i,j,k,n,m,p,t,x,y,z,ans,cnt,tcase,xcase;
string s[MAXN];
bool f[MAXN];
bool flag;

int main()
{
#ifdef Smile
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	while (cin>>tcase)
	{
		xcase=0;
		while (xcase<tcase)
		{
			xcase++;
			cout<<"Case #"<<xcase<<": "<<endl;
			memset(f,0,sizeof(f));
			flag=false;
			cin>>n>>m;
			for (int i = 0; i < n; ++i)
			{
				cin>>s[i];
				for (int j = 0; j < m; ++j)
				{
					if (s[i][j]!='?')
					{
						f[i]=true;
					}
					if (f[i] && s[i][j]=='?')
					{
						s[i][j]=s[i][j-1];
					}
				}
				if (f[i] && s[i][0]=='?')
				{
					for (int j = m-2; j >= 0; j--)
					{
						if (s[i][j]=='?')
						{
							s[i][j]=s[i][j+1];
						}
					}
				}
			}
			for (int i = 0; i < n; ++i)
			{
				if (f[i]) flag=true;
				if (flag && !f[i])
				{
					f[i]=true;
					s[i]=s[i-1];
				}
			}
			for (int i=n-2;i>=0 ;i--)
			{
				if (!f[i])
				{
					f[i]=true;
					s[i]=s[i+1];
				}
			}
			for (int i = 0; i < n; ++i)
			{
				cout<<s[i]<<endl;
			}
		}	
	}
	return 0;
}