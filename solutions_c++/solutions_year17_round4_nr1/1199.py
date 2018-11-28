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

const int MAXN = 1e5 + 5;

int cnt[5];

void solve(int t){
	int n, p, a;
	scanf("%d%d", &n, &p);
	REP(i, 0, p){
		cnt[i] = 0;
	}
	REP(i, 0, n){
		scanf("%d", &a);
		cnt[a % p]++;
	}
	int ans = cnt[0];
	if (p == 2){
		ans += (cnt[1] + 1) / 2;
	} else if (p == 3){
		int add = min(cnt[1], cnt[2]);
		ans += add;
		cnt[1] -= add;
		cnt[2] -= add;
		ans += cnt[1] / 3 + cnt[2] / 3;
		if (cnt[1] % 3 || cnt[2] % 3){
			ans++;
		}
	} else if (p == 4){
		int lim1 = cnt[2] / 2;
		for(int i = 0; i <= lim1; i++){
			int lim2 = min(cnt[1], cnt[3]);
			for(int j = 0; j <= lim2; j++){
				int cnt1 = cnt[1] - j;
				int cnt2 = cnt[2] - 2 * i;
				int cnt3 = cnt[3] - j;
				int lim31 = min(cnt1 / 2, cnt2);
				for(int k = 0; k <= lim31; k++){
					int cnt11 = cnt1 - 2 * k;
					int cnt22 = cnt2 - 2 * k;
					int cur = i + j + k + cnt11 / 4 + cnt3 / 4;
					if (cnt22 > 0 || cnt11 % 4 || cnt3 % 4){
						cur++;
					}
					ans = max(ans, cur + cnt[0]);
				}
				int lim33 = min(cnt3 / 2, cnt2);
				for(int k = 0; k <= lim33; k++){
					int cnt33 = cnt3 - 2 * k;
					int cnt22 = cnt2 - 2 * k;
					int cur = i + j + k + cnt1 / 4 + cnt33 / 4;
					if (cnt22 > 0 || cnt1 % 4 || cnt33 % 4){
						cur++;
					}
					ans = max(ans, cur + cnt[0]);
				}
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
