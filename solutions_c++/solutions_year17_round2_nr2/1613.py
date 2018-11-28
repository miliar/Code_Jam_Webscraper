#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

pair<bool, string> solve(size_t n, int r, int o, int y, int g, int b, int v, char last)
{
		vector<pair<int, char>> ponies;
		ponies.emplace_back(r, 'R');
		ponies.emplace_back(y, 'Y');
		ponies.emplace_back(b, 'B');
		sort(ponies.rbegin(), ponies.rend());

		string stable;

		while (ponies[0].first > 0) {
			if (ponies[0].second != last) {
				stable += ponies[0].second;
				--ponies[0].first;
			} else {
				if (ponies[1].first == 0) {
					return make_pair(false, "");
				}

				stable += ponies[1].second;
				--ponies[1].first;
			}

			last = *stable.rbegin();

			sort(ponies.rbegin(), ponies.rend());
		}

		if (stable.size() != n)
			return make_pair(false, "");

		if (*stable.begin() == *stable.rbegin())
			return make_pair(false, "");

		return make_pair(true, stable);
}

int main()
{
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		size_t n;
		int r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;

		string sol = "IMPOSSIBLE";

		auto c0 = solve(n, r, o, y, g, b, v, ' ');
		auto c1 = solve(n, r, o, y, g, b, v, 'R');
		auto c2 = solve(n, r, o, y, g, b, v, 'Y');
		auto c3 = solve(n, r, o, y, g, b, v, 'B');

		if (c0.first) {
			sol = c0.second;
		} else if (c1.first) {
			sol = c1.second;
		} else if (c2.first) {
			sol = c2.second;
		} else if (c3.first) {
			sol = c3.second;
		}

		cout << "Case #" << ti << ": " << sol << endl;
	}
}
