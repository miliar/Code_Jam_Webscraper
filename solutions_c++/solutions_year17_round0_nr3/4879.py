#include <algorithm>
#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#define F first
#define S second
#define PB push_back
typedef long long ll;
using namespace std;

struct Node {
    ll l;
    ll r;
} node, n1, n2;

bool operator <(const Node& x, const Node& y) {
    return abs(x.r - x.l) < abs(y.r - y.l);
}

ll distance(ll a, ll b) {
    return abs(a-b) - 1;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("C-small-2-attempt1.in", "r", stdin);
    freopen("Output.out", "w", stdout);

    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll N, K; cin >> N >> K;

        priority_queue<Node> q;
        node.l = 0;
        node.r = N+1;
        q.push(node);

        while (--K) {
            node = q.top();
            q.pop();
            ll pos = (node.l + node.r)/2;

            n1.l = node.l;
            n1.r = pos;

            n2.l = pos;
            n2.r = node.r;

            q.push(n1);
            q.push(n2);
        }

        node = q.top();
        ll pos = (node.l + node.r)/2;
        ll dL = distance(pos, node.l);
        ll dR = distance(pos, node.r);

        cout << "Case #" << t << ": ";
        cout << max(dL, dR) << ' ' << min(dL, dR);
        cout << '\n';
    }

    return 0;
}