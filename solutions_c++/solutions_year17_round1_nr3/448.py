#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define drep(i, a, b) for (int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define pb(x) push_back(x)
#define mp(x, y) (make_pair(x, y))
#define clr(x) memset(x, 0, sizeof(x))
#define xx first
#define yy second

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;
template <class T> inline void read(T &n) {
    char c; int flag = 1;
    for (c = getchar(); !(c >= '0' && c <= '9' || c == '-'); c = getchar()); if (c == '-') flag = -1, n = 0; else n = c - '0';
    for (c = getchar(); c >= '0' && c <= '9'; c = getchar()) n = n * 10 + c - '0'; n *= flag;
}
//***************************

int hd, ad, hk, ak, B, D;

void solve() {
	scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &B, &D);
	
	if (hk <= ad) {
		puts("1");
		return;
	}
	
	int ans = inf;
	
	rep(debuff, 0, 200)
		rep(buff, 0, 200) {
			int hd = ::hd, ad = ::ad, hk = ::hk, ak = ::ak;
			int cnt = 0, ok = true;
			
			rep(i, 1, debuff) {
				int nxt_ak = max(0, ak - D);
				
				// cure first
				if (hd - nxt_ak <= 0) {
					cnt++;
					hd = ::hd - ak;
				}
				
				if (hd <= 0) {
					ok = false;
					break;
				}
				
				// debuff
				ak = nxt_ak;
				hd -= ak;
				++cnt;
				
				if (hd <= 0) {
					ok = false;
					break;
				}
			}
			
			rep(i, 1, buff) {
				// cure first
				if (hd - ak <= 0) {
					cnt++;
					hd = ::hd - ak;
				}
				
				if (hd <= 0) {
					ok = false;
					break;
				}
				
				ad += B;
				hd -= ak;
				++cnt;
				
				if (hd <= 0) {
					ok = false;
					break;
				}
			}
			
			rep(i, 1, 10000) {
				if (hk <= ad) {
					++cnt;
					break;
				}
				
				if (hd - ak <= 0) {
					++cnt;
					hd = ::hd - ak;
				}
				
				if (hd <= 0) {
					ok = false;
					break;
				}
				
				++cnt;
				hk -= ad;
				if (hk <= 0) {
					break;
				}
				hd -= ak;
				if (hd <= 0) {
					ok = false;
					break;
				}
				
			}
			
			if (ok) ans = min(ans, cnt);
		}
	if (ans == inf) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}

int main(int argc, char *argv[]) {
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}
