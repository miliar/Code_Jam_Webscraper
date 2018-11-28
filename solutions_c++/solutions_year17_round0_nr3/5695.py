#include <iostream>
#include <queue>
// #include <priority_queue>
#include <stdexcept>
#include <tuple>

using namespace std;

int left(int i) {
    return (i-1)/2;
}
int right(int i) {
    return i/2;
}

tuple<int, int> foo(int n, int k) {
    priority_queue<int> q;
    q.push(n);
    for (int i = 0; i < k; i++) {
        n = q.top();
        q.pop();
        // cout << n << endl;
        q.push(right(n));
        q.push(left(n));
    }
    return make_tuple(right(n), left(n));
}



int main() {
    int t, n, k;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n >> k;
        // cout << foo(n, k) << endl;
        auto t = foo(n, k);
        cout << "Case #" << i << ": " << get<0>(t) << " " << get<1>(t) << endl;
    }
}