// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cmath>

#define rep(i, a, b) for (int i=a;i<b;i++)
# define PI 3.14159265358979323846

using namespace std;

typedef pair<double, double> pie;

int main()
{
	ifstream reader("input.txt");
	ofstream writer("output.txt");
	int T;
	reader >> T;
	pie p[1000];
	double rest[1000];
	rep(Ti, 0, T) {
		
		int n, k;
		reader >> n >> k;
		double r, h;
		rep(i, 0, n) {
			reader >> r >> h;
			p[i].first = r * 2 * PI*h;
			p[i].second = r * r * PI;
		}
		sort(p, p + n);
		double ans = 0;
		double maxb = 0;
		for (int i = n - 1; i > n - k; i--) {
			ans += p[i].first;
			maxb = max(maxb, p[i].second);
		}
		ans += maxb;
		for (int i = n - k; i >= 0; i--) {
			rest[i] = max(0.000000, p[i].second - maxb);
			rest[i] += p[i].first;
		}
		sort(rest, rest + n - k + 1);
		ans += rest[n - k];
		writer.precision(6);
		writer << "Case #" << fixed << Ti + 1 << ": " << ans << endl;
	}

	system("pause");
	return 0;
}

