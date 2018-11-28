#include <bits/stdc++.h>

using namespace std;

namespace Solve {

	typedef pair<long, long> pll;

	template<typename T> inline bool _min(T& data, const T& comp) {
		if (comp < data) {
			data = comp;
			return true;
		}
		return false;
	}

	template<typename T> inline bool _max(T& data, const T& comp) {
		if (data < comp) {
			data = comp;
			return true;
		}
		return false;
	}


	long n, m, c;

	struct Ticket {
		long pos, id;
		inline bool operator<(const Ticket &t) const {
			if (pos != t.pos) return pos < t.pos;
			return id < t.id;
	//		if (id != t.id) return id < t.id;
	//		return pos < t.pos;
		}
	} ticket[1024];

	long tsz[1024], tpos[1024];
	set<long> rider[1024];
	long cnt[1024];

	bool check(const long &count) {
		bool used[1024];
		set<long> rider;
		long c = 0;
		memset(used, 0, sizeof used);
		for (long i = 0; i < count; ++ i) {
			for (long j = 1, k = 0; j <= n; ++ j) {
				for (; k < m; ++ k) {
					if (used[k]) continue;
					if (ticket[k].pos < j) continue;
					if (rider.count(ticket[k].id)) continue;
					rider.insert(ticket[k].id);
					used[k] = true;
					c += 1;
					if (c == m) return true;
					break;
				}
			}
			rider.clear();
		}
		return false;
	}

	void main() {
		ios::sync_with_stdio(false);
		register long i, j;
		long T;
		cin >> T;
		for (long t = 1; t <= T; ++ t) {
			cin >> n >> c >> m;
			for (i = 0; i < m; ++ i) {
				cin >> ticket[i].pos >> ticket[i].id;
			}
			sort(ticket, ticket + m);
			memset(tsz, 0, sizeof tsz);
			memset(tpos, 0, sizeof tpos);
			for (i = 0; i < 1024; ++ i) rider[i].clear();
			long ans = 1, promo = 0;
			long lft = 1, rgt = 1024;
			while (lft < rgt - 1) {
				long mid = (lft + rgt) >> 1;
				if (check(mid)) rgt = mid;
				else lft = mid;
			}
			if (check(lft)) ans = lft;
			else if (check(lft + 1)) ans = lft + 1;
			else if (check(lft + 2)) ans = lft + 2;
			else abort();
/*
			for (i = 0; i < m; ++ i) {
				bool flag = false;
				// Loop 1: find exact seat
				for (j = 0; j < ans; ++ j) {
					// Seat is empty, and not already take this train
					if (tpos[j] < ticket[i].pos && !rider[j].count(ticket[i].id)) {
						tpos[j] = ticket[i].pos;
						tsz[j] += 1;
						rider[j].insert(ticket[i].id);
						flag = true;
						break;
					}
				}
				if (flag) continue;
				// Loop 2: find promo seat
				long mnsz = LONG_MAX, p = -1;
				for (j = 0; j < ans; ++ j) {
					if (tsz[j] < mnsz && !rider[j].count(ticket[i].id)) {
						mnsz = tsz[j];
						p = j;
					}
				}
				if (mnsz < ticket[i].pos)  {
					tsz[p] += 1;
					rider[p].insert(ticket[i].id);
					promo += 1;
					flag = true;
				}
*/
/*
				// Loop 2: find promo seat
				for (j = 0; j < ans; ++ j) {
					if (tsz[j] < ticket[i].pos && !rider[j].count(ticket[i].id)) {
						tsz[j] += 1;
						rider[j].insert(ticket[i].id);
						promo += 1;
						flag = true;
						break;
					}
				}
*/
/*
				if (flag) continue;
				// Add a new train.
				tsz[ans] = 1;
				tpos[ans] = ticket[i].pos;
				ans += 1;
			}
*/
/*
			promo = 0;
			memset(tpos, 0, sizeof tpos);
			memset(tsz, 0, sizeof tsz);
			for (i = 0; i < 1024; ++ i) rider[i].clear();
			for (i = 0; i < m; ++ i) {
				bool flag = false;
				// Loop 1: find exact seat
				for (j = 0; j < ans; ++ j) {
					// Seat is empty, and not already take this train
					if (tpos[j] < ticket[i].pos && !rider[j].count(ticket[i].id)) {
						tpos[j] = ticket[i].pos;
						tsz[j] += 1;
						rider[j].insert(ticket[i].id);
						flag = true;
						break;
					}
				}
				if (flag) continue;
				// Loop 2: find promo seat
				long mnsz = LONG_MAX, p = -1;
				for (j = 0; j < ans; ++ j) {
					if (tsz[j] < mnsz && !rider[j].count(ticket[i].id)) {
						mnsz = tsz[j];
						p = j;
					}
				}
				if (mnsz >= ticket[i].pos) abort();
				tsz[p] += 1;
				rider[p].insert(ticket[i].id);
				promo += 1;
			}
*/
			memset(cnt, 0, sizeof cnt);
			promo = 0;
			for (i = 0; i < m; ++ i) {
				cnt[ticket[i].pos] ++;
			}
			for (i = 1; i <= n; ++ i) {
				if (cnt[i] > ans) promo += cnt[i] - ans;
			}
			cout << "Case #" << t << ": " << ans << " " << promo << endl;
		}
	}
}

int main(void) {
	Solve::main();
	return 0;
}
