#pragma warning(disable:4996)

#include <stdio.h>
#include <memory.h>

int n, q;
double e[100];
double s[100];
double dist[100][100];

bool chk[100];
double mindist[100];
double d[100][100];

double ans[100];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d%d", &n, &q);
        for (int i=0; i<n; i++)
            scanf("%lf%lf", &e[i], &s[i]);
        for (int i=0; i<n; i++) for (int j=0; j<n; j++) scanf("%lf", &dist[i][j]);

        for (int i=0; i<n; i++)
        {
            memset(chk, 0, sizeof(chk));

            for (int j=0; j<n; j++)
                d[i][j] = -1;
            d[i][i] = 0;

            while (true)
            {
                int midx = -1;
                for (int j=0; j<n; j++)
                {
                    if (!chk[j] && d[i][j] != -1 && (midx==-1 || d[i][midx] > d[i][j]))
                        midx = j;
                }
                if (midx == -1 || d[i][midx] > e[i])
                    break;

                chk[midx] = true;

                for (int j=0; j<n; j++)
                {
                    if (!chk[j] && dist[midx][j] != -1 && (d[i][j]==-1 || d[i][j] > d[i][midx] + dist[midx][j]))
                        d[i][j] = d[i][midx] + dist[midx][j];
                }
            }

            for (int j=0; j<n; j++)
            {
                if (!chk[j])
                    d[i][j] = -1;
                else
                    d[i][j] /= s[i];
            }
        }

        for (int k=0; k<n; k++) for (int i=0; i<n; i++) for (int j=0; j<n; j++)
            if (d[i][k]!=-1 && d[k][j]!=-1 && (d[i][j]==-1 || d[i][j] > d[i][k] + d[k][j]))
                d[i][j] = d[i][k] + d[k][j];

        for (int i=0; i<q; i++)
        {
            int x, y;
            scanf("%d%d", &x, &y);
            x--; y--;
            ans[i] = d[x][y];
        }
        
        printf("Case #%d:", ++tt);
        for (int i=0; i<q; i++)
            printf(" %.8lf", ans[i]);
        printf("\n");
    }

    return 0;
}
