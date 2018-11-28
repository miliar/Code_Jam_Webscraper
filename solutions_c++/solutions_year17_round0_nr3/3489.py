#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for (int i=0;i<(n);i++)

pair<long, long> devide(long n) {
    return n % 2 == 0 ? make_pair(n/2, n/2-1) : make_pair(n/2, n/2);
}

void solve(int t) {
    long N, K;
    cin >> N >> K;
    priority_queue<long> q;
    q.push(N);
    REP(i, K-1) {
        long a = q.top();
        q.pop();
        auto p = devide(a);
        q.push(p.first);
        q.push(p.second);
    }
    long a = q.top();
    auto p = devide(a);
    cout << "Case #" << t << ": " << max(p.first, p.second) << " " << min(p.first, p.second) << endl;
}

int main() {
    int T;
    cin >> T;
    REP(t, T) solve(t+1);
}
