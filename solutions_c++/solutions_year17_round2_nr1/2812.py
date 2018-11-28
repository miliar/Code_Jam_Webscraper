#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <memory.h>
#include <iomanip>
#include <queue>
#include <numeric>
#include <fstream>
#include <set>

using namespace std;



int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qqq;
	cin >> qqq;
	for (int qq = 0; qq < qqq; qq++)
	{
		cout << "Case #" << qq + 1 << ": ";
		if (qq == 50)
		{
			int u = 0;
			u++;
		}
		long double d;
		long long n;
		cin >> d >> n;
		long double maxtime = 0;
		for (int i = 0; i < n; i++)
		{
			long double x, s;
			cin >> x >> s;
			long double time = (d - x) / s;
			maxtime = max(maxtime, time);
		}
		long double ans = d / maxtime;

		cout << fixed << setprecision(9) << ans << endl;
	}
}