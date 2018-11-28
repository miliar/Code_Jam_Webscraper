/*
 * GCJ2017_1B_B.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int T;
int N;
int R, O, Y, G, B, V;
string ans; // remember to go backwards when adding the extra colors

string doryb(int r, int y, int b) {
	string cur = "";

	if(r > y && r > b) {
		while(y > b) {
			cur = cur + "R";
			r--;
			cur = cur + "Y";
			y--;
		}
		while(b > y) {
			cur = cur + "R";
			r--;
			cur = cur + "B";
			b--;
		}
		while(r > y) {
			cur = cur + "R";
			r--;
			cur = cur + "Y";
			y--;
			cur = cur + "R";
			r--;
			cur = cur + "B";
			b--;
		}
	} else if(y > r && y > b) {
		while(r > b) {
			cur = cur + "Y";
			y--;
			cur = cur + "R";
			r--;
		}
		while(b > r) {
			cur = cur + "Y";
			y--;
			cur = cur + "B";
			b--;
		}
		while(y > r) {
			cur = cur + "Y";
			y--;
			cur = cur + "R";
			r--;
			cur = cur + "Y";
			y--;
			cur = cur + "B";
			b--;
		}
	} else if(b > r && b > y) {
		while(y > r) {
			cur = cur + "B";
			b--;
			cur = cur + "Y";
			y--;
		}
		while(r > y) {
			cur = cur + "B";
			b--;
			cur = cur + "R";
			r--;
		}
		while(b > y) {
			cur = cur + "B";
			b--;
			cur = cur + "Y";
			y--;
			cur = cur + "B";
			b--;
			cur = cur + "R";
			r--;
		}
	} else if(r > b) { // r == y > b
		while(r > b) {
			cur = cur + "R";
			r--;
			cur = cur + "Y";
			y--;
		}
	} else if(r > y) { // r == b > y
		while(r > y) {
			cur = cur + "R";
			r--;
			cur = cur + "B";
			b--;
		}
	} else if(y > r) { // y == b > r
		while(y > r) {
			cur = cur + "B";
			b--;
			cur = cur + "Y";
			y--;
		}
	}
//	cout << "current cur is " << cur << endl;
	// now r == y == b
	if(cur == "") {
		cur = "RYB";
		r--;
	}
	if(r > 0) {
		string seq = "";
		int len = cur.length();
		if(cur[0] == cur[len-1]) {
			if(cur[0] == 'R') {
				seq = "BRY";
			} else if(cur[0] == 'Y') {
				seq = "RYB";
			} else if(cur[0] == 'B') {
				seq = "RBY";
			}
		} else {
			if(cur[0] == 'R' && cur[len-1] == 'Y') {
				seq = "RYB";
			} else if(cur[0] == 'R' && cur[len-1] == 'B') {
				seq = "RYB";
			} else if(cur[0] == 'Y' && cur[len-1] == 'R') {
				seq = "YRB";
			} else if(cur[0] == 'Y' && cur[len-1] == 'B') {
				seq = "YRB";
			} else if(cur[0] == 'B' && cur[len-1] == 'R') {
				seq = "BRY";
			} else if(cur[0] == 'B' && cur[len-1] == 'Y') {
				seq = "BRY";
			}
		}
		while(r > 0) {
			cur = cur + seq;
			r--;
		}
	}
	return cur;
}

void solve() {
	cin >> N >> R >> O >> Y >> G >> B >> V;
	ans = "";
	int r = R, y = Y, b = B;

	if(O == 0 && Y == 0 && B == 0 && V == 0) { // only R and G
		if(R == G) {
			while(R > 0) {
				cout << "RG";
				R--;
			}
			cout << endl;
			return;
		} else {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	if(O == 0 && R == 0 && B == 0 && G == 0) { // only Y and V
		if(Y == V) {
			while(Y > 0) {
				cout << "YV";
				Y--;
			}
			cout << endl;
			return;
		} else {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	if(Y == 0 && R == 0 && V == 0 && G == 0) { // only O and B
		if(B == O) {
			while(B > 0) {
				cout << "BO";
				B--;
			}
			cout << endl;
			return;
		} else {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}

	r = R - G;
	y = Y - V;
	b = B - O;

	if(r <= 0 && G > 0) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	if(y <= 0 && V > 0) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	if(b <= 0 && O > 0) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	if(r > y + b) {
		cout << "IMPOSSIBLE" << endl;
		return;
	} else if(y > r + b) {
		cout << "IMPOSSIBLE" << endl;
		return;
	} else if(b > r + y) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	ans = doryb(r, y, b);
//	cout << "cur ans is " << ans << endl;

	for(int i = 0; i < ans.length(); i++) {
		if(ans[i] == 'R' && G > 0) {
			ans = ans.substr(0, i+1) + "GR" + ans.substr(i+1);
			G--;
		} else if(ans[i] == 'Y' && V > 0) {
			ans = ans.substr(0, i+1) + "VY" + ans.substr(i+1);
			V--;
		} if(ans[i] == 'B' && O > 0) {
			ans = ans.substr(0, i+1) + "OB" + ans.substr(i+1);
			O--;
		}
	}
	cout << ans << endl;
}

int main() {
	freopen("GCJ2017_1B_B.in", "r", stdin);
	freopen("GCJ2017_1B_B.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
