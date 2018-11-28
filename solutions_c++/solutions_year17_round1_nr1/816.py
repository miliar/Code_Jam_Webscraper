#include <iostream>
#include <string>
using namespace std;

void solve() {
	cout << endl;
	int R, C;
	cin >> R >> C;
	string xlast = "";
	int xunknown = 0;
	for (int i = 0; i < R; i++) {
		string ins;
		string outs;
		cin >> ins;
		char last = '?';
		int unknown = 0;
		for (int j = 0; j < C; j++) {
			if (ins[j] != '?') {
				last = ins[j];
				for (unknown++; unknown > 0; unknown--) outs += last;
			} else if (last == '?') {
				unknown++;
			} else {
				outs += last;
			}
		}
		if (unknown <= 0) {
			xlast = outs;
			for (xunknown++; xunknown > 0; xunknown--) cout << xlast << endl;
		} else if (xlast == "") {
			xunknown++;
		} else {
			cout << xlast << endl;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << (t+1) << ":";
		solve();
	}
	return 0;
}
