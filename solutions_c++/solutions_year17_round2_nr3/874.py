/*
	By: facug91
	From: 
	Name: 
	Date: 21/04/2017
*/

#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
#define endl "\n"
#define EPS 1e-9
#define MP make_pair
#define F first
#define S second
#define prev bjasdbi132ge79qwgdi
#define next usayhkdgisaydgiy212
#define move sdjifha978dyd9sag89
#define DB(x) cerr << " #" << (#x) << ": " << (x)
#define DBL(x) cerr << " #" << (#x) << ": " << (x) << endl
const double PI = acos(-1.0);

#define INF 1000000000
//#define MOD 100000007
#define MAXN 1000

using namespace std;
//using namespace __gnu_pbds;

typedef long long ll;
typedef unsigned long long llu;
typedef pair<ll, ll> ii; typedef pair<ii, int> iii; typedef pair<ii, ii> iiii;
typedef vector<int> vi; typedef vector<ii> vii; typedef vector<iiii> viiii;
//typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set; //insert, find_by_order, order_of_key, erase

int n, q, d[105][105], e, s, u, v;
double DP[105][105];
vector<pair<double, double>> h;

double dp (int curr, int prev, ll rest) {
	if (curr == n-1) return 0;
	if (DP[curr][prev] != -1.0) return DP[curr][prev];
	DP[curr][prev] = 1e16;
	// sumar el tiempo que tarda en viajar
	if (rest >= d[curr][curr+1]) DP[curr][prev] = dp(curr+1, prev, rest-d[curr][curr+1]) + d[curr][curr+1] / h[prev].S;
	if (h[curr].F >= d[curr][curr+1]) DP[curr][prev] = min(DP[curr][prev], dp(curr+1, curr, h[curr].F - d[curr][curr+1]) + d[curr][curr+1] / h[curr].S);
	return DP[curr][prev];
}

int main () {
	#ifdef ONLINE_JUDGE
		ios_base::sync_with_stdio(0); cin.tie(0);
	#endif
	cout<<fixed<<setprecision(9); cerr<<fixed<<setprecision(9); //cin.ignore(INT_MAX, ' '); //cout<<setfill('0')<<setw(9)
	int i, j;
	
	int tc;
	cin >> tc;
	for (int it=1; it<=tc; it++) {
		cout << "Case #" << it << ": ";
		cin>>n>>q;
		h.clear();
		for (i=0; i<n; i++) {
			cin>>e>>s;
			h.emplace_back(e, s);
		}
		for (i=0; i<n; i++) for (j=0; j<n; j++) cin>>d[i][j];
		for (i=0; i<n; i++) for (j=0; j<n; j++) DP[i][j] = -1.0;
		cin>>u>>v;
		cout<<dp(0, 0, 0)<<endl;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
