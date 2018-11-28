#include <vector>
#include <algorithm>
#include <functional>
#include <utility>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>

using namespace std;

static const int MAXN = 1009;
static const int MAXK = 1009;
long long D[MAXN][MAXK];
long long H[MAXN][MAXK];
static const double MY_PI = 3.141592653589793238462643383;

double solve(vector<pair<int, int>>& v, int k) {
	memset(D, 0, sizeof (D));
	memset(H, 0, sizeof (H));
	int n = v.size();
	sort(v.begin(), v.end(), greater<pair<int, int>>());
	D[n - 1][1] = v[n - 1].first * 1ll * (2ll * v[n - 1].second + v[n - 1].first);
	H[n - 1][1] = v[n - 1].first * 2ll * v[n - 1].second;
	for(int i = n - 2; i >= 0; i--) {
		if(i >= n - k) {
			D[i][n - i] = v[i].first * 1ll * (2 * v[i].second + v[i].first) + H[i + 1][n - i - 1];
			H[i][n - i] = v[i].first * 2ll * v[i].second + H[i + 1][n - i - 1];
		}
		for(int j = min(n - i - 1, k); j > 0; j--) {
			//we choose i base
			long long v1 = v[i].first * 1ll * (v[i].first + 2 * v[i].second) + H[i + 1][j - 1];
			//we don't choose i base
			long long v2 = D[i + 1][j];
			D[i][j] = max(v1, v2);
			//now for H
			v1 = v[i].first * 2ll * v[i].second + H[i + 1][j - 1];
			v2 = H[i + 1][j];
			H[i][j] = max(v1, v2);
		}
	}
	return D[0][k] * MY_PI;
}

double solve2(vector<pair<int, int>>& v, int k) {
	int n = v.size();
	long long maxSum = 0;
	vector<int> maxIdx;
	for(int i = 0; i < (1 << n); i++) {
		vector<int> idx;
		for(int j = 0; j < n; j++) {
			if((i & (1 << j)) != 0) {
				idx.push_back(j);
			}
		}
		if(idx.size() == k) {
			int maxR = 0;
			long long sum = 0;
			for(int j = 0; j < (int)(idx.size()); j++) {
				maxR = max(maxR, v[idx[j]].first);
				sum += v[idx[j]].first * 2ll * v[idx[j]].second;
			}
			if(sum + maxR * 1ll * maxR > maxSum) {
				maxSum = sum + maxR * 1ll * maxR;
				maxIdx = idx;
			}
		}
	}
	return maxSum * MY_PI;
}

int main()
{
	int t;
	ifstream f("input.txt");
	FILE * g = fopen("output.txt", "wt");
	f >> t;
	for(int test = 1; test <= t; test++) {
		int n, k;
		f >> n >> k;
		vector<pair<int, int>> v(n);
		for(int i = 0; i < n; i++) {
			f >> v[i].first >> v[i].second;
		}
		double res = solve(v, k);
		if(n < 22) {
			double res2 = solve2(v, k);
			double diff = abs(res - res2);
			assert(diff < 1e-8);
		}
		fprintf(g, "Case #%d: %.9lf\n", test, res);
	}
	f.close();
	fclose(g);
	return 0;
}
