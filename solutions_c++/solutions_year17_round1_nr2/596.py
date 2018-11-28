#include <queue>
#include <cstdio>
#include <algorithm>

const int MAXD = 101;
const int MAXR = 100001;
const int INF = ~0u >> 2;

struct Interval{
    int l, r, k;
    Interval() {}
    Interval(int l, int r, int k) : l(l), r(r), k(k) {}
    bool operator <(const Interval &rhs)const {
        return r > rhs.r;
    }
}ranges[MAXR];

int T, n, p, total, d[MAXR], r[MAXR], package[MAXD][MAXD];
std::priority_queue<Interval> queue[MAXR];

int getMin(int r, int s) {
    return (10 * r) / (9 * s);
}

int getMax(int r, int s) {
    return (10 * r + 11 * s - 1) / (11 * s);
}

int main() {
    freopen("B.in", "r", stdin);
    scanf("%d", &T);
    for (int cs = 1; cs <= T; cs++) {
        scanf("%d%d", &n, &p);
        for (int i = 1; i <= n; i++) {
            scanf("%d", r + i);
        }
        total = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= p; j++) {
                scanf("%d", &package[j][i]);
                ranges[++total] = Interval(std::max(1, getMax(package[j][i], r[i])), getMin(package[j][i], r[i]), i);
                if (ranges[total].l > ranges[total].r) total--;
            }
            while (!queue[i].empty()) queue[i].pop();
        }
        int td = 0;
        std::sort(ranges + 1, ranges + total + 1, [](const Interval &a, const Interval &b) {
            return a.l < b.l || (a.l == b.l && a.r < b.r);
        });
        for (int i = 1; i <= total; i++) {
            d[++td] = ranges[i].l;
            d[++td] = ranges[i].r;
        }
        std::sort(d + 1, d + td + 1);
        td = std::unique(d + 1, d + td + 1) - d - 1;
        int answer = 0;
        for (int scanner = 1; scanner <= td; scanner++) {
            int now = d[scanner];
            for (int j = 1; j <= total; j++) {
                if (ranges[j].l == now) {
                    queue[ranges[j].k].push(ranges[j]);
                }
            }
            while (true) {
                bool check = true;
                for (int i = 1; i <= n; i++) {
                    if (queue[i].empty()) {
                        check = false;
                        break;
                    }
                }
                if (!check) break;
                answer++;
                for (int i = 1; i <= n; i++) {
                    queue[i].pop();
                }
            }
            for (int i = 1; i <= n; i++) {
                while (!queue[i].empty() && queue[i].top().r == now) {
                    queue[i].pop();
                }
            }
        }
        printf("Case #%d: %d\n", cs, answer);
    }
    return 0;
}