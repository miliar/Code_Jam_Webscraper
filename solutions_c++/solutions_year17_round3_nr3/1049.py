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

const int A = 10000000000;

signed main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N, K;
		cin >> N >> K;
		double uu;
		cin >> uu;
		int U = uu * A;
		int P[50];
		for (int i = 0; i < N; i++)
		{
			double pp;
			cin >> pp;
			P[i] = pp * A;
		}

		ARY_SORT(P, N);

		while (U > 0)
		{
			int min_cnt = 1;
			int next = -1;
			for (int i = 1; i < N; i++)
			{
				if (P[i] == P[0])
				{
					min_cnt++;
				}
				else
				{
					next = P[i];
					break;
				}
			}

			if (next == -1)
			{
				for (int i = 0; i < N; i++)
				{
					P[i] += U / N;
				}
				U = 0;
			}
			else
			{
				int need = MIN(U, (next - P[0]) * min_cnt);
				for (int i = 0; i < min_cnt; i++)
				{
					P[i] += need / min_cnt;
				}
				U -= need;
			}
		}

		double ans = 1.0;
		for (int i = 0; i < N; i++)
		{
			ans *= P[i] / (double)A;
		}
		cout << fixed << setprecision(10) << "Case #" << (t + 1) << ": " << ans << endl;
	}
}
