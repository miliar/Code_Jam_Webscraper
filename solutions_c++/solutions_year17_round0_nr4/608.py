#include <iostream>
#include <string>
using namespace std;
typedef long long ll;

void output(int num, ll arg1, ll arg2) {
	cout << "Case #" << num << ": " << arg1 << " " << arg2 << endl;
}

int get_score(int c[101][101], int n) {
	int score = 0;
	for (int j = 1; j <= n; j++)
		for (int k = 1; k <= n; k++)
			if (c[j][k] == 3) score += 2;
			else if (c[j][k] == 2) score += 1;
			else if (c[j][k] == 1) score += 1;

	return score;
}

int count_change(int cb[101][101], int ca[101][101], int n) {
	int cnt = 0;
	for (int j = 1; j <= n; j++)
		for (int k = 1; k <= n; k++)
			cnt += (cb[j][k] == ca[j][k]) ? 0 : 1;

	return cnt;
}
void output_change(int cb[101][101], int ca[101][101], int n) {
	for (int j = 1; j <= n; j++)
		for (int k = 1; k <= n; k++)
			if (cb[j][k] != ca[j][k]) {
				char c = ca[j][k] == 1 ? '+' : ca[j][k] == 2 ? 'x' : 'o';
				printf_s("%c %d %d\n", c, j, k);
			}
}

void solve(int num, int n, int m, int c[101][101]) {

	int ca[101][101] = {};
	for (int j = 1; j <= n; j++) {
		for (int k = 1; k <= n; k++) {
			ca[j][k] = c[j][k];
		}
	}

	// set asterisk
	for (int j = 1; j <= n; j++) {
		for (int k = 1; k <= n; k++) {
			ca[j][0] |= c[j][k];
			ca[0][k] |= c[j][k];
		}
	}

	for (int j = 1, k = 1; j <= n; j++) {
		if (ca[j][0] & (1 << 1))continue;
		for (; k <= n; k++) {
			if (ca[0][k] & (1 << 1))continue;
			else {
				ca[j][k] |= (1 << 1); k++;
				break;
			}
		}
	}

	// set cross
	int sum[201] = {}, diff[201] = {};
	const int OFFSET_DIFF = 100;
	for (int j = 1; j <= n; j++) {
		for (int k = 1; k <= n; k++) {
			sum[j+k] |= c[j][k];
			diff[j-k+OFFSET_DIFF] |= c[j][k];
		}
	}

	for (int j = 1; j <= 1; j++) {
		for (int k = 1; k <= n; k++) {
			if ((sum[j + k] & 1) != 0) continue;
			if ((diff[j - k + OFFSET_DIFF] & 1) != 0) continue;
			ca[j][k] |= (1 << 0);
			sum[j + k] |= (1 << 0);
			diff[j - k + OFFSET_DIFF] |= (1 << 0);
		}
	}
	for (int j = n; j <= n; j++) {
 		for (int k = 1; k <= n; k++) {
			if ((sum[j + k] & 1) != 0) continue;
			if ((diff[j - k + OFFSET_DIFF] & 1) != 0) continue;
			ca[j][k] |= (1 << 0);
			sum[j + k] |= (1 << 0);
			diff[j - k + OFFSET_DIFF] |= (1 << 0);
		}
	}

	output(num, get_score(ca, n), count_change(c, ca, n));
	output_change(c, ca, n);
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int c[101][101] = {};
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < m; i++) {
			char d; int ci, ri;
			cin >> d >> ci >> ri;
			c[ci][ri] = (d == '+') ? 1 : (d == 'x') ? 2 : 3;
		}

		solve(i, n, m, c);
	}
}