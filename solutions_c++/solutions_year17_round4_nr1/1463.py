#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
#include <stdio.h>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		int n, p, m[4];
		cin >> n >> p;
		for (int i = 0; i < p; i++)
			m[i] = 0;
		for (int i = 0; i < n; i++) {
			int g;
			cin >> g;
			m[g % p]++;
		}

		int sol;
		if (p == 2) {
			sol = m[0] + m[1] / 2;
			m[1] = m[1] % 2;
		} else if (p == 3) {
			int pairs = min(m[1], m[2]);
			sol = m[0] + pairs;
			m[1] -= pairs;
			m[2] -= pairs;
			if (m[1] > 0) {
				sol += m[1] / p;
				m[1] = m[1] % p;
			}
			if (m[2] > 0) {
				sol += m[2] / p;
				m[2] = m[2] % p;
			}
		} else if (p == 4) {
			int halves = m[2];
			int pairs = min(m[1], m[3]);
			sol = m[0] + pairs + halves / 2;
			m[1] -= pairs;
			m[3] -= pairs;
			m[2] = m[2] % 2;

			if (m[1] > 0) {
				sol += m[1] / p;
				m[1] = m[1] % p;
			}
			if (m[3] > 0) {
				sol += m[3] / p;
				m[3] = m[3] % p;
			}

			if (m[2] == 1) {
				if (m[1] >= 2) {
					sol += 1;
					m[1] -= 2;
					m[2]--;
				} else if (m[3] >= 2) {
					sol += 1;
					m[3] -= 2;
					m[2]--;
				}
			}
		}
		for (int i = 1; i < p; i++)
			if (m[i] > 0) {
				sol++;
				break;
			}

		cout << "Case #" << cas << ": " << sol << endl;

	}
	return 0;
}
