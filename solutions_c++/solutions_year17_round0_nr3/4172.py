#include <iostream>
#include <map>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <queue>
#define REP(i, n) for(int i = 0; i < n; ++i)
#define RANGE(i, x, n) for(int i = x; i < n; ++i)
using namespace std;

typedef long long ll;
const ll INF = 0x3f3f3f3f3f3f3f3f;

struct Node {
    ll L;
    ll R;
    bool operator <(const Node &r) const {
        return R - L < r.R - r.L;
    }
};

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    RANGE(p, 1, T + 1) {
        priority_queue<Node> que;
        while(!que.empty()) que.pop();
        ll N, K;
        cin >> N >> K;
        Node node;
        node.L = 1;
        node.R = N;
        que.push(node);
        ll mins = INF, maxs = INF;
        REP(i, K) {
            node = que.top();
            que.pop();
            Node tmp1, tmp2;
            tmp1.L = node.L;
            tmp1.R = (node.L + node.R) / 2 - 1;
            tmp2.L = (node.L + node.R) / 2 + 1;
            tmp2.R = node.R;
            mins = min(tmp1.R - tmp1.L + 1, tmp2.R - tmp2.L + 1);
            maxs = max(tmp1.R - tmp1.L + 1, tmp2.R - tmp2.L + 1);
            que.push(tmp1);
            que.push(tmp2);
        }
        cout << "Case #" << p << ": " << maxs <<  " " << mins << endl;
    }
}
