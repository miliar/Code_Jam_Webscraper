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
	freopen("A-large (1).in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false); cin.tie(0);
	int cs; cin >> cs;
	rep(cc, cs) {
		int k, n; cin >> n >> k;
		vector<pair<double, int>> side(n);
		vector<double> rS(n);
		vector<double> rS2(n);
		rep(i, n) {
			double r, h; cin >> r >> h;
			side[i].first = -2 * r * h;
			side[i].second = i;
			rS[i] = r * r;
			rS2[i] = r * r + (-side[i].first);
		}
		sort(side.begin(), side.end());
		double sol = 0;
		rep(i, n) {
			double cand = rS2[i];
			int sel = 1;
			for (int j = 0; j < side.size(); ++j) {
				if (sel == k) break;
				if (rS[i] < rS[side[j].second]) continue;
				if (i == side[j].second) continue;
				cand += (-side[j].first);
				sel++;
			}
			if (sol < cand) sol = cand;
		}
		double sol2 = sol * PI;

		cout << "Case #" << cc + 1 << ": ";
		printf("%.10lf\n", sol2);
		//cout << "Case #" << cc + 1 << ": " << sol << '\n';
	}
	return 0;
}