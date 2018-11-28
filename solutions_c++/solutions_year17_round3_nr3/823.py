#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <cmath>	
#include <vector>
#include <stack>
#include <bitset>
#include <functional>
#include <math.h>


using namespace std;

const int INF = 2 * (int)1e9;
typedef pair<int, int> pii;
typedef int64_t ll;
const double eps = 1e-10;
const double dINF = 1e20;


const int DAY_LEN = 1440;
#define cout out
#define cin in

ll calc1(pair<ll, ll> a) {
	return 2 * a.second * a.first;
}
ll calc2(pair<ll, ll> a) {
	return  a.second * a.second;
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int ntest;
	cin >> ntest;
	for (int test = 1; test <= ntest; ++test) {
		/*int a1, a2;
		cin >> a1 >> a2;
		vector<pii> t1(a1);
		vector<pii> t2(a2);
		for (int i = 0; i < a1; ++i)
			cin >> t1[i].first >> t1[i].second;
		for (int i = 0; i < a2; ++i)
			cin >> t2[i].first >> t2[i].second;

		int res1 = 0, res2 = 0;
		for (int i = 0; i < a2; ++i)
			res1 += t2[i].second - t2[i].first;
		for (int i = 0; i < a1; ++i)
			res2 += t1[i].second - t1[i].first;
		int rem = DAY_LEN - res1 - res2;*/
		int n, k;
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> p(n);
		for (int i = 0; i < n; ++i) {
			cin >> p[i];
		}
		long double l = 0, r = 1;
		while (fabs(r - l) > eps) {
			long double mid = (l + r) / 2;
			double c_u = 0;
			for (int i = 0; i < n; ++i)
				if (p[i] < mid)
					c_u += mid - p[i];
			if (c_u > u)
				r = mid;
			else l = mid;
		}
		double lim = (l + r) / 2;
		vector<double> p1(n);
		for (int i = 0; i < n; ++i) {
			if (p[i] < lim)
				p1[i] = lim;
			else p1[i] = p[i];
		}
		long double res = 1;
		for (int i = 0; i < n; ++i)
			res *= p1[i];
		cout.precision(9);
		cout << "Case #" << test << ": " << fixed << res;
		//
		cout << endl;
		printf("%d\n", test);
	}

	return 0;

}




