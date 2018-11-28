
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<long long> dp[19][10];
vector<long long> tidy_numbers;
long long n;

void solve() {
	cin >> n;
	if (n < 10) {
		cout << n;
		return;
	}
	vector<long long>::iterator lower = upper_bound(tidy_numbers.begin(), tidy_numbers.end(), n);
	lower--;
	cout << *lower;
}

void precalc() {
	memset(dp, 0, sizeof(dp));
	for (int i = 1; i <= 9; ++i)
		dp[1][i].push_back(i);
	long long res = 1;
	long long t = 1;
	for (int len = 2; len <= 18; ++len) {
		t *= 10;
		for (int d = 1; d <= 9; ++d) {
			dp[len][d].clear();
			for (int i = d; i <= 9; ++i) {
				for (int k = 0; k < dp[len - 1][i].size(); ++k) {
					long long next_number = t * d + dp[len - 1][i][k];
					dp[len][d].push_back(next_number);
					tidy_numbers.push_back(next_number);
				}
			}
		}
	}
	tidy_numbers.push_back(1111111111111111111LL);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	precalc();
	int t;
	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
}
