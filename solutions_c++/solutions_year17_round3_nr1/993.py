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
typedef int64_t ll;
const double eps = 1e-8;
const double dINF = 1e20;


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
		int n, k;
		cin >> n >> k;
		vector<pair<ll, ll>> cake(n);
		for (int i = 0; i < n; ++i) {
			cin >> cake[i].second >> cake[i].first;
			cake[i].first = calc1(cake[i]);
		}
		ll res = 0;
		sort(cake.begin(), cake.end(), greater<pair<ll, ll>>());
		for (int i = 0; i < n; ++i) {
			ll curr = cake[i].first + calc2(cake[i]);
			for (int j = 0; j < k - 1; ++j) {
				if (i == j) {
					curr += cake[k - 1].first;
				}
				else {
					curr += cake[j].first;
				}
			}
			res = max(res, curr);
		}
		long double resD = res * M_PI;
		cout.precision(9);
		cout << "Case #" << test << ": " << fixed << resD;
		//
		cout << endl;
		printf("%d\n", test);
	}

	return 0;

}




