#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

const int INF = 9999;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		int a1, a2;
		cin >> a1 >> a2;
		vector<vector<bool> > busy(2, vector<bool>(1448));
		for (int i = 0; i < a1; i++) {
			int l, r;
			cin >> l >> r;
			for (int j = l; j < r; j++)
				busy[0][j] = 1;
		}
		for (int i = 0; i < a2; i++) {
			int l, r;
			cin >> l >> r;
			for (int j = l; j < r; j++)
				busy[1][j] = 1;
		}
		vector<vector<vector<pair<int, bool> > > > dp(722, vector<vector<pair<int, bool> > >(722, vector<pair<int, bool> >(2, { INF, 0 })));
		//dp[i][j][k] - min amount of changes to reach i and j charge time, having child with k-th parent

		dp[0][0][0] = { 0, 0 };
		dp[0][0][1] = { 0, 1 };
		for (int i = 0; i <= 1440; i++) {
			for (int q = 0; q <= min(i, 720); q++) {
				int w = i - q;
				if (w > 720)
					continue;

				if (!busy[0][q + w])
					dp[q + 1][w][0] = min(dp[q + 1][w][0], { dp[q][w][1].first + 1, dp[q][w][1].second });
				if (!busy[1][q + w])
					dp[q][w + 1][1] = min(dp[q][w + 1][1], dp[q][w][1]);

				if (!busy[0][q + w])
					dp[q + 1][w][0] = min(dp[q + 1][w][0], dp[q][w][0]);
				if (!busy[1][q + w])
					dp[q][w + 1][1] = min(dp[q][w + 1][1], { dp[q][w][0].first + 1, dp[q][w][0].second });
			}
		}
		cout << "Case #" << c + 1 << ": " << min(dp[720][720][0].first + (dp[720][720][0].second != 0), dp[720][720][1].first + (dp[720][720][1].second != 1)) << endl;
	}
	return 0;
}
