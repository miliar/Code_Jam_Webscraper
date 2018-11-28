#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int recipe[60];
int package[60][60];
int low[60][60];
int high[60][60];
int idx[60];

int main() {
	int T, n, p;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n >> p;
		for (int j = 0; j < n; j++) cin >> recipe[j];
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < p; k++) {
				cin >> package[j][k];
			}
			sort(package[j], package[j] + p);
		}
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < p; k++) {
				low[j][k] = ceil(package[j][k] / 1.1 / recipe[j]);
				high[j][k] = floor(package[j][k] / 0.9 / recipe[j]);
			}
		}
		
		int cnt = 0, num = 0;
		for (int j = 0; j < n; j++) {
			idx[j] = 0;
		}

		while (true) {
			bool flag = false;
			for (int j = 0; j < n; j++) {
				if (idx[j] >= p) {
					flag = true;
					break;
				}
			}
			if (flag) break;

			for (int j = 0; j < n; j++) {
				if (num < low[j][idx[j]]) num = low[j][idx[j]];
			}
			for (int j = 0; j < n; j++) {
				if (num > high[j][idx[j]]) {
					flag = true;
					idx[j]++;
				}
			}

			if (!flag) {
				cnt++;
				for (int j = 0; j < n; j++) idx[j]++;
			}
		}

		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}
}