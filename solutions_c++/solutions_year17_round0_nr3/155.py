#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <cstdint>

using namespace std;

using Res = pair<int64_t, int64_t>;

Res solve(int64_t n, int64_t k) {
    Res result;
    map<int64_t, int64_t> slots;

    slots[-n] = 1;
        
    while (true) {
        auto ans = -slots.begin()->first;
        auto cnt = slots.begin()->second;
        slots.erase(slots.begin());

        result.first = ans / 2;
        result.second = (ans - 1) / 2;

        if (cnt >= k) {
            break;
        }

        k -= cnt;
        slots[-result.first] += cnt;
        slots[-result.second] += cnt;
    }
    
    return result;
}

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        int64_t n, k;
        cin >> n >> k;

        auto res = solve(n, k);
        cout << "Case #" << i << ": " << res.first << " " << res.second << endl;
        
    }
        
}
