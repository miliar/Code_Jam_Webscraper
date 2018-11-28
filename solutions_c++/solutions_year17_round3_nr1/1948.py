#include <iostream>
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
#include <functional>

using namespace std;
#pragma warning(disable:4996)

int T, N, K;
const double PI = 3.14159265358979323846;

double cache[1001][1001];

bool pred(const pair<double, double>& a, const pair<double, double>& b) {
	if (a.first > b.first) return true;
	else if (a.first <= b.first) return false;
	else {
		if (a.second > b.second) return true;
		else if (a.second <= b.second) return false;
	}
}

double solve(const vector<pair<double, double> >& cakes, int i, int k) {
	if (k == 0) return 0;
	if (N- i  < k) return -1;

	double& ret = cache[i][k];
	if (ret != -1) return ret;

	ret = -1;

	double ans_a = solve(cakes, i+1, k);
	double ans_b = solve(cakes, i + 1, k - 1);
	if(ans_b != -1)
		ans_b = cakes[i].first * cakes[i].second * PI * 2 + solve(cakes, i + 1, k - 1);
	ret = max(ans_a, ans_b);
	return ret;
}

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("ans.txt", "w", stdout);
	cout.precision(9);
	cout << fixed;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> N >> K;
		for (int i = 0; i < 1001; ++i) 
			for (int j = 0; j < 1001; ++j)
				cache[i][j] = -1;
		
		vector<pair<double, double> > cakes;
		double a, b;
		for (int n = 0; n < N; ++n) {
			cin >> a >> b;
			cakes.push_back(make_pair(a, b));
		}

		sort(cakes.begin(), cakes.end(), pred);

		int size = cakes.size();

		double ret = 0;
		for (int i = 0; i < size; ++i) {
			double ans = cakes[i].first * cakes[i].first * PI;
			double sub = solve(cakes, i + 1, K - 1);
			if (sub == -1) continue;
			ret = max(ret, ans + sub + cakes[i].first * cakes[i].second * PI * 2);
		}

		cout << "Case #" << t + 1 << ": ";
		cout << ret << endl;
	}
}