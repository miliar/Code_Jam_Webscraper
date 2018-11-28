#include <bits/stdc++.h>
using namespace std;

int T;
int n, m;

long long b[100];
long long a[100][100];

map<long long, int> mapa[100];

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &n);
		scanf("%d", &m);

		for (int i = 0; i < n; i++) {
			mapa[i].clear();
		}

		for (int i = 0; i < n; i++) {
			scanf("%lld", &b[i]);
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%lld", &a[i][j]);
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				mapa[i][a[i][j]]++;
			}
		}

		int ansa = 0;
		vector<pair<long long, int>> tmpa;

		for (long long p = 1;; p++) {
			tmpa.clear();
			tmpa.reserve(n);
			for (int i = 0; i < n; i++) {
				if (mapa[i].size() == 0) {
					goto outa;
				}
				auto it = --mapa[i].end();
				if (it->first * 10 < p * b[i] * 9) {
					goto outa;
				}

				for (auto it = mapa[i].begin(); it != mapa[i].end(); it++) {
					auto au = *it;
					if (au.first * 10 >= p * b[i] * 9
							&& au.first * 10 <= p * b[i] * 11) {
						tmpa.push_back(au);
						break;
					}
				}
			}
			if (tmpa.size() == n) {
				int mina = 1 << 20;

				for (int i = 0; i < n; i++) {
					mina = min(mina, tmpa[i].second);
				}

				for (int i = 0; i < n; i++) {
					auto it = mapa[i].find(tmpa[i].first);

					it->second -= mina;
					if (it->second == 0) {
						mapa[i].erase(it);
					}
				}
				ansa += mina;

				p--;
			}

		}

		outa: 0;

		printf("Case #%d: %d\n", t, ansa);

//		for (int i = 0; i < n; i++) {
//			cout << " " << i << endl;
//			for (auto au : mapa[i]) {
//				cout << au.first << "  " << au.second << endl;
//			}
//		}

	}

	return 0;
}
