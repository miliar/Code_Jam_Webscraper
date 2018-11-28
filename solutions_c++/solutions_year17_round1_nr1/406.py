#include <bits/stdc++.h>
using namespace std;

#define max2(a,b) a<b?b:a

int T;
int n, m;

int visa[30];
int existname[30];

char stra[30][30];
char strb[30][30];

vector<char> veca[30];

struct pii {
	int begina;
	int enda;
	int beginn;
	int endn;
};

map<char, pii> mapa;

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &n);
		scanf("%d", &m);
		memset(visa, 0, sizeof(visa));
		memset(existname, 0, sizeof(existname));

		mapa.clear();
		for (int i = 1; i <= n; i++) {
			veca[i].clear();
		}

		for (int i = 1; i <= n; i++) {
			scanf("%s", stra[i]);
			for (int j = 0; j < m; j++) {
				if (stra[i][j] != '?') {
					existname[i] = 1;
					break;
				}
			}
		}

		int flag0 = 1;
		while (flag0) {
			flag0 = 0;
			for (int i = 1; i <= n; i++) {
				if (visa[i])
					continue;
				flag0 = 1;
				if (existname[i]) {

					int begina = -1;
					char nowname;
					for (int j = 0; j < m; j++) {
						if (stra[i][j] != '?') {
							if (begina != -1) {
								pii tp;
								tp.begina = begina;
								tp.enda = j - 1;
								tp.beginn = i;
								tp.endn = i;
								mapa[nowname] = tp;
								begina = j;
								veca[i].push_back(nowname);
								nowname = stra[i][j];
							} else {
								nowname = stra[i][j];
								begina = 0;
							}
						}
						if (j == m - 1) {
							if (begina != -1) {
								pii tp;
								tp.begina = begina;
								tp.enda = j;
								tp.beginn = i;
								tp.endn = i;
								mapa[nowname] = tp;
								veca[i].push_back(nowname);
							}
						}

					}
					visa[i] = 1;

				} else {
					if ((!visa[i - 1]) && (!visa[i + 1])) {
						continue;
					}

					visa[i] = 1;

					if (visa[i - 1]) {
						for (char au : veca[i - 1]) {
							if (i < mapa[au].beginn) {
								mapa[au].beginn--;
							}
							if (i > mapa[au].endn) {
								mapa[au].endn++;
							}

							veca[i].push_back(au);
						}
					} else {
						for (char au : veca[i + 1]) {
							if (i < mapa[au].beginn) {
								mapa[au].beginn--;
							}
							if (i > mapa[au].endn) {
								mapa[au].endn++;
							}

							veca[i].push_back(au);
						}
					}

				}
			}
		}

//		for (auto au : mapa) {
//			cout << au.first << "  " << au.second.begina << "  "
//					<< au.second.enda << "  " << au.second.beginn << "  "
//					<< au.second.endn << endl;
//		}
//		cout << endl;

		for (int i = 1; i <= n; i++) {
			strb[i][m] = 0;
		}
		for (auto au : mapa) {
			for (int i = au.second.beginn; i <= au.second.endn; i++) {
				for (int j = au.second.begina; j <= au.second.enda; j++) {
					strb[i][j] = au.first;
				}
			}
		}

		printf("Case #%d:\n", t);
		for (int i = 1; i <= n; i++) {
			puts(strb[i]);
		}
	}

	return 0;
}
