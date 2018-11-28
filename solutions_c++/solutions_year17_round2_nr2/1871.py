// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include <cstring>
using namespace std;

/*
#define MX 101
char g[MX][MX];

bool v[101], d1[201], d2[201];
int p[201];

int* nqueens(int n) {
	if (n % 6 == 0 || n % 6 == 4 || n%6==2 || n%6==3) {
		for (int i = 0; i < n/2; i++) {
			p[i] = i * 2 + 1;
		}
		for (int i = n / 2, j=0; i < n; i++, j+=2) {
			p[i] = j;
		}
	}
	if (n % 6 == 2) {
		p[n / 2] = 2, p[n / 2 + 1] = 0;
		for (int i = n / 2 + 2; i < n - 1; i++) {
			p[i] = p[i + 1];
		}
		p[n - 1] = 4;
	}
	else if (n % 6 == 3) {
		for (int i = 0; i < n / 2 - 1; i++) {
			p[i] = p[i + 1];
		}
		p[n / 2 - 1] = 1;
		for (int i = n / 2; i < n - 2; i++) {
			p[i] = p[i + 2];
		}
		p[n - 2] = 0, p[n-1] = 2;
	}
	if (n % 6 == 1 || n % 6 == 5) {
		for (int i = 0, j=1; i < n; i++, j=(j+3)%n) {
			p[i] = j;
		}
	}
	return p;
}

int main()
{
	int T;
	int n = 9;
	int *p = nqueens(n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (p[i] == j) {
				cout << "X ";
			}
			else {
				cout << "O ";
			}
		}
		cout << endl;
	}
//	cin >> T;
	//for (int c = 1; c <= T; c++) {
		//memset(v, 0, sizeof(v)); memset(d1, 0, sizeof(d1)); memset(d2, 0, sizeof(d2));
		//memset(p, -1, sizeof(p));
		
		//int n, m;
		//cin >> n >> m;
		//p[0] = 1, v[1] = d1[1] = d2[n] = true;
		//memset(g, 0, sizeof(g));
		//for (int i = 0; i < m; i++) {
			//char c;
			//int x, y;
			//cin >> c >> x >> y;
			//g[x - 1][y - 1] = c;
		//}


		//cout << "Case #" << c << ": ";
		//cout << ret[0] << " " << ret[1] << endl;
	}

    return 0;
}
*/

/*
#include <vector>
using namespace std;
#define MX 27

int main() {
	int T;
	cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		int R, C;
		cin >> R >> C;
		char d[MX][MX];
		for (int i = 0; i < R; i++) {
			scanf("%s", d[i]);
		}
		int pi = -1, ci = -1;
		for (int i = 0; i < R; i++) {
			int pj = -1;
			for (int j = 0; j < C; j++) {
				if (d[i][j] != '?') {
					for (int k = pi+1; k <= i; k++) {
						for (int l = pj+1; l <= j; l++) {
							d[k][l] = d[i][j];
						}
					}
					pj = j;
				}
			}
			if (pj != -1) {
				for (int k = pi + 1; k <= i; k++) {
					for (int l = pj + 1; l < C; l++) {
						d[k][l] = d[i][pj];
					}
				}
				pi = i;
			}
		}
		for (int i = pi + 1; i < R; i++) {
			for (int j = 0; j < C; j++) {
				d[i][j] = d[i - 1][j];
			}
		}
		cout << "Case #" << cs <<":"<< endl;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				cout << d[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}
*/

/*
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
#define MX 51
#define MX1 1000001
int main() {
	int T;
	cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		int N, P, R[MX], I[MX][MX], index[MX], f[MX][MX];
		cin >> N >> P;
		for (int i = 0; i < N; i++) {
			cin >> R[i];
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				cin >> I[i][j];
			}
		}
		vector<pair<int, int> > d[MX];
		vector<int> packs;
		int cnt = 0;
		memset(f, 0, sizeof(f));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				int l = (10 * I[i][j]) / (11 * R[i]);
				if (11 * l * R[i] < 10 * I[i][j]) {
					l++;
				}
				int r = (10 * I[i][j]) / (9 * R[i]);
				if (9 * (r + 1) * R[i] <= 10 * I[i][j]) {
					r++;
				}
				d[i].push_back(pair<int, int>(r, l));
				packs.push_back(r);
				packs.push_back(l);
			}
			sort(d[i].begin(), d[i].end());
			index[i] = 0;
		}
		sort(packs.begin(), packs.end());
		for (int p = 0;  p < packs.size(); p++) {
			vector<int> ff;
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < d[j].size(); k++) {
					if (!f[j][k] && d[j][k].first >= packs[p] && d[j][k].second <= packs[p]) {
						ff.push_back(k);
						break;
					}
				}
			}
			if (ff.size() == N) {
				for (int i = 0; i < N; i++) {
					f[i][ff[i]] = true;
				}
				cnt++;
			}
		}
		cout << "Case #" << cs << ": " << cnt << endl;
	}
	return 0;
}
*/

/*
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		int D, N;
		cin >> D >> N;
		vector<pair<int, int> > d;
		for (int i = 0; i < N; i++) {
			int K, S;
			cin >> K >> S;
			d.push_back(pair<int, int>(K, S));
		}
		sort(d.begin(), d.end());
		double ret = 1.0*(D - d[N-1].first) / d[N - 1].second;
		for (int i = N - 2; i >= 0; i--) {
			double r = 1.0*(D - d[i].first) / d[i].second;
			ret = max(r, ret);
		}
		printf("Case #%d: %0.12f\n", cs, 1.0*D/ret);
	}
	return 0;
}
*/

#include <vector>
#include <set>
#include <algorithm>
using namespace std;

#define MX 1002

int main() {
	int T;
	cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		int N, R, O, Y, G, B, V;
		char str[MX];
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
		vector<pair<int, char> > v;
		v.push_back(pair<int, int> (R, 'R'));
		v.push_back(pair<int, int> (Y, 'Y'));
		v.push_back(pair<int, int> (B, 'B'));
		sort(v.begin(), v.end());
		bool f = true;
		if (v[2].first > N / 2) {
			f = false;
		}
		else {
			int k = N - 2 * v[2].first;
			for (int i = 0; i<N; ) {
				if (v[2].first) {
					str[i] = v[2].second;
					i++;
					v[2].first--;
				}
				if (k) {
					if (v[1].first) {
						str[i] = v[1].second;
						v[1].first--;
						i++;
					}
					if (v[0].first) {
						str[i] = v[0].second;
						v[0].first--;
						i++;
					}
					k--;
				}
				else {
					if (v[1].first) {
						str[i] = v[1].second;
						v[1].first--;
						i++;
					}
					else if (v[0].first) {
						str[i] = v[0].second;
						v[0].first--;
						i++;
					}
				}
			}
			if (v[0].first > 0 || v[1].first > 0 || v[2].first > 0) {
				f = false;
			}
			str[N] = 0;
		}

		printf("Case #%d: ", cs);
		if (f) {
			printf("%s\n", str);
		}
		else {
			printf("IMPOSSIBLE\n", str);
		}
	}
	return 0;
}