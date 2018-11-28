#include <iostream>
#include <map>

using namespace std;

int main() {
    long long number_of_cases;
    cin >> number_of_cases;
    for (long long test_case = 0; test_case < number_of_cases; ++test_case) {
        long long n, k;
        cin >> n >> k;
        map<long long, long long> cnt_intervals;
        cnt_intervals[-n] = 1;
        long long x, y;
        while (k) {
            auto p = cnt_intervals.begin();
            long long len = -p->first;
            x = len / 2;
            y = len / 2 + len % 2 - 1; 
            if (cnt_intervals.begin()->second <= k) {
                k -= p->second;
                cnt_intervals[-x] += p->second;
                cnt_intervals[-y] += p->second;
                cnt_intervals.erase(p);
            } else {
                cnt_intervals.begin()->second -= k;
                k = 0;
            }
        }
        cout << "Case #" << test_case + 1 << ": ";
        cout << x << " " << y;
        cout << endl;
    }
    return 0;
}
