// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cmath>

#define rep(i, a, b) for (int i=a;i<b;i++)

using namespace std;


int main()
{
	ifstream reader("input.txt");
	ofstream writer("output.txt");
	int T;
	reader >> T;
	double p[50];
	rep(Ti, 0, T) {
		
		int n;
		reader >> n >> n;
		double t;
		reader >> t;
		rep(i, 0, n) {
			reader >> p[i];
		}
		sort(p, p + n);
		double maxadd;
		int i = 0;
		while (i<n) {
			int j = i+1;
			while (j < n && p[j] == p[i]) j++;
			if (j < n) maxadd = p[j] - p[i]; else maxadd = 1 - p[i];
			double maxpadd = t / j;
			double add = min(maxadd, maxpadd);
			rep(k, 0, j) p[k] += add;
			t = t - add * j;
			i = j;
		}
		double ans = 1;
		rep(i, 0, n)
		{
			ans *= p[i];
		}
		writer.precision(6);
		writer << "Case #" << fixed << Ti + 1 << ": " << ans << endl;
	}

	system("pause");
	return 0;
}

