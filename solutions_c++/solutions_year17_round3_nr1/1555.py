#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cmath>

#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;



void main() {
	int nTests;

	cin >> nTests;  // read t. cin knows that t is an int, so it reads it as such.
	for (int testCase = 1; testCase <= nTests; ++testCase) {
		int N;
		int K;
		cin >> N;
		cin >> K;

		multimap<int, int> cakes;
		for (int i = 0; i < N; i++) {
			int R;
			int H;
			cin >> R;
			cin >> H;
			cakes.insert(make_pair(R, H));
		}

		while ((int)cakes.size() > K) {
			long double minCake = 1e14;

			multimap<int, int>::reverse_iterator cake = cakes.rbegin();
			multimap<int, int>::reverse_iterator minIter = cake;
			for (; cake != cakes.rend(); cake++) {
				long double temp = 0.0;
				if (cake == cakes.rbegin()) {
					temp = 2 * M_PI * cake->first * cake->second + M_PI * cake->first*cake->first;
					multimap<int, int>::reverse_iterator next = cake; next++;
					if (next != cakes.rend()) {
						temp = temp - M_PI * next->first*next->first;
					}
				}
				else {
					temp = 2 * M_PI * cake->first * cake->second;
				}
				if (minCake > temp) {
					minCake = temp;
					minIter = cake;
				}
			}

			for (multimap<int, int>::iterator iter = cakes.begin(); iter != cakes.end(); iter++) {
				if (iter->first == minIter->first && iter->second == minIter->second) {
					cakes.erase(iter);
					break;
				}
			}
		}

		multimap<int, int>::reverse_iterator cake = cakes.rbegin();
		long double ans = 2 * M_PI * cake->first * cake->second + M_PI * cake->first*cake->first;
		cake++;
		for (; cake != cakes.rend(); cake++) {
			ans += 2 * M_PI * cake->first * cake->second;
		}
		cout.precision(10);
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}
