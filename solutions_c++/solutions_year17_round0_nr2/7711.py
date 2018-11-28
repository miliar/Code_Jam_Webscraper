#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#define INF 1000000000

using namespace std;

typedef long long lon;
typedef pair<lon, lon> ll;
typedef pair<lon, ll> lll;
typedef vector<lon> vl;
typedef vector<ll> vll;
typedef vector<lll> vlll;

int main() {
	int nCases;
	cin >> nCases;
	for (int cnum = 1; cnum <= nCases; cnum++) {
		lon N;
		cin >> N;
		lon solution;
		for (lon i = N; i >= 0; i--) {
			lon num = i;
			lon tidy = 1;
			lon dig = 9;
			while (num > 0) {
				lon cur = num % 10;
				if (cur > dig) tidy = 0;
				num = num / 10;
				dig = cur;
			}
			if (tidy) {
				solution = i;
				break;
			}
		}
		cout << "Case #" << cnum << ": " << solution << endl;
	}
}
