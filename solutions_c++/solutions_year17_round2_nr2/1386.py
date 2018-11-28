#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <string>

using namespace std;

vector<string> uns = { "R", "O", "Y", "G", "B", "V" };
double calcInter(int x1, int x2, int v1, int v2)
{
	if (x1 == x2) return 0;
	if (v2 <= v1) return INT_MAX;
	return 1.0 * (x1 - x2) / (v2 - v1);
}
int main() {
	freopen("B-small-attempt4.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) 
	{
		int n, r, o, y, g, b, v;
		vector<int> colors;
		cin >> n;
		for (int i = 0; i < 6; i++)
		{
			int tt;
			cin >> tt;
			colors.push_back(tt);
		}
		bool ans = false;
		string res;
		int prev = -1;
		for (int i = 0; i < n; i++)
		{
			int idx = -1;
			for (int j = 0; j < 6; j++)
			{
				if (colors[j] > 0 && j != prev)
					idx = j;
			}
			if (idx == -1)
			{
				res = "Impossible";
				break;
			}
			for (int j = 0; j < 6; j++)
			{
				if (colors[j] > 0 && colors[j] > colors[idx] && j != prev)
					idx = j;
			}
			colors[idx]--;
			prev = idx;
			res += uns[idx];
		}
		if (res != "Impossible") for (int i = 1; i < n; i++)
		{
			if (res[i] == res[i - 1])
			{
				res = "Impossible";
				break;
			}
		}
		if (res != "Impossible" && res[0] == res[n - 1])
		{
			bool art = false;
			for (int i = 1; i < n - 1; i++)
			{
				if (res[i] != res[0] && (i == n - 2 || res[i] != res[n - 2]))
					if (i - 1 == n - 1 || res[i - 1] != res[n - 1])
						if (i + 1 == n - 1 || res[i + 1] != res[n - 1])
						{
							swap(res[i], res[n - 1]);
							art = true;
							break;
						}
			}
			if (!art) res = "Impossible";
		}
			

		cout << "Case #" << test << ": " << res << endl;
	}
}