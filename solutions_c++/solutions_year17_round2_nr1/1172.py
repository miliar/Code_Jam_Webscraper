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

ll t,n,m,x,y;



int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cin>>m>>n;
		double ans=0;
		while(n--)
		{
			cin>>x>>y;
			ans=max(ans,(double)(m-x)/y);
		}
		printf("Case #%d: ",tc);
		cout<<fixed<<setprecision(6)<<(double)m/ans<<endl;

	}
	return 0;	
}