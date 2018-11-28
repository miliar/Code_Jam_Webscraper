#include <algorithm>
#include <bitset>
#include <iostream>
#include <queue>
#include <set>
#include <string>

using namespace std;

struct space {
	int l;
	int r;

	space(int l, int r) : l(l), r(r) {}

	bool operator <(const space& other) const {
		if (length() != other.length())
			return length() > other.length();
		if (l != other.l)
			return l < other.l;
		if (r != other.r)
			return r < other.r;

		return false;
	}

	size_t length() const {
		return l - r;
	}

	int mid() const {
		return ((r - 1) + (l + 1)) / 2;
	}
};

int main()
{
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		int n;
		int k;

		cin >> n >> k;

		priority_queue<space> spaces;
		spaces.emplace(0, n + 1);

		int ls = 0;
		int rs = 0;

		while (k--) {
			space c = spaces.top(); spaces.pop();

			int mid = c.mid();
			ls = mid - c.l - 1;
			rs = c.r - mid - 1;

			spaces.emplace(c.l, mid);
			spaces.emplace(mid, c.r);
		}

		cout << "Case #" << tc << ": "
		     << max(ls, rs) << " " << min(ls, rs) << endl;
	}
}
