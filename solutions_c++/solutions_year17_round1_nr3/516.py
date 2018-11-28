#include <iostream>
#include <set>
#include <vector>

using namespace std;

struct state {
	int hd;
	int ad;
	int hk;
	int ak;

	state(int hd, int ad, int hk, int ak)
		: hd(hd), ad(ad), hk(hk), ak(ak)
	{}

	bool operator<(const state& o) const
	{
		if (hd != o.hd) {
			return hd < o.hd;
		}
		if (ad != o.ad) {
			return ad < o.ad;
		}
		if (hk != o.hk) {
			return hk < o.hk;
		}
		if (ak != o.ak) {
			return ak < o.ak;
		}
		return false;
	}

	bool operator==(const state& o) const
	{
		return hd == o.hd &&
			ad == o.ad &&
			hk == o.hk &&
			ak == o.ak;
	}

	bool is_win() const
	{
		return hk <= 0;
	}

	bool is_lose() const
	{
		return hd <= 0;
	}
};

int main()
{
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		int hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;

		set<state> seen;
		set<state> current;
		set<state> next;
		bool win = false;
		int round = 0;

		current.emplace(hd, ad, hk, ak);

		do {
			while (!current.empty() && !win) {
				auto c = *current.begin();
				current.erase(current.begin());

				vector<state> cand;

				/* attack */
				cand.emplace_back(c.hd - c.ak, c.ad,
						  c.hk - c.ad, c.ak);

				/* cure */
				cand.emplace_back(hd - c.ak, c.ad,
						  c.hk, c.ak);

				/* buff */
				cand.emplace_back(c.hd - c.ak, c.ad + b,
						  c.hk, c.ak);

				/* debuff */
				cand.emplace_back(c.hd - max(0, c.ak - d), c.ad,
						  c.hk, max(0, c.ak - d));

				for (auto& cstate : cand) {
					if (cstate.is_win()) {
						win = true;
						break;
					}
					if (cstate.is_lose()) {
						continue;
					}
					if (seen.insert(cstate).second) {
						next.insert(cstate);
					}
				}
			}

			swap(current, next);
			++round;
		} while (!current.empty() && !win);

		if (win) {
			cout << "Case #" << ti << ": " << round << endl;
		} else {
			cout << "Case #" << ti << ": IMPOSSIBLE" << endl;
		}
	}
}
