#include <cstdio>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

const double PI = acos((double)-1.0);
const int MAXN = 1000;

struct node {
    long long R, H;
    bool operator < (const node& x) const {
        return R*H < x.R*x.H;
    }
    double get_s() const {
        return 2*PI*R*R+2*PI*R*H;
    }
};

node nodes[MAXN+5];

int main() {
//    freopen("A-eg.in", "r", stdin);
//    freopen("A-small.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
//    freopen("A-eg.out", "w", stdout);
//    freopen("A-small.out", "w", stdout);
    freopen("A-large.out", "w", stdout);
    int T, n, k;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        double ans = 0;
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++i) {
            scanf("%lld%lld", &nodes[i].R, &nodes[i].H);
        }
        for (int i = 0; i < n; ++i) {
            node now_max = nodes[i];
            priority_queue<node> q;
            for (int j = 0; j < n; ++j) {
                if (j != i) {
                    q.push(nodes[j]);
                }
            }
            double now_ans = now_max.get_s()-PI*now_max.R*now_max.R;
            for (int j = 0; j < k-1; ++j) {
                node top_node = q.top();
                q.pop();
                now_ans += 2*PI*top_node.R*top_node.H;
            }
            ans = max(now_ans, ans);
        }
        printf("Case #%d: %.9f\n", t, ans);
    }
    return 0;
}