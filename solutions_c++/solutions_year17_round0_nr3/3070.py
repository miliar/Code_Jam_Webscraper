#include <algorithm>
#include <iostream>
#include <vector>
#include <deque>
#define F first
#define S second
#define PB push_back
typedef long long ll;
using namespace std;

struct Node {
    ll size;
    ll cnt;
} node;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll N, K; cin >> N >> K;

        deque<Node> dq;
        node.size = N;
        node.cnt = 1;
        dq.PB(node);

        while (K > dq.front().cnt) {
            node = dq.front();
            K -= node.cnt;
            dq.pop_front();

            Node child1, child2;
            child2.size = (node.size-1)/2;
            child1.size = (node.size - child2.size - 1);

            child1.cnt = node.cnt;
            child2.cnt = node.cnt;

            bool used1 = false, used2 = false;
            for (ll i = 0; i < dq.size(); ++i) {
                if (used1 && used2)
                    break;
                if (!used1 && dq[i].size == child1.size)
                    dq[i].cnt += child1.cnt, used1 = true;
                if (!used2 && dq[i].size == child2.size)
                    dq[i].cnt += child2.cnt, used2 = true;
            }

            if (!used1 && !used2 && child2.size == child1.size)
                child1.cnt += child2.cnt, dq.PB(child1);
            else {
                if (child2.size > child1.size)
                    node = child2, child2 = child1, child1 = child2;
                if (!used1)
                    dq.PB(child1);
                if (!used2)
                    dq.PB(child2);
            }
        }

        node = dq.front();
        ll ans = (node.size - 1)/2;
        cout << "Case #" << t << ": ";
        cout << (node.size - ans - 1) << ' ' << ans;
        cout << '\n';
    }

    return 0;
}

