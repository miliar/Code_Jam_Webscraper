#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <queue>
#include <sstream>
#include <limits>
#include <list>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <vector>
#include <regex>

using namespace std;

int solve(int n, int p, vector<int> &need, vector<vector<int>> &pack) {
    if (n == 1) {
        int res = 0;
        for (int i = 0; i < p; ++i) {
            long long low = 0;
            for (int k = max(1LL, 10LL * pack[0][i] / 11 / need[0] - 5); k <= 10LL * pack[0][i] / 9 / need[0] + 5; ++k) {
                if (9LL * need[0] * k <= 10LL * pack[0][i] && 10LL * pack[0][i] <= 11LL * need[0] * k) {
                    ++res;
                    break;
                }
            }
        }
        return res;
    } else {
        int res = 0;
        vector<int> indexes(p, 0);
        for (int i = 0; i < p; ++i) indexes[i] = i;
        do {
            int cur_res = 0;
            for (int i = 0; i < p; ++i) {
                long long low = max(1LL, max(10LL * pack[0][i] / 11 / need[0] - 5, 10LL * pack[1][indexes[i]] / 11 / need[1] - 5));
                long long high = max(1LL, min(10LL * pack[0][i] / 9 / need[0] + 5, 10LL * pack[1][indexes[i]] / 9 / need[1] + 5));

                for (long long k = low; k <= high; ++k) {
                    if (9LL * need[0] * k <= 10LL * pack[0][i] && 10LL * pack[0][i] <= 11LL * need[0] * k &&
                        9LL * need[1] * k <= 10LL * pack[1][indexes[i]] && 10LL * pack[1][indexes[i]] <= 11LL * need[1] * k) {
                        ++cur_res;
                        break;
                    }
                }
            }

            res = max(res, cur_res);
        } while (next_permutation(indexes.begin(), indexes.end()));

        return res;
    }
}

int main() {
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, p;
        cin >> n >> p;
        vector<int> need(n);
        for (int i = 0; i < n; ++i) {
            cin >> need[i];
        }

        vector<vector<int>> pack(n, vector<int>(p, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < p; ++j) {
                cin >> pack[i][j];
            }
        }

        cout << "Case #" << t << ": " << solve(n, p, need, pack) << endl;
    }

    return 0;
}
