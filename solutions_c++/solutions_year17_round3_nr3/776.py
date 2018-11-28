#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <algorithm>
#include <string>
#include <memory.h>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <queue>
#include <numeric>
#include <math.h>
#include <fstream>
#include <set>

using namespace std;

#define PI 3.14159265358979323846264338327950288419716939937510

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qqq;
	cin >> qqq;
	for (int qq = 0; qq < qqq; qq++)
	{
		cout << "Case #" << qq+1 << ": ";
		/*int ac, aj;
		cin >> ac >> aj;
		vector <int> ans(1421,0);
		int cleft = 720, jleft = 720;
		for (int i = 0; i < ac; i++)
		{
			int st, fin;
			cin >> st >> fin;
			for (int j = st; j < fin; j++)
			{
				ans[j] = 2;
			}
		}
		for (int i = 0; i < aj; i++)
		{
			int st, fin;
			cin >> st >> fin;
			for (int j = st; j < fin; j++)
			{
				ans[j] = 1;
			}
		}
		int dp[1421][721][721][2];
		dp[0][0][0][0] = 0;
		dp[0][0][0][1] = 1;
		for (int i=1;i<1421;i++)
		{
			for (int c=0;c<=720;c++)
			{
				int j = i - c;
				if (j >= 0)
				{

					if (ans[i] == 1)
					{
						dp[i][c][j][0] = dp[i][c - 1][j][0];

						dp[i][c][j][0] = min(dp[i - 1][c-1][j][0]])
					}
				}

	*/

		int n, k;
		cin >> n >> k;
		vector <long double > pr;
		long double u;
		cin >> u;
		long double maxp = 0;
		for (int i = 0; i < n; i++)
		{
			long double x;
			cin >> x;
			pr.push_back(x);
			maxp = max(maxp, x);
		}
		long double l = 0, r = 1;
		int tryes = 0;
		while (r - l > 1e-9 && tryes < 5000)
		{
			tryes++;
			long double mid = (r + l) / 2;
			long double need = 0;
			for (auto x : pr)
			{
				if (x < mid)
				{
					need += mid - x;
				}
			}
			if (need > u)
			{
				r = mid;
			}
			else
			{
				l = mid;
			}
		}
		long double p = 1.0;
		for (int i = 0; i < n; i++)
		{
			if (pr[i] < r)
			{
				p *= r;
			}
			else
			{
				p *= pr[i];
			}
		}
		cout << fixed << setprecision(10) << p << endl;

	}




}