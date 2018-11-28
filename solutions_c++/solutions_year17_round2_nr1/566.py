#include <iostream>
#include <cstdio>

using namespace std;

typedef long double ld;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int Ti = 1; Ti <= T; Ti++) {
        int D, N;
        scanf("%d %d", &D, &N);

        ld t = 0;

        for (int Ni = 0; Ni < N; Ni++) {
            int K, S;
            scanf("%d %d", &K, &S);
            t = max(t, (ld)(D-K)/S);
        }

        printf("Case #%d: %.9f\n", Ti, (double)(D/t));
    }
}
