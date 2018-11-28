#include <fstream>
#include <iomanip>

#define NMAX 101

using namespace std;

int dist[NMAX];
int speed[NMAX];

int distances[NMAX][NMAX];
int u[NMAX];
int v[NMAX];

double dp[NMAX][NMAX];
int remaining[NMAX][NMAX];

int main()
{
    ifstream f("express.in");
    ofstream g("express.out");
    int t;
    f >> t;
    int n, q;
    int i, j;
    double time;
    for (int ii = 0; ii < t; ii++)
    {
        f >> n >> q;
        for (i = 1; i <= n; i++)
            f >> dist[i] >> speed[i];
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                f >> distances[i][j];
        for (i = 0; i < q; i++)
            f >> u[i] >> v[i];
        dp[1][1] = 1;
        remaining[1][1] = dist[1];
        for (i = 1; i < n; i++)
        {
            for (j = 1; j < n; j++)
            {
                if (dp[i][j] > 0 && remaining[i][j] >= distances[i][i + 1])
                {
                    time = (double) distances[i][i + 1] / speed[j];
                    if (dp[i + 1][j] == 0 || dp[i + 1][j] > (dp[i][j] + time))
                    {
                        dp[i + 1][j] = dp[i][j] + time;
                        remaining[i + 1][j] = remaining[i][j] - distances[i][i + 1];
                    }
                    else if (dp[i + 1][j] == (dp[i][j] + time) && remaining[i + 1][j] < (remaining[i][j] - distances[i][i + 1]))
                    {
                        remaining[i + 1][j] = (remaining[i][j] - distances[i][i + 1]);
                    }

                    if (dp[i + 1][i + 1] == 0 || dp[i + 1][i + 1] > (dp[i][j] + time))
                    {
                        dp[i + 1][i + 1] = dp[i][j] + time;
                        remaining[i + 1][i + 1] = dist[i + 1];
                    }
                    else if (dp[i + 1][i + 1] == (dp[i][j] + time) && remaining[i + 1][i + 1] < dist[i + 1])
                    {
                        remaining[i + 1][i + 1] = dist[i + 1];
                    }
                }
            }
        }
        double sol = 0;
        for (j = 1; j <= n; j++)
            if (sol == 0 || dp[n][j] < sol)
            {
                sol = dp[n][j];
            }

        sol -= 1;
        g << "Case #" << ii + 1 << ": ";
        g << fixed << setprecision(7) << sol;
        g << '\n';
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
            {
                dp[i][j] = 0;
                remaining[i][j] == 0;
            }
    }
    f.close();
    g.close();
    return 0;
}