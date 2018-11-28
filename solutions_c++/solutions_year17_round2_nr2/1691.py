#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <string>
#include <algorithm>
#include <numeric>
#include <list>
#include <vector>
#include <functional>

using namespace std;

typedef pair<int, char> ic;

const int N = 8;

const int R = 1;
const int Y = 2;
const int B = 4;

char c[N];
int h[256];

int p[N];

int main() {
#ifdef _DEBUG
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	
	c[R] = 'R';
	c[R | Y] = 'O';
	c[Y] = 'Y';
	c[Y | B] = 'G';
	c[B] = 'B';
	c[B | R] = 'V';

	h['R'] = R;
	h['O'] = R | Y;
	h['Y'] = Y;
	h['G'] = Y | B;
	h['B'] = B;
	h['V'] = B | R;

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		fill(p, p + 8, 0);
		int n;
		cin >> n >> p[R] >> p[R | Y] >> p[Y] >> p[Y | B] >> p[B] >> p[B | R];

		bool imp = false;

		bool r[N];
		fill(r, r + N, false);

		string z[N];
		for (int i = 1; i < N; i <<= 1) {
			int j = 7 ^ i;
			int l = min(p[i], p[j]);
			for (int k = 0; k < l; k++) {
				z[i] += c[i];
				z[i] += c[j];
			}
			p[i] -= l;
			p[j] -= l;
			n -= 2 * l;
			if (p[j] > 0) {
				imp = true;
			}
		}

		if (!imp && n == 0) {
			if (z[R].length() == 0 && z[Y].length() == 0) {
				cout << z[B];
			}
			else if (z[R].length() == 0 && z[B].length() == 0) {
				cout << z[Y];
			}
			else if (z[Y].length() == 0 && z[B].length() == 0) {
				cout << z[R];
			}
			else {
				imp = true;
			}
		}
		else if (!imp) {
			string zz(3000 + 100, ' ');
			vector<ic> f;
			for (int i = 1; i < N; i <<= 1) {
				f.push_back(ic(p[i], c[i]));
			}

			sort(f.begin(), f.end(), greater<ic>());

			int k = 0;
			for (int i = 0; i < f.size() - 1; i++) {
				int d = f[i].first;
				char cc = f[i].second;
				for (int j = i; d > 0; j += 3) {
					k = max(j, k);
					zz[j] = cc;
					d--;
				}
			}

			while (k % 3 != 2) {
				k++;
			}
			int d = f[2].first;
			char cc = f[2].second;
			for (int j = k; d > 0 && j >= 0; j -= 3) {
				zz[j] = cc;
				d--;
			}

			if (d > 0) {
				imp = true;
			}
			else {
				string zzz = "";
				for (int i = 0; i < zz.size(); i++) {
					if (zz[i] != ' ') {
						if (zz[i] == 'R') {
							zzz += z[R];
							z[R] = "";
						} else if (zz[i] == 'Y') {
							zzz += z[Y];
							z[Y] = "";
						}
						else if (zz[i] == 'B') {
							zzz += z[B];
							z[B] = "";
						}
						zzz += zz[i];
					}
				}
				
				for (int i = 0; i < zzz.size(); i++) {
					imp = imp || ((h[zzz[i]] & h[zzz[(i + 1) % zzz.length()]]) > 0);
				}

				if (!imp) {
					cout << zzz;
				}
			}
		}

		if (imp) {
			cout << "IMPOSSIBLE";
		}

		cout << endl;
	}
	
	return 0;
}