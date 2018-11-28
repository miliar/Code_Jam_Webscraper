#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <string>
#include <map>
using namespace std;

void solve(int test) {
	int N, M;
	cin >> N >> M;
	string s = "";
	for (int i = 0; i < N; ++i) {
		s += '.';
	}
	vector<string> d(N), d1(N), d2(N);
	vector<vector<bool> > used1(N), used2(N), usedAll(N);
	for (int i = 0; i < N; ++i) {
		d[i] = s;
		d1[i] = s;
		d2[i] = s;
		used1[i].resize(N);
		used2[i].resize(N);
		usedAll[i].resize(N);
	}
	int cnt = 0;
	for (int i = 0; i < M; ++i) {
		char c;
		int x, y;
		cin >> c >> x >> y;
		x--, y--;
		d[x][y] = c;
		if (c == '+') {
			cnt++;
			d1[x][y] = c;
			for (int t = 0; t < N; ++t) {
				if (x - t >= 0 && y - t >= 0) {
					used1[x - t][y - t] = true;
				}
				if (x - t >= 0 && y + t < N) {
					used1[x - t][y + t] = true;
				}
				if (x + t < N && y - t >= 0) {
					used1[x + t][y - t] = true;
				}
				if (x + t < N && y + t < N) {
					used1[x + t][y + t] = true;
				}
			}
		}
		else if (c == 'x') {
			cnt++;
			d2[x][y] = c;
			for (int t = 0; t < N; ++t) {
				if (x - t >= 0) {
					used2[x - t][y] = true;
				}
				if (x + t < N) {
					used2[x + t][y] = true;
				}
				if (y - t >= 0) {
					used2[x][y - t] = true;
				}
				if (y + t < N) {
					used2[x][y + t] = true;
				}
			}
		}
		else {
			cnt+=2;
			d1[x][y] = '+';
			d2[x][y] = 'x';
			for (int t = 0; t < N; ++t) {
				if (x - t >= 0 && y - t >= 0) {
					used1[x - t][y - t] = true;
				}
				if (x - t >= 0 && y + t < N) {
					used1[x - t][y + t] = true;
				}
				if (x + t < N && y - t >= 0) {
					used1[x + t][y - t] = true;
				}
				if (x + t < N && y + t < N) {
					used1[x + t][y + t] = true;
				}
				if (x - t >= 0) {
					used2[x - t][y] = true;
				}
				if (x + t < N) {
					used2[x + t][y] = true;
				}
				if (y - t >= 0) {
					used2[x][y - t] = true;
				}
				if (y + t < N) {
					used2[x][y + t] = true;
				}
			}
		}
	}
	int add = 0;
	int x = 0, y = 0, npx = 1, npy = 0, ccnt = 0;
	while (ccnt < N * N) {
		ccnt++;
		usedAll[x][y] = true;
		int addNow = 0;
		if (!used1[x][y]) {
			cnt++;
			addNow++;
			d1[x][y] = '+';
			for (int t = 0; t < N; ++t) {
				if (x - t >= 0 && y - t >= 0) {
					used1[x - t][y - t] = true;
				}
				if (x - t >= 0 && y + t < N) {
					used1[x - t][y + t] = true;
				}
				if (x + t < N && y - t >= 0) {
					used1[x + t][y - t] = true;
				}
				if (x + t < N && y + t < N) {
					used1[x + t][y + t] = true;
				}
			}
		}
		if (!used2[x][y]) {
			cnt++;
			addNow++;
			d2[x][y] = 'x';
			for (int t = 0; t < N; ++t) {
				if (x - t >= 0) {
					used2[x - t][y] = true;
				}
				if (x + t < N) {
					used2[x + t][y] = true;
				}
				if (y - t >= 0) {
					used2[x][y - t] = true;
				}
				if (y + t < N) {
					used2[x][y + t] = true;
				}
			}
		}
		if (addNow > 0) {
			add++;
		}
		if (x + npx >= 0 && x + npx < N && y + npy >= 0 && y + npy < N && !usedAll[x + npx][y + npy]) {
			x += npx;
			y += npy;
		}
		else {
			if (npx == 1) {
				npx = 0;
				npy = 1;
			}
			else if (npy == 1) {
				npx = -1;
				npy = 0;
			}
			else if (npx == -1) {
				npx = 0;
				npy = -1;
			}
			else {
				npx = 1;
				npy = 0;
			}
			x += npx;
			y += npy;
		}
	}
	printf("Case #%d: %d %d\n", test, cnt, add);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			char curCh = '.';
			if (d1[i][j] == '+')
				curCh = '+';
			if (d2[i][j] == 'x') {
				if (curCh == '+')
					curCh = 'o';
				else
					curCh = 'x';
			}
			if (curCh != d[i][j]) {
				cout << curCh << " " << i + 1 << " " << j + 1 << endl;
			}
		}
	}
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
		solve(i + 1);
	return 0;
}