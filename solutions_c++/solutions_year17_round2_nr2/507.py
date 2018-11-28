//Author: Stefan Toman

#include <iostream>
#include <vector>
#include <string>

using namespace std;

string solve() {
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;
	string ret = "";
	char last = 'R';
	if(r == 0) last = 'B';
	if(r == 0 && b == 0) last = 'Y';

	while(ret.length() < n) {	
		if((last == 'R' && (b > y || (b == y && ret.length() > 0 && ret[0] == 'B'))) || (last == 'Y' && (b > r || (b == r && ret.length() > 0 && ret[0] == 'B')))) {
			//next b
			ret += 'B';
			b--;
			while(o > 0) {
				ret += 'O';
				o--;
				if(ret.length() != n || ret[0] != 'B') {
					ret += 'B';
					b--;
				}
			}
			if(b < 0) return "IMPOSSIBLE";
			last = 'B';
		}
		else if((last == 'R' && (y >= b || (y == b && ret.length() > 0 && ret[0] == 'Y'))) || (last == 'B' && (y >= r || (y == r && ret.length() > 0 && ret[0] == 'Y')))) {
			//next y
			ret += 'Y';
			y--;
			while(v > 0) {
				ret += 'V';
				v--;
				if(ret.length() != n || ret[0] != 'Y') {
					ret += 'Y';
					y--;
				}
			}
			if(y < 0) return "IMPOSSIBLE";
			last = 'Y';
		}
		else {
			//next r
			ret += 'R';
			r--;
			while(g > 0) {
				ret += 'G';
				g--;
				if(ret.length() != n || ret[0] != 'R') {
					ret += 'R';
					r--;
				}
			}
			if(r < 0) return "IMPOSSIBLE";
			last = 'R';
		}
	}
	if(ret[0] == ret[ret.length() - 1]) return "IMPOSSIBLE";
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
			cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}

