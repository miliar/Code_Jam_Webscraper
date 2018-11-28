#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef long double ld; 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

char a[101][101];
char b[101][101];
int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<":\n";
		int n,m; cin>>n>>m;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				b[i][j]='?';
				cin>>a[i][j];
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(a[i][j]!='?')
				{
					int l = i; int r = i;
					for(int k=i+1;k<n;k++)
					{
						if(a[k][j]=='?') r=k;
						else break;
					}
					for(int k=i-1;k>=0;k--)
					{
						if(a[k][j]=='?') l=k;
						else break;
					}
					for(int k=l;k<=r;k++) b[k][j]=a[i][j];
				}
			}
		}
		for(int j=0;j<m;j++)
		{
			if(b[0][j]=='?')
			{
				int cur=j;
				for(int k=j+1;k<m;k++)
				{
					if(b[0][k]=='?') cur=k;
					else break;
				}
				if(cur==m-1)
				{
					cur=j;
					for(int k=j-1;k>=0;k--)
					{
						if(b[0][k]=='?') cur=k;
						else break;
					}
					assert(cur>0);
					for(int k=0;k<n;k++)
					{
						b[k][j]=b[k][cur-1];
					}
				}
				else
				{
					for(int k=0;k<n;k++)
					{
						b[k][j]=b[k][cur+1];
					}
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cout<<b[i][j];
				if(a[i][j]!='?') assert(a[i][j]==b[i][j]);
			}
			cout<<'\n';
		}
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}
