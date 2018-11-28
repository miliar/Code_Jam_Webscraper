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


int t,n,m,x,y;
vector<pair<int,int>> a;

long double findmax(int index, long double score,int no)
{
	if(no==m)
	{
		return score;
	}

	if(index<0)
	{
		return -score-1;
	}

	long double ans=0;

	ans=findmax(index-1,score+(long double)2*M_PI*a[index].first*a[index].second,no+1);
	ans=max(ans,findmax(index-1,score,no));
	return ans;
}

int main()
{
	freopen("A-small-attempt0(2).in","r",stdin);
    freopen("output.out","w",stdout);
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cin>>n>>m;
		a.clear();
		for(int i=0;i<n;i++)
		{
			cin>>x>>y;
			a.push_back(mp(x,y));
		}
		printf("Case #%d: ",tc);
		sort(a.begin(),a.end());

		long double ans=0;

		for(int i=n-1;i>=m-1;i--)
		{
			ans=max(ans,findmax(i-1,(long double)M_PI*a[i].first*a[i].first+(long double)M_PI*2*a[i].first*a[i].second,1));
		}

		cout<<fixed<<setprecision(7)<<ans<<endl;

	}
	return 0;	
}