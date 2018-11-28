#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

enum Color { R=0, O, Y, G, B, V };
const char *r = "ROYGBV";

string align(int n, const vector<int> &unicorn) {
	int mcnt = unicorn[R] + unicorn[O] + unicorn[V];
	for (int i = 2; i < 6; i += 2) {
		mcnt = max<int>(mcnt, unicorn[i-1] + unicorn[i] + unicorn[i+1]);
	}
	if (mcnt > n / 2) {
		return "IMPOSSIBLE";
	}
	vector<Color> type { R, O, Y, G, B, V };
	sort(type.begin(), type.end(), [&](auto a, auto b) {
		return unicorn[a] > unicorn[b];
	});

	string ans(n, 'N');
	int k = 0;
	for (int i = 0; i < 6; ++i) {
		for (int j = 0; j < unicorn[type[i]]; ++j) {
			if (k >= n)
				k = 1;
			ans[k] = r[type[i]];
			k += 2;
		}
	}
	return ans;
}

int main(void) {
	cout.sync_with_stdio(false);
	int nTests;
	cin >> nTests;
	for (int t = 1; t <= nTests; ++t) {
		int n;
		cin >> n;
		vector<int> unicorn(6);
		for (int i = 0; i < 6; ++i)
			cin >> unicorn[i];
		cout << "Case #" << t << ": ";
		cout << align(n, unicorn) << endl;
	}
	return 0;
}
