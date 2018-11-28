#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    priority_queue<int> que;
    que.push(n);
    

    while (k-- > 1) {
        int larger = que.top();
        que.pop();
        que.push((larger - 1) / 2);
        que.push(larger / 2);
    }

    int last = que.top();
    cout << last / 2 << " " << (last - 1) / 2 << endl;
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}