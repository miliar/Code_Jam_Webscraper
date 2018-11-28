#include <iostream>
#include <vector>
#include <set>
#include <sstream>
#include <cmath>
#include <map>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <algorithm>
#include <list>

using namespace std;

void solve() {
    long long n, k;
    cin >> n >> k;
    if (n == k) {
        cout << "0 0\n";
        return;
    }
    map<long long, long long> sg_len;
    sg_len[n] = 1;
    k--;
    while (k > 0) {
        auto biggest = *(sg_len.rbegin());
        long long q = min(biggest.second, k);
        sg_len[biggest.first] -= q;
        if (sg_len[biggest.first] == 0) {
            sg_len.erase(biggest.first);
        }
        long long nsz = (biggest.first - 1) / 2;
        if (biggest.first % 2 == 0) {
            sg_len[nsz] += q;
            sg_len[nsz + 1] += q;
        } else {
            sg_len[nsz] += 2 * q;
        }
        k -= q;
    }
    auto ans_seg = *(sg_len.rbegin());
    long long nsz = (ans_seg.first - 1) / 2;
    if (ans_seg.first % 2 == 0) {
        cout << nsz + 1 << " " << nsz << "\n";
    } else {
        cout << nsz << " " << nsz << "\n";
    }
    
}

void stupid() {
    int n, k;
    cin >> n >> k;
    int arr[1002] = {};
    for (int i = 1; i <= k; i++) {
        int best_sl = -1, best_sr = -1, best_id = -1;
        for (int j = 0; j < n; j++) {
            if (arr[j] == 1) continue;
            int sl = 0, sr = 0;
            for (int li = j - 1; li >= 0 && arr[li] == 0; li--) {
                sl++;
            }
            for (int ri = j + 1; ri < n && arr[ri] == 0; ri++) {
                sr++;
            }
            
            if (min(sl, sr) > min(best_sl, best_sr) ||
                (min(sl, sr) == min(best_sl, best_sr) && max(sl, sr) > max(best_sl, best_sr))) {
                best_sl = sl;
                best_sr = sr;
                best_id = j;
            }
        }
        arr[best_id] = 1;
        if (k == i) {
            cout << max(best_sl, best_sr) << " " << min(best_sl, best_sr) << "\n";
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    
    
    return 0;
}
