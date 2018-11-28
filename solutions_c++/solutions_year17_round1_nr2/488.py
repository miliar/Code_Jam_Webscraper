// jimjam
#include <cstdio>
#include <algorithm>
using namespace std;

int T, N, P, serve[55], ans;
int pack[55][55];
int p[55];

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &N, &P);
        ans = 0;
        for (int i = 0; i < N; i++) scanf("%d", serve+i), p[i] = 0;
        for (int i = 0; i < N; i++) {
            for (int p = 0; p < P; p++) {
                scanf("%d", pack[i]+p);
            }
            sort(pack[i],pack[i]+P);
        }

        bool stop = 0;
        int s = 1;
        while (1) {
            for (int i = 0; i < N; i++) {
                if (p[i] == P) {
                    stop = 1;
                    break;
                }
                if (10*pack[i][p[i]] < 9*s*serve[i]) p[i]++, i = -1;
                else if(10*pack[i][p[i]] > 11*s*serve[i]) s++, i = -1;
            }
            if (stop) break;
            else {
                ans++;
                for (int i = 0; i < N; i++) p[i]++;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
