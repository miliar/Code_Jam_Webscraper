#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef complex<double> point;
#define xx real()
#define yy imag()

#define REP(i, a, b) for(int i = (a); i < (int)(b); i++)
#define REPN(i, a, b) for(int i = (a); i <= (int)(b); i++)
#define FA(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define SZ(x) (int)(x).size()
#define BE(x) (x).begin(), (x).end()
#define SORT(x) sort(BE(x))
#define _1 first
#define _2 second

#define x1 gray_cat_x1
#define y1 gray_cat_y1

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

#define file "I1"

const double EPS = 1e-9;
const double PI = acos(-1.);
const int INF = 1e9;
const ll MOD = 1e9 + 7;

const int MAXN = 1e3 + 5;

ll v[MAXN][MAXN];

ll cnt[MAXN];

int ind[MAXN];
ll l[MAXN], r[MAXN];

void solve(int t){
	int n, p;
	scanf("%d%d", &n, &p);
	REP(i, 0, n){
		scanf("%lld", &cnt[i]);
	}
	REP(i, 0, n){
		REP(j, 0, p){
			scanf("%lld", &v[i][j]);
		}
		sort(v[i], v[i] + p);
	}
	
	int ans = 0;
	REP(i, 0, n){
		ind[i] = 0;
	}
	
	while(1){
		int finish = 0;
		REP(i, 0, n){
			if (ind[i] == p){
				finish = 1;
			}
		}
		if (finish){
			break;
		}
		ll mxl = -1, mnr = INF;
		REP(i, 0, n){
			ll x = v[i][ind[i]];
			l[i] = (10ll * x + 11ll * cnt[i] - 1) / (11ll * cnt[i]);
			r[i] = (10ll * x) / (9ll * cnt[i]);
			mxl = max(mxl, l[i]);
			mnr = min(mnr, r[i]);
		}
		if (mnr < mxl){
			REP(i, 0, n){
				if (r[i] == mnr){
					ind[i]++;
				}
			}
		} else {
			ans++;
			REP(i, 0, n){
				ind[i]++;
			}
		}
	}
	
	printf("Case #%d: ", t);
	printf("%d\n", ans);
}   

int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    //freopen(file".in", "r", stdin); freopen(file".out", "w", stdout);
    int t = 1;
    //cin >> t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        solve(i);    
    }
}
