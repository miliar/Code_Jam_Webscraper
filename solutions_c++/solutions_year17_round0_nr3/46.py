#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

map<long long, long long> cnt;

int main(void) {

    int test_num;
    cin >> test_num;

    for (int Case = 1 ; Case <= test_num ; ++Case) {

        long long n, k;
        cin >> n >> k;

        cnt.clear();
        cnt[n] = 1;

        long long ans = -1;
        while (!cnt.empty()) {
            auto mx = *prev(cnt.end());
            if (k <= mx.second) {
                ans = mx.first;
                break;
            } else {
                long long val = mx.first, mid = (mx.first + 1) / 2;
                cnt[mid - 1] += mx.second;
                cnt[val - mid] += mx.second;
                cnt.erase(prev(cnt.end()));
                k -= mx.second;
            }
        }

        long long mid = (ans + 1) / 2;
        auto out = minmax(mid - 1, ans - mid);
        cout << "Case #" << Case << ": " << out.second << " " << out.first << endl;

        cerr << Case << endl;
    }

    return 0;
}
