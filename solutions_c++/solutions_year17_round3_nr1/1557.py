#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
using namespace std;
typedef pair<long double, long double> pii;

int n, k;

vector<pii> v;

long double ans, pi = 3.14159265359;

long double pd[1050][1050];

long double dp(int i, int x)
{
		if(i >= n || x >= k) return 0.0;

		double ri = -v[i].f, hi = -v[i].s;

		double sl = 2*pi*ri*hi;

		if(pd[i][x] >= -0.000000001) return pd[i][x];

		if(x == k)
		{
			return pd[i][x] = sl + pi*ri*ri;
		} 

		if(x == 0)
		{
			double add = dp(i + 1, x + 1) + sl + pi*ri*ri;
			double nadd = dp(i + 1, x);

			return pd[i][x] = max(add, nadd);
		}

		double add = dp(i + 1, x + 1) + sl;

		double nadd = dp(i + 1, x);

		return pd[i][x] = max(add, nadd); 
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	int T;

	cin>>T;

	for(int t = 1; t <= T; t++) {

	cin>>n>>k;

	cout<<"Case #"<<t<<": ";

	v.clear();

	memset(pd, -1, sizeof pd);

	for(int i = 1; i <= n; i++)
	{
		long double hi, ri;
		cin>>ri>>hi;

		v.push_back(pii(-ri, -hi));
	}

	sort(v.begin(), v.end());

	cout<<setprecision(9);
	cout<<fixed;

	cout<<dp(0, 0)<<"\n";
}
}