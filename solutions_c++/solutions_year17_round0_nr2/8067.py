#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

long process(long num);

int main(int argc, char const *argv[])
{
    int t, T;

    cin >> T;

    for (t = 1; t <= T; ++t) {
        long num, ans, prev_ans = -1;

        cin >> num;

        ans = num;

        while (ans != prev_ans) {
            prev_ans = ans;
            ans = process(ans);
        }

        printf("Case #%d: %ld\n", t, ans);
    }

    return 0;
}

long process(long num) {
    long ans = 0, i, N;
    vector<long> d;

    while (num > 0) {
        d.push_back(num % 10);
        num /= 10;
    }

    N = d.size();
    reverse(d.begin(), d.end());

    for (i = 0; i < N; ++i) {
        if (i == N - 1) {
            ans = 10 * ans + d[i];
        } else if (d[i + 1] >= d[i]) {
            ans = 10 * ans + d[i];
        } else {
            ans = 10 * ans + d[i] - 1;
            break;
        }
    }

    for (i = i + 1; i < N; ++i) {
        ans = 10 * ans + 9;
    }

    return ans;
}