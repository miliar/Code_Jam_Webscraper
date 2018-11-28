//Author: Stefan Toman

#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		int n, p;
		cin >> n >> p;
		vector<int> counts(p, 0);
		for(int j = 0; j < n; j++) {
			int tmp;
			cin >> tmp;
			counts[tmp % p]++;
		}
		int r = counts[0];
		if(p == 2) {
			r += counts[1] / 2;
			counts[1] %= 2;
		}
		if(p > 2) {
			int m = min(counts[1], counts[p-1]);
			r += m;
			counts[1] -= m;
			counts[p-1] -= m;
		}
		if(p == 4) {
			r += counts[2] / 2;
			counts[2] %= 2;
		}
		int rem = 0;
		for(int j = 1; j < p; j++) {
			for(int k = 0; k < counts[j]; k++) {
				if(rem == 0) r++;
				rem = (rem + j) % p;
			}
		}

		cout << "Case #" << i << ": " << r << endl;
	}
	return 0;
}

