/*input
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define PII pair<ll, ll>
#define f first
#define s second
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define MAXN 100005
#define INF LLONG_MAX
#define mod 1000000007
using namespace std;

ll t, r, c;
char mat[55][55];

int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	F(cas,1,t)
	{
		cin>>r>>c;
		F(i,1,r)
			F(j,1,c)
				cin>>mat[i][j];

		F(i,1,r)
		{
			char prv = '?';
			F(j,1,c)
			{
				if(mat[i][j]>='A' && mat[i][j]<='Z' && mat[i][j]!=prv)
				{
					prv = mat[i][j];
					F(k,1,j-1)
					{
						if(mat[i][k]=='?')
							mat[i][k] = prv;
					}
				}
				else
					mat[i][j] = prv;
			}
		}
		F(j,1,c)
		{
			char prv = '?';
			F(i,1,r)
			{
				if(mat[i][j]>='A' && mat[i][j]<='Z' && mat[i][j]!=prv)
				{
					prv = mat[i][j];
					F(k,1,i-1)
					{
						if(mat[k][j]=='?')
							mat[k][j] = prv;
					}
				}
				else
					mat[i][j] = prv;
			}
		}
		cout<<"Case #"<<cas<<":"<<endl;
		F(i,1,r)
		{
			F(j,1,c)
			{
				cout<<mat[i][j];
			}
			cout<<endl;
		}

	}	
	return 0;
}