// 1b1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <climits>

using namespace std;

void conversion(double counts)
{
	std::ostringstream ss;
	ss.precision(6);
	ss << std::fixed << counts;
	std::cout << ss.str();
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	long T, lp;
	double ans;
	cin >> T;
	for (lp = 1;lp <= T;lp++)
	{
		long N, i;
		double D;
		cin >> D >> N;
		double time;
		double mxTime = 0;
		for (i = 0; i < N; i++)
		{
			double pos, spd;
			cin >> pos >> spd;
			time = (D - pos) / spd;
			mxTime = max(mxTime, time);
		}

		ans = D / mxTime;





		cout << "Case #" << lp << ": ";
		conversion(ans);
		cout << "\n";
	}





	return 0;
}

