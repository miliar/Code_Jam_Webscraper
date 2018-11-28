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
		int a1, a2;
		cin >> a1 >> a2;
		vector<pii> t1(a1);
		vector<pii> t2(a2);
		for (int i = 0; i < a1; ++i)
			cin >> t1[i].first >> t1[i].second;
		for (int i = 0; i < a2; ++i)
			cin >> t2[i].first >> t2[i].second;
		sort(t1.begin(), t1.end());
		sort(t2.begin(), t2.end());
		if (a1 < a2) {
			swap(a1, a2);
			swap(t1, t2);
		}

		int res = -1;
		if (a1 == 2 && a2 == 0) {
			if (t1[1].second - t1[0].first <= DAY_LEN / 2 || t1[0].second + DAY_LEN - t1[1].first <= DAY_LEN / 2)
				res = 2;
			else res = 4;
		}
		else if (a1 == 1 && a2 == 1) {
			res = 2;
		}
		else if (a1 == 1 && a2 == 0) {
			res = 2;
		}
		cout << "Case #" << test << ": " << res;
		//
		cout << endl;
		printf("%d\n", test);
	}

	return 0;

}




