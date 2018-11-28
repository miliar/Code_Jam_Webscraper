#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <list>
#include <string>
#include <algorithm>
#include <chrono>
#include <limits>
#include <cmath>
#include <unordered_set>
#include <set>
#include <queue>

using namespace std;

struct node {
    string val;
    node(const string& s) : val(s) {}
    node(const string& s, int pos, int k) : val(s) {
        for (int i = 0; i < k; ++i) {
            val[pos + i] = val[pos + i] == '-' ? '+' : '-';
        }
    }
    bool operator <(const node& o) const {
        return val < o.val;
    }
    bool operator==(const node& o) const {
        return val == o.val;
    }
};
/*
bool operator<(const node n1, const node n2) {
    return n1.val < n2.val;
}
*/
struct nhash {
    size_t operator()(const node& n) const {
        return hash<string>()(n.val);
    }
};

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        string s;
        int k;
        cin >> s >> k;

        string target(s.size(), '+');

        unordered_map<node, int, nhash> vis{ {node{s}, 0} };

        queue<node> q;
        q.push(node{s});

        int ans = -1;

        while (!q.empty()) {
            node cur = q.front();
            if (cur.val == target) {
                ans = vis[cur];
                break;
            }
            q.pop();
            for (int p = 0; p <= s.size() - k; ++p) {
                node new_n = node{cur.val, p, k};
                if (vis.find(new_n) == vis.end()) {
                    q.push(new_n);
                    vis[new_n] = vis[cur] + 1;
                }
            }
        }

        if (ans == -1) cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << t + 1 << ": " << ans << endl;
    }

    return 0;
}
