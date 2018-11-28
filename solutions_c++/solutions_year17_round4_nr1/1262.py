#include <iostream>
#include <cstdio>

using namespace std;

int DP[101][101][101][5];

int main()
{
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int Ti = 1; Ti <= T; Ti++) {
        int N, P;
        scanf("%d %d", &N, &P);

        int num[5] = {};
        int ans = 0;

        for (int Ni = 0; Ni < N; Ni++) {
            int x;
            scanf("%d", &x);

            if ( x%P == 0 ) ans++;
            else num[x%P]++;
        }

        fill(DP[0][0][0], DP[100][100][100]+5, -1000);
        DP[0][0][0][0] = 0;

        for (int i = 0; i <= num[1]; i++)
            for (int j = 0; j <= num[2]; j++)
                for (int k = 0; k <= num[3]; k++)
                    for (int p = 0; p < P; p++){
                        if ( i ) DP[i][j][k][p] = max(DP[i][j][k][p], DP[i-1][j][k][(p-1+P)%P]+(p==1));
                        if ( j ) DP[i][j][k][p] = max(DP[i][j][k][p], DP[i][j-1][k][(p-2+P)%P]+(p==2));
                        if ( k ) DP[i][j][k][p] = max(DP[i][j][k][p], DP[i][j][k-1][(p-3+P)%P]+(p==3));
                    }

        int mx = 0;
        for (int p = 0; p < P; p++)
            mx = max(mx, DP[num[1] ][num[2] ][num[3] ][p]);

        ans += mx;
        printf("Case #%d: %d\n", Ti, ans);
    }
}
