#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define REP(i,n) for( (i)=0 ; (i)<(n) ; (i)++ )
#define rep(i,x,n) for( (i)=(x) ; (i)<(n) ; (i)++ )
#define REV(i,n) for( (i)=(n) ; (i)>=0 ; (i)-- )
#define FORIT(it,x) for( (it)=(x).begin() ; (it)!=(x).end() ; (it)++ )
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define SZ(x) ((int)(x).size())
#define MMS(x,n) memset(x,n,sizeof(x))
#define mms(x,n,s) memset(x,n,sizeof(x)*s)
#define pb push_back
#define mp make_pair
#define NX next_permutation
#define UN(x) sort(all(x)),x.erase(unique(all(x)),x.end())
#define CV(x,n) count(all(x),(n))
#define FIND(x,n) find(all(x),(n))-(x).begin()
#define ACC(x) accumulate(all(x),0)
#define PPC(x) __builtin_popcount(x)
#define LZ(x) __builtin_clz(x)
#define TZ(x) __builtin_ctz(x)
#define mxe(x) *max_element(all(x))
#define mne(x) *min_element(all(x))
#define low(x,i) lower_bound(all(x),i)
#define upp(x,i) upper_bound(all(x),i)
#define NXPOW2(x) (1ll << ((int)log2(x)+1))
#define PR(x) cout << #x << " = " << (x) << endl ;

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef pair<int, int> pii;

const int OO = (int) 2e9;
const double eps = 1e-9;

const int N = 30;

int n, m;
char a[N][N];

void solve() {
	//  each char will take the whole row
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (a[i][j] != '?') {
				for (int k = j - 1; k >= 0; k--) {
					if (a[i][k] == '?') {
						a[i][k] = a[i][j];
					} else {
						break;
					}
				}
				for (int k = j + 1; k < m; k++) {
					if (a[i][k] == '?') {
						a[i][k] = a[i][j];
					} else {
						break;
					}
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (a[i][0] == '?') {
			for (int k = i - 1; k >= 0; k--) {
				if (a[k][0] != '?') {
					for (int j = 0; j < m; j++) {
						a[i][j] = a[k][j];
					}
					break;
				}
			}
			if (a[i][0] == '?') {
				for (int k = i + 1; k < n; k++) {
					if (a[k][0] != '?') {
						for (int j = 0; j < m; j++) {
							a[i][j] = a[k][j];
						}
						break;
					}
				}
			}
		}
	}
}

int main() {
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
//#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
//#endif
	int t, tt = 1;
	cin >> t;
	while (t--) {
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		solve();
		cout << "Case #" << tt++ << ":" << "\n";
		for (int i = 0; i < n; i++) {
			cout << a[i] << "\n";
		}
	}
	return 0;
}
