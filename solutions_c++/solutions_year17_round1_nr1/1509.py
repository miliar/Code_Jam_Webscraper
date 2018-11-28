#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

#define REP(i, a, b)		for(i = (a); i <= (b); i++)
#define FOR(i, N)			REP(i, 0, N-1)

#define REPI(it, a, b)		for(it = (a); it != (b); it++)
#define FORI(it, v)			REPI(it, All(v))

#define All(v)				v.begin(), v.end()

#define VI					vector<int>
#define VS					vector<string>

#define II					pair<int, int>
#define VII					vector<II>

int main() {
	ifstream cin("input2.txt");
	ofstream cout("output1a.txt");
	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i, j, k;
		int R, C;
		cin >> R >> C;

		VS cake(R);
		FOR(i, R) cin >> cake[i];

		VII pre;
		FOR(i, R) FOR(j, C) if (cake[i][j] != '?')
			pre.push_back(II(i, j));

		FOR(k, pre.size()) {
			int r = pre[k].first;
			int c = pre[k].second;
			int cc = c-1;
			while (cc >= 0 && cake[r][cc] == '?')
				cake[r][cc--] = cake[r][c];
			cc = c+1;
			while (cc < C && cake[r][cc] == '?')
				cake[r][cc++] = cake[r][c];
		}

		FOR(i, R) if (cake[i][0] != '?')
			break;

		FOR(j, i)
			cake[j] = cake[i];
		REP(j, i + 1, R - 1) if (cake[j][0] == '?')
			cake[j] = cake[j - 1];

		cout << "Case #" << t << ":" << endl;
		FOR(i, R) cout << cake[i] << endl;
	}
}