#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

typedef uint64_t my_int;

pair<my_int, my_int> split_interval(my_int interval) {
    if (interval % 2 == 0) {
        return make_pair(interval / 2, (interval / 2) - 1);
    } else {
        my_int r = (interval - 1)/2;
        return make_pair(r, r);
    }
}

pair<my_int, my_int> solve(my_int N, my_int K) {
    priority_queue<my_int> intervals = priority_queue<my_int>();

    intervals.push(N);

    for (int i = 1; i <= K-1; i++) {
        my_int interval = intervals.top();
        intervals.pop();

        pair<my_int, my_int> splits = split_interval(interval);
        if (splits.first > 0) {
            intervals.push(splits.first);
        }
        if (splits.second > 0) {
            intervals.push(splits.second);
        }
    }

    // get interval for last person
    my_int last_interval = intervals.top();

    return split_interval(last_interval);

}

int main() {
    int T;
    cin >> T;

    for (int c = 1; c <= T; c++) {
        my_int N, K;
        cin >> N >> K;        

        pair<my_int,my_int> res = solve(N, K);

        printf("Case #%d: %llu %llu\n", c, res.first, res.second);
    }

    return 0;
}