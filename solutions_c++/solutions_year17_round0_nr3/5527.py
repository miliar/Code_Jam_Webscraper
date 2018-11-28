#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <ctime>
#include <cstdlib>
#include <unordered_set>
#include <deque>
#include <queue>

using namespace std;

typedef long long ll;


int main() {
    int tests;
    cin >> tests;
    for (int test_id = 0; test_id < tests; ++test_id) {
        int n, k;
        cin >> n >> k;
        
        vector<bool> empty(n, true);
        for (int i = 0; i < k; ++i) {
            vector<int> closest_left(n);
            vector<int> closest_right(n);
            
            vector<int> L(n), R(n);
            
            for (int j = 0; j < n; ++j) {
                if (!empty[j])
                    closest_left[j] = j;
                else {
                    if (j == 0)
                        closest_left[j] = -1;
                    else
                        closest_left[j] = closest_left[j - 1];
                }
                L[j] = j - closest_left[j] - 1;
            }
            
            for (int j = n - 1; j >= 0; --j) {
                if (!empty[j])
                    closest_right[j] = j;
                else {
                    if (j == n - 1)
                        closest_right[j] = n;
                    else
                        closest_right[j] = closest_right[j + 1];
                }
                R[j] = closest_right[j] - j - 1;
            }
            
            int mn_value = -1e9;
            int best_idx = -1;
            
            for (int j = 0; j < n; ++j) {
                if (empty[j]) {
                    if (mn_value < min(L[j], R[j])) {
                        mn_value = min(L[j], R[j]);
                        best_idx = j;
                    } else if (mn_value == min(L[j], R[j])) {
                        if (max(L[j], R[j]) > max(L[best_idx], R[best_idx])) {
                            best_idx = j;
                        }
                    }
                }
            }
            
            empty[best_idx] = false;
            
            if (i == k - 1)
                cout << "Case #" << test_id + 1 << ": " << max(L[best_idx], R[best_idx]) << " " << min(L[best_idx], R[best_idx]) << endl;
        }
        
        
    }
}
