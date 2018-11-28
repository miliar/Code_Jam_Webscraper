#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Double;
char G[30][30];
pair<int, int> tl[256], br[256];
bool overlap(int i) {
	for (int j = 0; j < 26; ++j)
		if (tl[j].first != INT_MAX && j != i) {
			if (tl[i].first > br[j].first) continue;
			if (tl[j].first > br[i].first) continue;
			if (tl[i].second > br[j].second) continue;
			if (tl[j].second > br[i].second) continue;
			return true;
		}
	return false;
}
void solve(int cn) {
	int R, C;
	scanf("%d%d", &R, &C);
	for (int i = 0; i < 26; ++i) {
		tl[i] = {INT_MAX, INT_MAX};
		br[i] = {INT_MIN, INT_MIN};
	}
	int area = 0;
	for (int i = 0; i < R; ++i) {
		scanf("%s", G[i]);
		for (int j = 0; j < C; ++j) {
			int c = G[i][j] - 'A';
			pair<int, int> x = {i, j};
			if (x < tl[c]) tl[c] = x;
			if (x > br[c]) br[c] = x;
		}
	}
	for (int i = 0; i < 26; ++i) {
		if (tl[i].first != INT_MAX) {
			while (tl[i].first >= 0 && !overlap(i)) --tl[i].first;
			++tl[i].first;
			while (br[i].first < R && !overlap(i)) ++br[i].first;
			--br[i].first;
			while (tl[i].second >= 0 && !overlap(i)) --tl[i].second;
			++tl[i].second;
			while (br[i].second < C && !overlap(i)) ++br[i].second;
			--br[i].second;
		}
		for (int r = tl[i].first; r <= br[i].first; ++r)
			for (int c = tl[i].second; c <= br[i].second; ++c) {
				G[r][c] = i + 'A';
				++area;
			}
	}
	printf("Case #%d:\n", cn);
	for (int i = 0; i < R; ++i) printf("%s\n", G[i]);
//	assert(area == R * C);
}
int main() {
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		solve(cn);
	}
}

