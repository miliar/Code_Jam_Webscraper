#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <tuple>
#include <queue>
#include <utility>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <new>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <chrono>
#include <thread>

const double pi = 3.1415926535897932384626433832795;

using namespace std;

typedef long long ll;

int main(void) {
	cin.tie(nullptr);
	cin.sync_with_stdio(false);

	int t;
	cin >> t;
	for (int c = 1; c <= t; c++) {
		string S;
		int k;
		cin >> S >> k;
		int flips = 0;
		for (int i = 0; i < S.length(); i++) {
			if (S[i] == '-') {
				if (S.length() - i >= k) {
					for (int j = 0; j < k; j++) {
						S[i + j] = (S[i + j] == '-' ? '+' : '-');
					}
					flips++;
				}
				else {
					flips = -1;
					break;
				}
			}
		}
		if (flips == -1) cout << "Case #" << c << ": IMPOSSIBLE\n";
		else cout << "Case #" << c << ": " << flips << "\n";
	}

	return 0;
}