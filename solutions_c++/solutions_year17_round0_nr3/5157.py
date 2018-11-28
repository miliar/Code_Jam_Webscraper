#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        long long n, k;
        cin >> n >> k;
        priority_queue<long long> q;
        q.push(n);
        long long ansmax = n, ansmin = n;
        while (k--) {
            long long cur = q.top();
            q.pop();
            ansmax = cur/2;
            ansmin = (cur-1)/2;
            q.push(ansmax);
            q.push(ansmin);
        }
        cout << "Case #" << test << ": " << ansmax << ' ' << ansmin << '\n';

        cerr << "Solved case " << test << '\n';
    }
    return 0;
}