/* In The Name Of God */
#include <bits/stdc++.h>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;
pair<long double , long double> pan[1010];
int n,k;
long double dp[1010][1010];
int main(){
	ios_base::sync_with_stdio (0);
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;cin>>T;
	for(int tc=1 ; tc<=T ; tc++){
		for(int i=0 ; i<1010 ; i++)
			for(int j=0 ; j<1010 ; j++)
				dp[i][j] = 0.00000000;
		cin>>n>>k;
		for(int i=1 ; i<=n ; i++)
			cin>> pan[i].xx >> pan[i].yy;
		sort(pan+1,pan+1+n);
		reverse(pan+1,pan+1+n);
		for(int i=1 ; i<=n ; i++)
			dp[i][1] = (pan[i].xx*pan[i].xx + pan[i].xx*2.00*pan[i].yy) * M_PI;
		// cout<<dp[1][1]<<' '<<dp[2][1]<<endl;
		for(int i=1 ; i<=n ; i++)
			for(int j=1 ; j<=k ; j++)
				dp[i][j] = max(dp[i][j] , max(dp[i-1][j] , dp[i-1][j-1] + pan[i].yy*pan[i].xx*2.00*M_PI) );
		cout<<"Case #"<<tc<<": ";
		cout<<fixed<<setprecision(8)<<dp[n][k]<<endl;
	}
	return 0;
}

