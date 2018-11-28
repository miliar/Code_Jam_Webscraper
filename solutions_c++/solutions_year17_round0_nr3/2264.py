#include <bits/stdc++.h>

using namespace std;

void solve(int test_num)
{
    long long n, k;
    cin >> n >> k;
    k--;
    long long first = 0;
    long long level_size = 1;
    long long level_sum = n;
    while (not (k >= first && k < first + level_size)) {
        first += level_size;
        level_sum -= level_size;
        level_size *= 2;
    }

    long long pos_in_level = k - first;
    long long el = level_sum / level_size;
    if (pos_in_level < level_sum % level_size) {
        el++;
    }

    cout << "Case #" << test_num << ": " << (el - 1 + 1) / 2 << ' ' << (el - 1) / 2 << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        solve(i);
    }
}
