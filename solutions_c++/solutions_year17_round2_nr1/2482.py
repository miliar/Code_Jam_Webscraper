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
long double maxi = 0;
int main(){
	ios_base::sync_with_stdio (0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;cin>>T;
	for(int tc = 1 ; tc<=T ; tc++){
		maxi = 0;
		cout<<"Case #"<<tc<<": ";
		ll d,n;
		cin>>d>>n;
		for(int i=1 ; i<=n ; i++){
			long double x;cin>>x;
			x = max((long double)0.0,d-x);
			long double s;cin>>s;
			maxi = max(maxi , x/s);
		}
		cout<<setprecision(7)<<fixed<<d/maxi<<endl;
	}
	return 0;
}

