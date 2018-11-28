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
		ll N;
		cin >> N;
		string S = to_string(N);
		string result = S;
		string prevresult = S;
		do {
			S = result;
			prevresult = result;
			result = "";
			if (S[0] == '1' && S.length() > 1) {
				if (S[1] == '0') {
					for (int i = 0; i < S.length() - 1; i++) {
						result += '9';
					}
					break;
				}
			}
			if (result.length() > 0) {
				break;
			}
			for (int i = 0; i < S.length(); i++) {
				if (i == S.length() - 1) {
					result += S[i];
					break;
				}
				if (S[i] > S[i + 1]) {
					result += (S[i] - 1);
					for (int j = 0; j < S.length() - i - 1; j++) {
						result += '9';
					}
					break;
				}
				else {
					result += S[i];
				}
			}
		} while (result != prevresult);
		cout << "Case #" << c << ": " << result << "\n";
	}

	return 0;
}