#include<stdio.h>
#include<string.h>
#include<math.h>
#include <algorithm>
#include <queue>


class CellStalls {
public:
    long long int index_min;
    long long int index_max;
    long long int len;
    CellStalls(const CellStalls &o) {
        index_min = o.index_min;
        index_max = o.index_max;
        len = o.len;
    }
    CellStalls() {
        index_max = index_min = len = 0;
    }
    CellStalls(long long int imin, long long int imax) {
        index_min = imin;
        index_max = imax;
        len = index_max - index_min - 1;
    }
    void initIndex(long long int imin, long long int imax) {
        index_min = imin;
        index_max = imax;
        len = index_max - index_min - 1;
    }
    bool muteLeft(CellStalls &l, CellStalls &r) {
        if (len == 0)
            return false;
        long long int mid = (index_max + index_min) / 2;
        l.initIndex(index_min, mid);
        r.initIndex(mid, index_max);
        return true;
    }
    void getLsRs(long long int &maxS, long long int &minS) {
        long long int mid = (index_max + index_min) / 2;
        minS = std::min(mid - index_min, index_max - mid) - 1l;
        maxS = std::max(mid - index_min, index_max - mid) - 1l;
    }
    bool operator < (const CellStalls &p) const {
        return len < p.len;
    }
};
void resolv2(long long int n, long long int k, long long int &MAX_LR, long long int &MIN_LR) {
    std::priority_queue < CellStalls > pq;
    pq.push(CellStalls(0, n+1));
    for (int i = 0; i < k - 1; ++i) {
        CellStalls range = pq.top();pq.pop();
        CellStalls ls, rs;
        if (range.muteLeft(ls, rs)) {
            if (ls.len > 0)
                pq.push(ls);
            if (rs.len > 0)
                pq.push(rs);
        } else {
            --k;
        }
    }
    if (pq.empty()) {
        MAX_LR = MIN_LR = 0;
        return;
    }
    CellStalls result = pq.top();pq.pop();
    result.getLsRs(MAX_LR, MIN_LR);

}
int main() {
    long long int N, K, RMIN, RMAX;
    int T;
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for(int i = 0; i < T;++i) {
        scanf("%lld %lld", &N, &K);
        resolv2(N, K, RMAX, RMIN);
        printf("Case #%d: %lld %lld\n", i+1, RMAX, RMIN);
    }

    return 0;
}
