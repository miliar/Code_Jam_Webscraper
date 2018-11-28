#include<bits/stdc++.h>
using namespace std;

#define INF (int)1e9
#define EPS 1e-9

#define pb push_back
#define fill(a,v) memset(a, v, sizeof a)
#define sz(a) a.size()
#define mp make_pair

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef map<int,int> mii;


int t,n,m,x,y,k;


int main()
{
	freopen("A-large(1).in","r",stdin);
    freopen("A-large(1).out","w",stdout);
	scanf("%d",&t);
	string s;
	for(int tc=1;tc<=t;tc++)
	{

		bool finding;
		vector<string> v;
		vector<int> pos;
		scanf("%d%d",&n,&m);

		for(int i=0;i<n;i++)
		{
			cin>>s;
			v.pb(s);
		}

		printf("Case #%d:\n",tc);

		for(int i=0;i<n;i++)
		{
			finding=false;
			for(int j=0;j<m;j++)
			{
				if(v[i][j]!='?')
				{
					finding=true;
					break;
				}
			}

			if(finding)
			{
				for(int j=0;j<m;j++)
				{
					if(v[i][j]!='?')
					{
						k=j-1;
						while(k>=0)
						{
							if(v[i][k]!='?')break;
							v[i][k]=v[i][j];
							k--;
						}
						k=j+1;
						while(k<m)
						{
							if(v[i][k]!='?')break;
							v[i][k]=v[i][j];
							k++;
						}
					}
				}
			}
			else pos.pb(i);

		}

		for(int i=0;i<pos.size();i++)
		{
			if(!pos[i])
			{
				int j=1;
				while(v[j][0]=='?')
				{
					j++;
				}

				for(int k=0;k<m;k++)
				{
					v[pos[i]][k]=v[j][k];
				}
			}

			else
			{
				int j=pos[i]-1;
				while(v[j][0]=='?')
				{
					j--;
				}

				for(int k=0;k<m;k++)
				{
					v[pos[i]][k]=v[j][k];
				}
			}
		}
		

		for(int i=0;i<n;i++)
		{
			cout<<v[i]<<endl;
		}

	}
	return 0;	
}