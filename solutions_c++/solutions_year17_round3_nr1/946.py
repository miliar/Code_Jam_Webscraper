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

		long long k, n;
		cin >> n >> k;
		vector <pair <long double, long double> >  pancakes;
		for (int i = 0; i < n; i++)
		{
			long long r, h;
			cin >> r >> h;
			pancakes.push_back(make_pair((r*h), r));
		}
		sort(pancakes.begin(), pancakes.end());
		reverse(pancakes.begin(), pancakes.end());
		long double ans = 0;
		long double maxr = -1;
		for (int i = 0; i < k; i++)
		{
			maxr = max(maxr, pancakes[i].second);
			ans += 2 * pancakes[i].first;
		}
		ans += maxr * maxr;
		long double bestans = ans;
		for (int i = k; i < n; i++)
		{
			if (pancakes[i].second >= maxr)
			{
				ans -= pancakes[k - 1].first  * 2;
				ans -= maxr*maxr ;
				ans += pancakes[i].second * pancakes[i].second ;
				ans += pancakes[i].first  * 2;
				if (ans >= bestans)
					bestans = ans;
				ans += pancakes[k - 1].first  * 2;
				ans += maxr*maxr ;
				ans -= pancakes[i].second * pancakes[i].second ;
				ans -= pancakes[i].first  * 2;
			}
		}
		cout << fixed << setprecision(30) << PI*bestans << endl;







	}




}