#include <cstdio>
#include <algorithm>
using namespace std;

int Ac, Aj, C[100], D[100], J[100], K[100];
int a[2][1440], dp[2][1440];

int f(int C[], int D[]) {
    if (max(D[0], D[1]) - min(C[0], C[1]) <= 720)
        return 2;
    if (max(C[0], C[1]) - min(D[0], D[1]) >= 720)
        return 2;
    return 4;
}

int solve() {
    scanf("%d%d", &Ac, &Aj);
    for (int i = 0; i < Ac; i++)
        scanf("%d%d", C + i, D + i);
    for (int i = 0; i < Aj; i++)
        scanf("%d%d", J + i, K + i);
    if (Ac == 1 || Aj == 1)
        return 2;
    if (Ac == 2)
        return f(C, D);
    if (Aj == 2)
        return f(J, K);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
        printf("Case #%d: %d\n", i, solve());
}
