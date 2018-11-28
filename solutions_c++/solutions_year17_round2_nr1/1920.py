#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <limits>
#include <functional>
#include <iomanip>
#include <fstream>

using namespace std;
typedef long long ll;
typedef long double ld;
int const INF = numeric_limits<int>::max();


int main()
{
	ios::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		ld mxtime = 0;
		ld d;
		int n;
		cin >> d >> n;
		for (int i = 0; i < n; i++)
		{
			ld k, s;
			cin >> k >> s;
			mxtime = max(mxtime, (d - k) / s);
		}
		cout << "Case #" << test << ": " << fixed << setprecision(10) << d / mxtime << endl;
	}
	return 0;
}

