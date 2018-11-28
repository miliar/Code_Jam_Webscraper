#include <climits>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;
typedef unsigned char byte;
typedef long long llong;
typedef unsigned long long ullong;
inline bool feq(const double& a, const double& b) { return fabs(a - b) < 1e-10; }
const double PI = 3.14159265358;

int dp[1441][2][721];

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		int N, K;
		double U;
		cin >> N >> K >> U;
		vector<double> ps(N);
		for (int i = 0; i < N; ++i)
			cin >> ps[i];
		sort(ps.begin(), ps.end());
		double fill = 0;
		int i = 1;
		for (; i < N; ++i)
		{
			double tmp = i * (ps[i] - ps[i - 1]);
			if (fill + tmp > U)
				break;
			fill += tmp;
		}
		double to = ps[i - 1] + (U - fill) / i;
		for (int j = 0; j < i; ++j)
			ps[j] = to;
		double res = 1;
		for (int j = 0; j < N; ++j)
			res *= ps[j];
		printf("Case #%d: %.8lf\n", t, res);
	}
	return 0;
};