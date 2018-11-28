#include <cstdio>
#include <algorithm>

int main() {
    int T;
    scanf("%d", &T);
    long double D;
    int N;
    int pos, sp;
    long double ans;
    for (int t = 1; t <= T; t++) {
        scanf("%Lf%d", &D, &N);
        scanf("%d%d", &pos, &sp);
        ans = (D*sp) / (D - pos);
        for (int i = 1; i < N; i++) {
            scanf("%d%d", &pos, &sp);
            ans = std::min(ans, (D*sp) / (D - pos));
        }
        printf("Case #%d: %Lf\n", t, ans);
    }
    return 0;
}