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

ll adj[105][105];
double cache[105];
vector<pair<double, double>> arr;
ll n, q;
void dfs2(int here, double t, double rem, double speed) {
	if (rem < 0) return;
	double& sol = cache[here];
	// 최대로 초기화 되어 있어야 한다.
	sol = min<double>(sol, t);
	rep(i, n) {
		if (adj[here][i] != -1) {
			double dist = adj[here][i];
			dfs2(i, t + (dist / speed), rem - dist, speed);
		}
	}
}
vi order;
void dfs(int here) {
	order.push_back(here);
	rep(i, n)
		if (adj[here][i] != -1)
			dfs(i);
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false); cin.tie(0);
	int cs; cin >> cs;
	rep(cc, cs) {
		fill(cache, cache + 101, numeric_limits<double>::max());
		order.resize(0);
		cin >> n >> q;
		arr.resize(n);
		rep(i, n) {
			ll ei, si; cin >> ei >> si;
			arr[i].first = ei;
			arr[i].second = si;
		}
		rep(i, n) rep(j, n) {
			cin >> adj[i][j];
		}
		dfs(0);
		double start = 0.0;
		rep(i, order.size()) {
			int here = order[i];
			if (here == 0) {
				dfs2(here, start, arr[here].first, arr[here].second);
			}
			else {
				start = cache[here];
				dfs2(here, start, arr[here].first, arr[here].second);
			}
		}
		int u, v; cin >> u >> v;
		cout << "Case #" << cc + 1 << ": ";
		printf("%.10lf\n", cache[n - 1]);
		//cout << "Case #" << cc + 1 << ": " << sol << '\n';
	}
	return 0;
}