#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++) {
		string s;
		int k, n;
		cin >> s >> k;
		n = s.size();
		bool arr[n];
		bool changes[n+1];
		for (int j=0; j<n; j++) arr[j] = s[j] == '-';
		for (int j=0; j<n; j++) changes[j] = false;
		int flips = 0;
		bool state = false;
		bool ok = true;
		for (int j=0; j<n; j++) {
			if (changes[j]) state = !state;
			if (arr[j] != state) {
				//cout << "flipping at " << j << endl;
				flips++;
				state = !state;
				if (j+k <= n) {
					changes[j+k] = true;
				} else {
					ok = false;
					break;
				}
			}
		}
		if (ok) {
			cout << "Case #" << i+1 << ": " << flips << endl;
		} else {
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		}
	}
}
