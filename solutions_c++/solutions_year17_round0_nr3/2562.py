#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

int main() {
    long T, N, K;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N >> K;
        priority_queue<long> q;
        map<long, long> counts;
        q.push(N);
        counts[N]++;

        long total = 0;
        long num, lo, hi;;
        while (total < K) {
            num = q.top();
            q.pop();
            hi = num / 2;
            lo = (num - 1) / 2;

            if (!counts[hi]) q.push(hi);
            counts[hi] += counts[num];
            if (!counts[lo]) q.push(lo);
            counts[lo] += counts[num];
            total += counts[num];
        }

        cout << "Case #" << t << ": ";
        cout << hi << ' ' << lo;
        cout << endl;
    }
}
