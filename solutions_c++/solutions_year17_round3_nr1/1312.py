#define _USE_MATH_DEFINES
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

int r[1000];
int h[1000];

signed main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N, K;
		cin >> N >> K;
		for (int i = 0; i < N; i++)
		{
			cin >> r[i] >> h[i];
		}

		vector<int> v;
		for (int i = 0; i < N; i++)
		{
			v.push_back(i);
		}

		int max_d = 0;
		do
		{
			int max_r = 0;
			int sum_h = 0;
			for (int i = 0; i < K; i++)
			{
				int ind = v[i];
				max_r = MAX(r[ind], max_r);
				sum_h += 2 * r[ind] * h[ind];
			}
			int d = max_r * max_r + sum_h;
			if (max_d < d)
			{
				max_d = d;
			}
		} while (next_permutation(v.begin(), v.end()));

		double ans = (max_d) * M_PI;
		cout << "Case #" << (t+1) << ": " << fixed << setprecision(10) << ans << endl;
	}
}
