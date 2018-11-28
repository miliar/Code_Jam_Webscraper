#include <iostream>
#include <string>

using namespace std;

#define DEBUG 0

void flip(string& s, int n, int m) {
	for (int i = n; i <= m; i++) {
		if (s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
}

bool happy(string& s) {
	if (s.find('-') == string::npos) return true;
	return false;
}

int main() {

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		string laststr;
		string pancakes;
		cin >> pancakes;
		int k;
		cin >> k;
		int y = 0;
		if (DEBUG) cout << pancakes.length() << ' ' << k << endl;
		while(!happy(pancakes)) {
			if (DEBUG) cout << pancakes << endl;
			if (pancakes.length() < k) {
				y = -1;
				break;
			}
			if (pancakes.find('+') == string::npos) {
				if ((pancakes.length() % k) == 0) {
					y = pancakes.length() / k;
					break;
				}
			}

			if (DEBUG) cout << pancakes << endl;
		for (int e = 0; e <= ((pancakes.length()-k)/2); e++) {
			if (DEBUG) cout << "e=" << e;
			if (pancakes.at(pancakes.length()-1-e) == '-') {
				//flip end
				flip(pancakes, pancakes.length()-k-e, pancakes.length()-1-e);
				y++;
			}
			if (DEBUG) cout << " " << pancakes << endl;
			if (pancakes.at(e) == '-') {
				//flip beginning
				flip(pancakes, e, k-1+e);
				y++;
			}
			if (DEBUG) cout << " " << pancakes << endl;
		}
			if (DEBUG) cout << pancakes << endl;
			if (pancakes == laststr) {
				int c = 0;
				for (int ii = 0; ii < pancakes.length(); ii++) {
					if (pancakes.at(ii) == '-') c++;
					//else c--;
				}
				if ((c%k) < k) {
					y = -1;
					if (DEBUG) cout << "LOOK AT " << i << endl;
					break;
				}
				//break;
			}
			laststr = pancakes;
		}

		if (y >= 0)
			cout << "Case #" << i << ": " << y << endl;
		else
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
	}

	return 0;
}