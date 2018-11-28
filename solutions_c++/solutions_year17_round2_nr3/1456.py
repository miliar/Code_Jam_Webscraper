#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

struct ty
{
    int k, s;
}h[101];

long long dis[101][101];
bool inque[101];
double ti[101];
int N, Q;

void BFS(int v, int u, vector<double> &ans)
{
    for (int i = 0; i < N; i++)
        inque[i] = false;
    queue<int> que;
    que.push(v);
    ti[v] = 0;
    while (!que.empty())
    {
        int x = que.front(); que.pop();
//        cout<<x<<endl;
        for (int i = 0; i < N; i++)
        {
            if (dis[x][i] == -1LL) continue;
            if (dis[x][i] > h[x].k) continue;
            double tmp = ti[x] + (double)dis[x][i] / (double)h[x].s;
//            cout<<x<<" "<<i<<" "<<tmp<<endl;
            if ((!inque[i]) || inque[i] && tmp < ti[i])
            {
                ti[i] = tmp;
                que.push(i);
                inque[i] = true;
            }
        }
    }
    ans.push_back(ti[u]);
}

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    cin>>T;
    for (int cas = 1; cas <= T; cas++)
    {
        cin>>N>>Q;
        for (int i = 0; i < N; i++)
        {
            cin>>h[i].k>>h[i].s;
        }
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
                cin>>dis[i][j];
        }
        for (int k = 0; k < N; k++)
        {
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                    if (dis[i][k] != -1LL and dis[k][j] != -1LL)
                    {
                        if (dis[i][k] + dis[k][j] < dis[i][j] || dis[i][j] == -1LL)
                            dis[i][j] = dis[i][k] + dis[k][j];
                    }
            }
        }

//        for (int i = 0; i < N; i++)
//        {
//
//            for (int j = 0; j < N; j++)
//                cout<<dis[i][j]<<" ";
//            cout<<endl;
//        }

        vector<double> ans;
        for (int q = 0; q < Q; q++)
        {
            int v, u;
            cin>>v>>u;
            BFS(v - 1, u - 1, ans);
        }
        printf("Case #%d:", cas);
        for (int i = 0; i < Q; i++)
            printf(" %.8f", ans[i]);
        puts("");
    }
    return 0;
}
