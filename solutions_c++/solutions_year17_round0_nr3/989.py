#include <cstdlib>
#include <cstring>

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

void work() {
    uint64_t n, k;
    cin >> n >> k;
    uint64_t x = n, c0 = 1, c1 = 0, cnt = 0;
    while (cnt < k) {
        // cout << x << ' ' << c0 << ' ' << c1 << endl;
        if (cnt + c1 >= k) {
            cout << (x + 1) / 2 << ' ' << x / 2 << endl;
            return;
        }
        cnt += c1;
        if (cnt + c0 >= k) {
            cout << x / 2 << ' ' << (x - 1) / 2 << endl;
        }
        cnt += c0;

        uint64_t tc0, tc1;
        if (x % 2 == 1) {
            tc0 = c0 * 2 + c1;
            tc1 = c1;
        }
        else {
            tc0 = c0;
            tc1 = c0 + c1 * 2;
        }
        c0 = tc0;
        c1 = tc1;
        x = (x - 1) / 2;
    }
}

int main() {
    int tot; cin >> tot;
    for (int cas = 1; cas <= tot; cas ++) {
        cout << "Case #" << cas << ":";
        cout << " ";
        work();
    }
    return 0;
}
