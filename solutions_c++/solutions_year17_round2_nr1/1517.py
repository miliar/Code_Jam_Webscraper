#include <cstdio>
#include <queue>
#include <iostream>       
#include <string>
#include <vector>
#include <fstream>        
#include <functional> 
#include <algorithm>  
#include <cstdlib>    
#include <cstring>    
#include <map>        
#include <iomanip>    
#include <limits> 
#include <unordered_map>
#include <set>
#include <cmath>
#include <numeric> //accumulate
#include <stack>
#include <bitset>

//#include <unordered_set>//unordered_set

#define rep(i,a) for (int i = 0; i < (a); ++i)
#define rep2(i,a,b) for (int i = (a); i < (b); ++i)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define PI 3.14159265359;

using namespace std;
typedef long long ll;
typedef double lf;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> pli;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<pair<int, int>> vpii;
typedef vector<vector<int>> vvi;
typedef const vector<int> cvi;
typedef vector<bool> vb;

//const ll INF = 1ull << 62;
const int INF = 987654321;
const int MOD = 1000000007;


int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false); cin.tie(0);
	int cs; cin >> cs;
	rep(cc, cs) {
		double d, n; cin >> d >> n;
		vector<pair<double, double>> arr(n);
		rep(i, n) {
			double ki, si; cin >> ki >> si;
			arr[i].first = ki;
			arr[i].second = si;
		}
		sort(arr.begin(), arr.end());
		double prv = (d - arr.back().first) / arr.back().second;
		for (int i = arr.size() - 2; i >= 0; --i) {
			double cur = (d - arr[i].first) / arr[i].second;
			prv = max<double>(cur, prv);
		}
		double sol = d / prv;
		cout << "Case #" << cc + 1 << ": ";
		printf("%.10lf\n", sol);
		//cout << "Case #" << cc + 1 << ": " << sol << '\n';
	}
	return 0;
}