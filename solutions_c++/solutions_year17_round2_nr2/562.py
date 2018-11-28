#include <iostream>
#include <cstdio>

using namespace std;

char A[2001];

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int Ti = 1; Ti <= T; Ti++) {
        int N, R, O, Y, G, B, V;
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

        for (int Ni = 0; Ni <= N; Ni++) A[Ni] = 0;

        int mx = max(R, max(Y, B));
        int mn = min(R, min(Y, B));
        int mid = R+Y+B-mx-mn;

        char s, r, t;

        if ( R >= Y && R >= B ) {
            s = 'R';
            if ( Y >= B ) r = 'Y', t = 'B';
            else r = 'B', t = 'Y';
        }
        else if ( Y >= R && Y >= B ) {
            s = 'Y';
            if ( R >= B ) r = 'R', t = 'B';
            else r = 'B', t = 'R';
        }else {
            s = 'B';
            if ( R >= Y ) r = 'R', t = 'Y';
            else r = 'Y', t = 'R';
        }

        for (int Ni = 0; Ni < N && mx; Ni+=2)
            A[Ni] = s, mx--;

        for (int Ni = N-1; Ni >= 0 && !A[Ni] && mid; Ni-=2)
            A[Ni] = r, mid--;

        for (int Ni = 0; Ni < N; Ni++)
            if ( !A[Ni] ) {
                if ( mid ) A[Ni] = r, mid--;
                else A[Ni] = t, mn--;
            }

        bool OK = true;

        for (int Ni = 0; Ni < N; Ni++)
            if ( A[Ni] == A[(Ni+1)%N] ) OK = false;
        if ( mx ) OK = false;

        printf("Case #%d: ", Ti);
        if ( !OK ) puts("IMPOSSIBLE");
        else puts(A);
    }
}
