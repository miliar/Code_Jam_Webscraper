#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <limits>

#include <cstdio>
#include <cmath>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);

	int32_t T;
	cin >> T;

	for (auto tc = 1; tc <= T; tc++) {
		int64_t N;
		cin >> N;

		if (N < 10) {
			cout << "Case #" << tc << ": " << N << endl;
		}
		else {
			string S = to_string(N);

			while (true) {
				bool is_success = true;

				for (auto i = S.size() - 1; i > 0; i--) {
					if (S[i - 1] > S[i]) {
						S[i - 1]--;
						for (auto j = i; j < S.size(); j++) {
							S[j] = '9';
						}

						is_success = false;
						break;
					}
				}

				if (is_success) {
					break;
				}
			}

			cout << "Case #" << tc << ": " << stoll(S) << endl;
		}
	}

	return 0;
}