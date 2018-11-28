#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

int TC;
int Hd, Ad, Hk, Ak, B, D;

void solve()
{
	ll ret = LLONG_MAX;

	rep(i, 110) {
		rep(j, 110) {
			int cH = Hd, cAk = Ak, cAd = Ad, oH = Hk;
			ll cur = 0;

			bool ng = 0;
			int rr = 0;

			while (rr < i) {
				++cur;
				if (cH <= cAk - D) {
					cH = Hd - cAk;
					if (cH <= cAk) {
						ng = 1;
						break;
					}
					continue;
				}
				cAk = max(cAk - D, 0);
				cH -= cAk;
				++rr;
			}

			rr = 0;
			while (rr < j) {
				++cur;
				if (cH <= cAk) {
					cH = Hd - cAk;
					if (cH <= cAk) {
						ng = 1;
						break;
					}
					continue;
				}
				cAd += B;
				cH -= cAk;
				++rr;				
			}

			while (oH > 0) {
				++cur;
				if (oH <= cAd) {
					break;
				}

				if (cH <= cAk) {
					cH = Hd - cAk;
					if (cH <= cAk) {
						ng = 1;
						break;
					}
					continue;
				}
				cH -= cAk;
				oH -= cAd;							
			}

			if (!ng) {
				ret = min(ret, cur);
			}
		}
	}

	if (ret == LLONG_MAX) puts("IMPOSSIBLE");
	else printf("%lld\n", ret);
}

int main() {
	scanf("%d", &TC);

	rep(tc, TC) {
		scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		printf("Case #%d: ", tc + 1);
		solve();
	}

	return 0;
}