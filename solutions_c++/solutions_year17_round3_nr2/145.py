#include <iostream>
#include <vector>

using namespace std;

int d[721][721][2];

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n[2];
        cin >> n[0] >> n[1];

        for (int i = 0; i < 2; i++)
            for (int j = 0; j < n[i]; j++)
            {
                int x, y;
                cin >> x >> y;

                for (int s = x + 1; s <= y; s++)
                    for (int v = 0; v <= 720; v++)
                    {
                        int u = s - v;
                        if (u < 0 || u > 720)
                            continue;

                        d[u][v][i] = 1 << 20;;
                    }
            }

        for (int i = 0; i <= 720; i++)
            for (int j = !i; j <= 720; j++)
                for (int k = 0; k < 2; k++)
                {
                    if (d[i][j][k])
                        continue;

                    d[i][j][k] = 1 << 20;
                    if (i && k == 0)
                        d[i][j][k] = min(d[i][j][k], min(d[i - 1][j][0], d[i - 1][j][1] + 1));
                    if (j && k == 1)
                        d[i][j][k] = min(d[i][j][k], min(d[i][j - 1][1], d[i][j - 1][0] + 1));
                }

        int a = min(d[720][720][0], d[720][720][1]);
        a += a % 2;

        cout << "Case #" << tt << ": " << a << endl;

        for (int i = 0; i <= 720; i++)
            for (int j = 0; j <= 720; j++)
                d[i][j][0] = d[i][j][1] = 0;
    }

    return 0;
}
