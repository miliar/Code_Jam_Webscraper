#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <unordered_set>
#include <deque>
using namespace std;

typedef struct {
	int Hd, Ad;
	int Hk, Ak;
} strct_s;

int tn;
int Hd, Ad, Hk, Ak, B, D, Hd0;
strct_s ts, ns;

unordered_set<long long> states;
deque<pair<int, strct_s> > q;

int main() {

	scanf("%d", &tn);
	for(int ctn = 0; ctn < tn; ctn ++) {

		scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		Hd0 = Hd;
		states.clear();
		q.clear();

		long long code = Hd*27000000L + Ad*90000L + Hk*300L + Ak;
		states.insert(code);
		ts.Hd = Hd; ts.Ad = Ad; ts.Hk = Hk; ts.Ak = Ak;
		q.push_back(make_pair(0, ts));

		int ans = -1;

		while (q.size() > 0) {
			int step = q.begin()->first;
			ts = q.begin()->second;
			q.pop_front();

			// Attack
			if (ts.Ad > 0) {
				ns.Hd = ts.Hd; ns.Ad = ts.Ad; ns.Hk = ts.Hk - ts.Ad; ns.Ak = ts.Ak;
				if (ns.Hk <= 0) {
					ans = step + 1;
					break;
				}
				ns.Hd = ns.Hd - ts.Ak;
				if (ns.Hd > 0) {
					code = ns.Hd*27000000L + ns.Ad*90000L + ns.Hk*300L + ns.Ak;
					if (!states.count(code)) {
						states.insert(code);
						q.push_back(make_pair(step+1, ns));
					}
				}	
			}

			// Buff
			if (B > 0) {
				ns.Hd = ts.Hd - ts.Ak; ns.Ad = ts.Ad + B; ns.Hk = ts.Hk; ns.Ak = ts.Ak;
				if (ns.Hd > 0) {
					code = ns.Hd*27000000L + ns.Ad*90000L + ns.Hk*300L + ns.Ak;
					if (!states.count(code)) {
						states.insert(code);
						q.push_back(make_pair(step+1, ns));
					}					
				}
			}

			// Cure
			if (ts.Hd < Hd0) {
				ns.Hd = Hd0 - ts.Ak; ns.Ad = ts.Ad; ns.Hk = ts.Hk; ns.Ak = ts.Ak;
				if (ns.Hd > 0) {
					code = ns.Hd*27000000L + ns.Ad*90000L + ns.Hk*300L + ns.Ak;
					if (!states.count(code)) {
						states.insert(code);
						q.push_back(make_pair(step+1, ns));
					}						
				}
			}

			// Debuf
			if (ts.Ak > 0 && D > 0) {
				ns.Hd = ts.Hd; ns.Ad = ts.Ad; ns.Hk = ts.Hk; ns.Ak = ts.Ak - D;
				if (ns.Ak < 0) ns.Ak = 0;
				ns.Hd = ns.Hd - ns.Ak;
				if (ns.Hd > 0) {
					code = ns.Hd*27000000L + ns.Ad*90000L + ns.Hk*300L + ns.Ak;
					if (!states.count(code)) {
						states.insert(code);
						q.push_back(make_pair(step+1, ns));
					}	
				}
			}
		}

		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", ctn+1);
		}
		else {
			printf("Case #%d: %d\n", ctn+1, ans);
		}

	}

	return 0;

}