#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include "io.h"

using std::max;
using std::min;
using std::priority_queue;
using std::vector;

struct node {
    long long l, r;
    node() {}
    node(long long _l, long long _r): l(_l), r(_r) {}
    long long get_mid() const {
        return (l+r)/2;
    }
    long long get_left_dis() const {
        return get_mid()-l;
    }
    long long get_right_dis() const {
        return r-get_mid();
    }
    long long get_max_dis() const {
        return max(get_left_dis(), get_right_dis());
    }
    long long get_min_dis() const {
        return min(get_left_dis(), get_right_dis());
    }
    vector<node> get_split() const {
        vector<node> v;
        if (l == r) {
            return v;
        } else {
            if (r-l == 1) {
                v.push_back(node(r, r));
                return v;
            } else {
                v.push_back(node(l, get_mid()-1));
                v.push_back(node(get_mid()+1, r));
                return v;
            }
        }
    }
    bool operator < (const node &x) const {
        if (get_min_dis() != x.get_min_dis()) {
            return get_min_dis() < x.get_min_dis();
        } else {
            if (get_max_dis() != x.get_max_dis()) {
                return get_max_dis() < x.get_max_dis();
            } else {
                return get_mid() > x.get_mid();
            }
        }
    }
};

int main() {
//    init_io("C-eg.in", "C-eg.out");
    init_io("C-small-2-attempt0.in", "C-small-2-attempt0.out");
//    init_io("B-large.in", "B-large.out");
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        long long n, k;
        priority_queue<node> q;
        scanf("%lld%lld", &n, &k);
        q.push(node(1, n));
        node tmp, ans, last;
        vector<node> v;
        for (long long i = 0; i < k; ++i) {
            if (q.top().l == q.top().r) {
//                printf("l == r == %lld\n", q.top().l);
                ans = q.top();
                goto finished;
            } else {
                last = tmp = q.top();
                q.pop();
                v = tmp.get_split();
                for (size_t j = 0; j < v.size(); ++j) {
//                    printf("push l=%lld r=%lld\n", v[j].l, v[j].r);
                    q.push(v[j]);
                }
//                if (q.size() == 1) {
//                    printf("q.size() == 1 l == %lld r == %lld\n", q.top().l, q.top().r);
//                    ans = q.top();
//                    goto finished;
//                }
            }
        }
        ans = last;
        finished:
        printf("Case #%d: %lld %lld\n", t, ans.get_max_dis(), ans.get_min_dis());
    }

    return 0;
}