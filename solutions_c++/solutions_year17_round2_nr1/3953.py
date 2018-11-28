#include <fstream>
#ifdef ONLINE_JUDGE
#define cin in
#define cout out
#endif
#include <algorithm>
#include <iostream>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <set>
#include <string>
#include <map>
#define M_PI 3.14159265358979323846
#include <cmath>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <bitset>
#include <cfloat>
#include <queue>
#include <climits>
using namespace std;

const size_t MAX = 100 + 2;

uint64_t gcd(uint64_t a, uint64_t b)
{
	return b ? gcd(b, a%b) : a;
}

void floyd_warshall(int32_t(*arr)[MAX], int32_t n) {
	for (int32_t k = 0; k < n; ++k)
		for (int32_t i = 0; i < n; ++i)
			for (int32_t j = 0; j < n; ++j)
				arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
}

int main(int argc, char *argv[])
{
	ios_base::sync_with_stdio(false);
	ifstream in("input.txt");
	ofstream out("output.txt");
	int32_t tests, d, n, k, s;
	double time = 0;
	cin >> tests;
	for (int32_t t = 1; t <= tests; ++t) {
		cin >> d >> n;
		vector<pair<double, double>> horses(n);
		for (int32_t i = 0; i < n; ++i) {
			cin >> horses[i].first >> horses[i].second;
		}
		sort(horses.begin(), horses.end());
		time = 0;
		for (int32_t i = n - 1; i >= 1; --i) {
			double k2 = horses[i].first;
			double k1 = horses[i - 1].first;
			double s2 = horses[i].second;
			double s1 = horses[i - 1].second;
			double f = double(k2*s1 - s2*k1) / (s1 - s2);
			if (s1 > s2 && f <= d) {
				horses[i - 1].first = f;
				horses[i - 1].second = s2;
				time += double(k2 - k1) / (s1 - s2);
			}
			else {
				horses[i - 1].first = k1 + s1 * double(d - k2) / s2;
				time += double(d - k2) / s2;
			}
		}
		double timeForFirst = double(d - horses[0].first) / horses[0].second;
		cout << setprecision(6) << fixed << "Case #" << t << ": " << d / (time + timeForFirst) << endl;
	}
	return 0;
}