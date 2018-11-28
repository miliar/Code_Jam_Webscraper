#include<bits/stdc++.h>

# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.in","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
# define test(c) ini(c);while(c--)


using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
	rf;
	wf;
	int tt;
	cin>>tt;
	double PI=3.14159265359;
	for(int test=1;test<=tt;test++)
	{
		
		int n,k;
		cin>>n>>k;
		vii inp1;
		for(int i=0;i<n;i++)
		{
			int r,h;
			cin>>r>>h;
			inp1.pb(mp(r,h));
		}
		
		sort(all(inp1),greater<ii>());
		vector<pair<double,double> > inp;
		for(int i=0;i<n;i++) inp.pb(inp1[i]);
		double dp[k][n];
		//int topmost[k][n];
		dp[0][0]=(1.0*PI*(inp[0].first)*(inp[0].first) + 2.0*PI*(inp[0].first)*(inp[0].second));
		//cout<<dp[0][0];
		//topmost[0][0]=0;
		for(int i=1;i<n;i++) dp[0][i]=max(dp[0][i-1],(PI*(inp[i].first)*(inp[i].first) + 2*PI*(inp[i].first)*(inp[i].second)));
		//for(int i=1;i<n;i++) topmost[0][i]=(dp[0][i-1]>((inp[i].first) + 2*PI*(inp[i].first)*(inp[i].second)))?(i-1):i;
		for(int i=1;i<k;i++)
		{
			dp[i][i]=dp[i-1][i-1]+2*PI*(inp[i].first)*(inp[i].second);
			for(int j=i+1;j<n;j++)
			{
				dp[i][j]=max(dp[i][j-1],dp[i-1][j-1]+2*PI*(inp[j].first)*(inp[j].second));
			}
		}
	
	
	
/*	for(int i=0;i<k;i++)
	{
		for(int j=i;j<n;j++)
		{
			cout<<dp[i][j]<<" ";
		}
		cout<<endl;
		}*/	
		cout<<"Case #"<<test<<": "<<fixed<<setprecision(10)<<dp[k-1][n-1]<<endl;

		
		
	}
	
}
