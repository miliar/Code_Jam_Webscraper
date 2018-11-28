#include <iostream>
#include <cstdio>
#include <queue>
#include <string>

using namespace std;



struct node {
    int start;
    int end;
    node() = default;
    node(int s, int e) : start(s), end(e) {}
    bool operator<(const node& that) const {
        auto dist_this = end - start;
        auto dist_that = that.end - that.start;
        return dist_that == dist_this ? start > that.start : dist_this < dist_that;
    }
};


void solve(int k, int n) {
    //cout << k << " " << n;
    if (k==n) {
        cout << 0 << " " << 0;
        return;
    }
    // if (n == 1) {
    //     cout << (k+1)/2 << " " <<(k-1)/2;
    //     return;
    // }
    priority_queue<node> pq;
    pq.push(node(1, k));
    int ls, lr;
    while (n--) {
        auto cur = pq.top();
        pq.pop();
        auto s = cur.start;
        auto e = cur.end;

        auto select = s + (e-s)/2;
        ls = select - s;
        lr = e - select;
        if (s <= select -1)
            pq.emplace(s, select -1);
        if (e >= select + 1)
            pq.emplace(select+1, e);
    }

    cout << max(ls, lr) << " " <<min(ls, lr);
}

int main() {
    int t;
    cin >> t;
    int i = 0;
    while (i++ < t) {
        int k, n;
        cin >> k >> n;
        cout << "Case #" << i << ": ";
        solve(k, n);
        cout << endl;
    }
}
