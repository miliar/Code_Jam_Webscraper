#include <cstdio>
#include <vector>
#include <algorithm>

const int MAXN = 2001;
const int INF = ~0u >> 2;

struct Ticket{
    int seat;
    int person;
}ticket[MAXN];

int T, n, m, c, own[MAXN];

int main() {
    scanf("%d", &T);
    for (int cs = 1; cs <= T; cs++) {
        scanf("%d%d%d", &n, &c, &m);
        std::fill(own + 1, own + c + 1, 0);
        for (int i = 1; i <= m; i++) {
            scanf("%d%d", &ticket[i].seat, &ticket[i].person);
            own[ticket[i].person]++;
        }
        int answer = 0;
        for (int i = 1; i <= c; i++) {
            answer = std::max(answer, own[i]);
        }
        for (int seat = 1; seat <= n; seat++) {
            int tot = 0;
            for (int i = 1; i <= m; i++) {
                if (ticket[i].seat <= seat) {
                    tot++;
                }
            }
            answer = std::max(answer, (tot + seat - 1) / seat);
        }
        int transfer = 0;
        for (int seat = 1; seat <= n; seat++) {
            int tot = 0;
            for (int i = 1; i <= m; i++) {
                if (ticket[i].seat == seat) {
                    tot++;
                }
            }
            transfer += std::max(0, tot - answer);
        }
        printf("Case #%d: %d %d\n", cs, answer, transfer);
    }
    return 0;
}
