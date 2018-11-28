#include <iostream>
#include <string>
#include <queue>

using namespace std;
typedef long long ll;

void solve() {
    ll K, N;
    cin >> N >> K;

    // make heap
    priority_queue<ll> q;
    q.push(N);

    ll big, small;
    for (int i = 0; i < K; i++) {
        ll rem = q.top() - 1;
        q.pop();
        if (rem % 2) {
            small = (rem-1)/2;
            big = (rem+1)/2;
        } else {
            small = rem/2;
            big = rem/2;
        }
        q.push(small);
        q.push(big);
    }

    cout << big << " " << small;
}

int main() {
    ll T;
    cin >> T;
    for (ll i = 0; i < T; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << "\n";
    }
}
