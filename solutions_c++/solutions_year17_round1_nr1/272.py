#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
char arr[27][27];
pair<int, int> init[26];
vector<char> chars;

void go(int i, int j, int pj, char c) {
	int downlmt = i, uplmt = i;
	for (int k = i + 1; k < n; ++k) {
		if (arr[k][j] == '?') {
			arr[k][j] = c;
			downlmt = k;
		}
		else {
			break;
		}
	}
	for (int k = i - 1; k >= 0; --k) {
		if (arr[k][j] == '?') {
			arr[k][j] = c;
			uplmt = k;
		}
		else {
			break;
		}
	}

	for (int b = pj + 1; b <= j; ++b) {
		for (int k = uplmt; k <= downlmt; ++k) {
			arr[k][b] = c;
		}
	}
}

void proc(int caseidx) {
	for (int i = 0; i < 26; ++i) {
		init[i] = { -1, -1 };
	}
	chars.clear();

	scanf("%d %d ", &n, &m);
	for (int i = 0; i < n; ++i) {
		scanf("%s", arr[i]);
		for (int j = 0; j < m; ++j) {
			if (arr[i][j] != '?') {
				init[arr[i][j] - 'A'] = { i, j };
				chars.push_back(arr[i][j]);
			}
		}
	}

	int pj = -1;
	for (int j = 0; j < m; ++j) {
		bool updated = false;
		for (int i = 0; i < n; ++i) {
			if (arr[i][j] != '?') {
				go(i, j, pj, arr[i][j]);
				updated = true;
			}
		}
		if (updated) pj = j;
	}

	for (int j = pj + 1; j < m; ++j) {
		for (int i = 0; i < n; ++i) {
			arr[i][j] = arr[i][pj];
		}
	}

	printf("Case #%d:\n", caseidx);
	for (int i = 0; i < n; ++i) {
		printf("%s\n", arr[i]);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}