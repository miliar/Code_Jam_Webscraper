/*input
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
*/
#include <bits/stdc++.h>
#define fastIo ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define fi first
#define se second
#define sz size
#define pb push_back
#define mp make_pair
using namespace std;

//#define LOCAL
#ifdef LOCAL
	#define DEBUG(x) do { cout << #x << ": " << x << '\n'; } while (0)
#else
	#define DEBUG(x) 
#endif

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;

const int dr[] = {1, 1, 0, -1, -1, -1, 0, 1};
const int dc[] = {0, 1, 1, 1, 0, -1, -1, -1};

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

void solve(){
	int n, k;
	cin >> n >> k;

	vector<pair<long long, long long>> v;
	long long r, h;
	for(int i = 0; i < n; i++){
		cin >> r >> h;
		v.pb(mp(r, r * h));
	}

	sort(all(v));
    double ans = 0.0;
    for(int i = n - 1; i >= k - 1; i--){
        double sum = PI * (v[i].fi * v[i].fi) + 2.0 * PI * v[i].se;
        set<long long> s;
        for(int j = i - 1; j >= 0; j--){
            s.insert(v[j].se);
        }
        auto it = s.end();
        if(!s.empty()) it--;
        for(int j = 0; j < k - 1; j++){
            sum += 2.0 * PI * (*it);
            it--;
        }
        ans = max(ans, sum);
    }

    cout << fixed << setprecision(12) << ans << '\n';
}

int main(){
	fastIo;

	freopen("A2.in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	cin >> t;

	for(int i = 0; i < t; i++){
		cout << "Case #" << i + 1 << ": ";
		solve();
	}


	return 0;
}