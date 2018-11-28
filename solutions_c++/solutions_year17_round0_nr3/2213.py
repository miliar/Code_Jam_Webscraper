#define _CRT_SECURE_NO_WARNINGS
#include <iostream> 
#include <vector>
#include <algorithm>
#include <map> 
#include <string>
#include <set> 
#include <iterator> 
#include <deque>
#include <iomanip>
#include <string> 
#include <math.h> 
#include <time.h>
#include <queue> 
#include <stdio.h>
#include <valarray>
#include <stack>

#define mp(x, y) make_pair(x, y)
#define all(x) x.begin(), x.end() 
#define det(a, b, c, d) a*d - b*c

typedef long long ll;

using namespace std;


struct cmp {
	bool operator()(const ll & a, const ll& b) const {
		return a > b;
	}
};
int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		ll n, k;
		cin >> n >> k;
		map<ll, ll, cmp> m;
		m[n] = 1;
		ll aMax = 0, aMin = 0;
		while (k > 0) {
			auto curr = m.begin();
			ll curLen = curr->first;
			if (curLen % 2 == 1) {
				curLen--;
				aMax = aMin = curLen / 2;
				m[curLen / 2] += 2*curr->second;
			}
			else {
				aMax = curLen / 2;
				aMin = curLen - curLen / 2 - 1;
				m[aMax]+= curr->second;
				m[aMin]+= curr->second;
			}
			k -= curr->second;
			m.erase(curr);
		}
		cout << "Case #" << i + 1 << ": " << aMax << ' ' << aMin << endl;
	}
	return 0;
}
