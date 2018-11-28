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

ll tc, k, n;

ii binary_search (ll i, ll j, ll n) {
	ll mid = (j+i)/2;
	if (n == 1) {
		return ii(j-mid, mid-i);
	}
	ll len = j - i + 1;
	if (len % 2 == 0) {
		if (n % 2 != 0) {
			return binary_search(i, mid-1, n/2);
		} else {
			return binary_search(mid+1, j, n/2);
		}
	} else {
		if (n % 2 == 0) {
			return binary_search(i, mid-1, n/2);
		} else {
			return binary_search(mid+1, j, n/2);
		}
	}
}

int main () {
	//#ifdef ONLINE_JUDGE
		//ios_base::sync_with_stdio(0); cin.tie(0);
	//#endif
	//cout<<fixed<<setprecision(9); cerr<<fixed<<setprecision(9); //cin.ignore(INT_MAX, ' '); //cout<<setfill('0')<<setw(9)
	ll tc = 1, i, j, k;
	
	cin>>tc;
	for (int it=1; it<=tc; it++) {
		cin>>n>>k;
		ii ans = binary_search(0, n-1, k);
		cout<<"Case #"<<it<<": "<<ans.F<<" "<<ans.S<<endl;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
