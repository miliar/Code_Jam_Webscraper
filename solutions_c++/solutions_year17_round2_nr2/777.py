#include <bits/stdc++.h>

using namespace std;

int N, R, O, Y, G, B, V;
const string IMPOSSIBLE = "IMPOSSIBLE";

string solve(int r, int b, int y) {
	char colorr = 'R';
	char colorb = 'B';
	char colory = 'Y';
	if (r > b) {
		swap(r, b);
		swap(colorr, colorb);
	}
	if (b > y) {
		swap(b, y);
		swap(colorb, colory);
	}
	if (r > y) {
		swap(r, y);
		swap(colorr, colory);
	}

	if (b + r < y) {
		return IMPOSSIBLE;
	}

	string ret = "";
	for (int i = 1; i <= y; i++) {
		ret += colory;
		if (i <= b) {
			ret += colorb;
		}
		if (i >= y - r + 1) {
			ret += colorr;
		}
	}

	return ret;
}

string solve() {
	if (G > R || O > B || V > Y) {
		return IMPOSSIBLE;
	}

	int eq = (G > 0 && G == R) + (O > 0 && O == B) + (V > 0 && V == Y);
	if (eq > 0) {
		if (eq > 1) {
			return IMPOSSIBLE;
		}
		// eq = 1
		if ((R > 0) + (B > 0) + (Y > 0) > 1) {
			return IMPOSSIBLE;
		}
		string s;
		if (R > 0) s = "RG";
		if (B > 0) s = "BO";
		if (Y > 0) s = "YV";
		int cnt = max(max(R, B), Y);

		string ret = "";
		while (cnt--) {
			ret += s;
		}
		return ret;
	}

	string ret = solve(R - G, B - O, Y - V);
	if (ret == IMPOSSIBLE) {
		return ret;
	}

	string aux;
	int pos;
	
	pos = ret.find('R');
	aux = "";
	while (G-- > 0) {
		aux += "GR";
	}
	ret = ret.substr(0, pos + 1) + aux + ret.substr(pos + 1);

	pos = ret.find('B');
	aux = "";
	while (O-- > 0) {
		aux += "OB";
	}
	ret = ret.substr(0, pos + 1) + aux + ret.substr(pos + 1);

	pos = ret.find('Y');
	aux = "";
	while (V-- > 0) {
		aux += "VY";
	}
	ret = ret.substr(0, pos + 1) + aux + ret.substr(pos + 1);

	return ret;
}

int main() {
	assert(freopen("B.in", "r", stdin));
	assert(freopen("B.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		cin >> N >> R >> O >> Y >> G >> B >> V;
		string ans = solve();
		assert(ans == IMPOSSIBLE || (int) ans.size() == N);
		cout << ans << endl;
		
		cerr << t << endl;
	}

	return 0;
}
