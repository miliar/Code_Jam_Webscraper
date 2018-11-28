#include <stdio.h>
#include <set>
#include <queue>

std::pair<int, int> simulate(int N, int K) {
    std::set<int> taken {-1, N};
    int maximal_min;
    int maximal_max;
    int best_index;
    for (int i = 0; i < K; ++i) {
        maximal_min = -1;
        maximal_max = -1;
        best_index = -1;

        auto it = taken.begin();
        int l = -1;
        int r = *it;
        while (++it != taken.end()) {
            l = r;
            r = *it;
            if (r - l == 1) continue;

            int local_best = (r + l) / 2;
            int ls = local_best - l - 1;
            int rs = r - local_best - 1;
            int min_lr = std::min(ls, rs);
            int max_lr = std::max(ls, rs);
            if (min_lr > maximal_min) {
                best_index = local_best;
                maximal_min = min_lr;
                maximal_max = max_lr;
            } else if (min_lr == maximal_min) {
                if (max_lr > maximal_max) {
                    best_index = local_best;
                    maximal_min = min_lr;
                    maximal_max = max_lr;
                }
            }
        }
        taken.insert(best_index);
    }
    return std::make_pair(maximal_min, maximal_max);
}

std::pair<int, int> mathish(int N, int K) {
    std::priority_queue<int> segs;
    segs.push(N);
    int s;
    int d;
    for (int i = 1; i < K; ++i) {
        s = segs.top() - 1;
        segs.pop();
        d = s / 2;
        segs.push(d);
        if (s % 2 == 0) {
            segs.push(d);
        } else {
            segs.push(d + 1);
        }
    }
    s = segs.top() - 1;
    d = s / 2;
    int d2 = d;
    if (s % 2 == 1) ++d2;
    return std::make_pair(d, d2);
}

int main() {
    int T;
    scanf("%d\n", &T);
    for (int cs = 1; cs <= T; ++cs) {
        int N, K;
        scanf("%d %d\n", &N, &K);
        auto p = mathish(N, K);
        printf("Case #%d: %d %d\n", cs, p.second, p.first);
    }
}
