#pragma comment(linker, "/STACK:256000000")
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include <set>
#include <queue>
#include <map>
#include <vector>
#include <ctime>

using namespace std;

#define mp make_pair
#define con continue
typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector < vector < int> > vvi;
typedef vector < vector < pair < int, int > > > vvii;

const double PI = 3.141592653589793238462;

int t, n, k;
double r, h;
double ans;

pair < double, double >  A[1010];
pair <double, int > B[1010];

int main()
{
	freopen("A-large (1).in", "r", stdin); freopen("output.txt", "w", stdout);
	cin >> t;
	for (int q = 0; q < t; ++q)
	{
		cin >> n >> k;
		for (int i = 0; i < 1000; ++i)
		{
			A[i].first = 0;
			A[i].second = 0;
			B[i].first = 0;
			B[i].second = 0;
		}

		ans = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> r >> h;
			A[i].first = r;
			A[i].second = h;
			B[i].first = 2 * PI * r * h;
			B[i].second = i;
		}
		sort(B, B + n);
		reverse(B, B + n);
		for (int i = 0; i < n; ++i)
		{
			double cur_ans = 0;
			cur_ans += PI * A[i].first * A[i].first + 2 * PI * A[i].first * A[i].second;
			int w = 1;
			for (int j = 0; j < n; ++j)
			{
				int e = B[j].second;
				if (A[e].first <= A[i].first && e != i)
				{
					if (w < k)
					{
						cur_ans += B[j].first;
						w++;
					}
					if (w >= k)
						break;
				}
			}
			if (w >= k)
				if (ans < cur_ans)
					ans = cur_ans;
		}

		printf("Case #%d: %.10lf\n", q + 1, ans);
	}
	return 0;
}