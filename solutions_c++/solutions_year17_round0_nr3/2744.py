	#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-8;
const int INF = (int)1e9;
const int MAXN = 500500;

int T;
ll n, k;
pair<ll, ll> ans;
map<ll, ll> elems;

int main() {

    cin >> T;
    forn(tt, T) {
        printf("Case #%d: ", tt + 1);
        
        cin >> n >> k;

		k--;
		elems.clear();
		elems[-n] = 1;
		ans = {-1, -1};

		while (true) {
			pair<ll, ll> cur = *elems.begin();
			
			ll val = -cur.X;
			ll cnt = cur.Y;

			elems.erase(cur.X);

			ll d1 = (val - 1) / 2;
			ll d2 = val / 2;
			
			k -= cnt;
			//cout << "val=" << val << endl;
			//cout << "cnt=" << cnt << endl;
			//cout << "k=" << k << endl;

			if (k < 0) {
				ans = {d1, d2};
				break;
			}

			if (d1 > 0) {
				elems[-d1] += cnt;
			}
			if (d2 > 0) {
				elems[-d2] += cnt;
			}
		}		        

		assert(ans.X != -1 && ans.Y != -1);
		if (ans.X < ans.Y) {
			swap(ans.X, ans.Y);
		}

        cout << ans.X << ' ' << ans.Y << '\n';        
    }
    
    return 0;
}