#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdint.h>

using namespace std;

double INF = 1.0;

int main()
{
    for (int i = 0; i < 16; i++)
            INF *= 10.0;

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        int N, Q;
        cin >> N >> Q;

        vector<int> E(N, 0);
        vector<int> S(N, 0);

        for (int n = 0; n < N; ++n)
            cin >> E[n] >> S[n];

        vector<vector<int> > mat(N, vector<int> (N, 0));
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                cin >> mat[i][j];

        vector<vector<int64_t> > distance(N, vector<int64_t> (N, -1));
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                if (i == j)
                    distance[i][j] = 0;
                else
                    distance[i][j] = mat[i][j];

        for (int k = 0; k < N; ++k)
        {
            for (int i = 0; i < N; ++i)
            {
                for (int j = 0; j < N; ++j)
                {
                    if ((distance[i][k] != -1) && (distance[k][j] != -1))
                    {
                        if (distance[i][j] == -1 || (distance[i][j] > (distance[i][k] + distance[k][j])))
                            distance[i][j] = distance[i][k] + distance[k][j];
                    }
                }
            }
        }

        vector<vector<double> > dist(N, vector<double> (N, INF));
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
                if (i == j)
                {
                    dist[i][j] = 0;
                    continue;
                }

                double tij = (double)(distance[i][j])/(double)(S[i]);
                if (distance[i][j] == -1)
                    dist[i][j] = INF;
                else
                    dist[i][j] = (distance[i][j] > E[i]) ? INF : tij;
            }
        }

        //cout << endl;
        for (int k = 0; k < N; ++k)
        {
            /*
            cout << "iter " << k << ": " << endl;
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                    cout << dist[i][j] << " ";
                cout << endl;
            }
            */

            for (int i = 0; i < N; ++i)
            {
                for (int j = 0; j < N; ++j)
                {
                    if (dist[i][j] > (dist[i][k] + dist[k][j]))
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }

        printf("Case #%d:", t);
        for (int q = 0; q < Q; ++q)
        {
            int u, v;
            cin >> u >> v;

            --u;
            --v;

            printf(" %.6f", dist[u][v]);
        }
        printf("\n");

    }
}
