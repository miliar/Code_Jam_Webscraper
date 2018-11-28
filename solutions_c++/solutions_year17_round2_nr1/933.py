#include <bits/stdc++.h>
#define endl '\n'
#define forn(i, n) for(int i=0;i<n;i++)
#define lli long long int
#define pii pair<int,int>
#define psi pair<int,pii>
#define fi first
#define se second
#define pb push_back

using namespace std;

const int MAXN = 1000001;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout<<fixed<<setprecision(9);
	int t,n,u=1;
	double x,v,d;
	cin>>t;

	while(t--) {
		cin>>d>>n;
		double ans = 0;
		forn(i, n) {
			cin>>x>>v;
			double needed = (d - x) / v;
			ans = max(ans, needed);
		}
		ans = d / ans;
		cout<<"Case #"<<u++<<": "<<ans<<endl;
	}
	return 0;
}
