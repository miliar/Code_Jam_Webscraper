#include <iostream>
#include <map>
#include <vector>
#include <queue>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;

    for (int tc_i = 0; tc_i < tc; tc_i++) {
        long long n, k;
        cin >> n >> k;

        priority_queue<long long> q;

        q.push(n);

        long long x, y;

        for (int i = 0; i < k; i++) {
            long long val = q.top() - 1;
            q.pop();

            x = val / 2;
            y = val / 2 + (val % 2);

            q.push(x);
            q.push(y);
        }

        cout << "Case #" << (tc_i + 1) << ": ";

        cout << y << " " << x;

        cout << endl;
    }

    return 0;
}