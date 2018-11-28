#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cstring>
#include <cmath>
#include <stack>
#include <iomanip>
#define int long long
#define CONTAINS(v,n) (find((v).begin(), (v).end(), (n)) != (v).end())
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define ARY_SORT(a, size) sort((a), (a)+(size))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
using namespace std;

signed main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int D, N;
		cin >> D >> N;
		double max_hour = INT_MIN;
		for (int n = 0; n < N; n++)
		{
			int k, s;
			cin >> k >> s;
			int dis = D - k;
			double hour = dis / (double)s;
			if (hour > max_hour)
			{
				max_hour = hour;
			}
		}
		double ans = (D / max_hour);
		cout << "Case #" << (t + 1) << ": " << fixed << setprecision(7) << ans << endl;
	}
}
