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

int t,n,m,x,y,q;
vector<pii> horse;

long double d[101][101];
int b[101];
int c[101];


long double minimum(int pos,int distance,int ho)
{
	if(pos==n-1)
	{
		return 0;
	}

	if(horse[pos].first>=d[pos][pos+1])
	{
		long double ans=d[pos][pos+1]/(long double)horse[pos].second+minimum(pos+1,d[pos][pos+1],pos);

		if(horse[ho].first-distance>=d[pos][pos+1])
		{	
			ans=min(ans,d[pos][pos+1]/(long double)horse[ho].second+minimum(pos+1,d[pos][pos+1]+distance,ho));
		}

		return ans;
	}

	long double ans=d[pos][pos+1]/(long double)horse[ho].second+minimum(pos+1,d[pos][pos+1]+distance,ho);
	return ans;
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		horse.clear();
		cin>>n>>q;
		for(int i=0;i<n;i++)
		{
			cin>>x>>y;
			horse.pb(mp(x,y));
		}

		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				cin>>d[i][j];
			}
		}
		for(int i=0;i<q;i++)
		{
			cin>>b[i];
			cin>>c[i];
		}


		printf("Case #%d: ",tc);

		cout<<fixed<<setprecision(6)<<(d[0][1]/(long double)horse[0].second + minimum(1,d[0][1],0))<<endl;
		
	}
	return 0;	
}