/*
	By: facug91
	From: 
	Name: 
	Date: 11/12/2016
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

int tc, k, n, DP[1<<10], mask, limit;
string s;

int dp (int bm) {
	//cerr<<"bm "<<bm<<endl;
	if (DP[bm] != -1) return DP[bm];
	if (bm == limit) return 0;
	DP[bm] = INF;
	for (int i=0; i<=n-k; i++)
		DP[bm] = min(DP[bm], dp(bm ^ (mask<<i)) + 1);
	return DP[bm];
}

int main () {
	//#ifdef ONLINE_JUDGE
		ios_base::sync_with_stdio(0); cin.tie(0);
	//#endif
	//cout<<fixed<<setprecision(9); cerr<<fixed<<setprecision(9); //cin.ignore(INT_MAX, ' '); //cout<<setfill('0')<<setw(9)
	
	
	cin>>tc;
	for (int it=1; it<=tc; it++) {
		cin>>s>>k;
		int bm = 0;
		n = s.length();
		for (int i=0; i<n; i++) bm = (bm << 1) + (s[i] == '+');
		memset(DP, -1, sizeof DP);
		mask = (1 << k) - 1;
		limit = (1 << n) - 1;
		int ans = dp(bm);
		if (ans == INF) cout<<"Case #"<<it<<": "<<"IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<it<<": "<<ans<<endl;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
