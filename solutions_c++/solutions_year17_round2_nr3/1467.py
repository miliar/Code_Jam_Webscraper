#include <bits/stdc++.h>
using namespace std;
#define ing long long
struct Node {
    int cno;
    int hno;
    int remain;
    Node(int _cno, int _hno, int _remain)
        : cno(_cno)
        , hno(_hno)
        , remain(_remain)
    {
    }
};
vector<pair<int, int> > edge[201];
double ans = 1e9;
int E[200];
int S[200];
void dfs(int p, int city, int horse, int remain, int target, double ans2)
{
    if (city == target) {
        ans = min(ans2, ans);
        return;
    }
    for (auto i : edge[city]) {
        int t = i.first;
        int d = i.second;
        if (t == p)
            continue;
        if (E[city] < remain || S[city] < S[horse]) {
            if (d <= remain) {
                double ans3 = (double)ans2 + (double)d / S[horse];
                dfs(city, t, horse, remain - d, target, ans3);
            }
        }
        if (d <= E[city]) {
           // if (E[city] <= remain && S[city] <= S[horse]) {
            //} else {
                double ans4 = (double)ans2 + (double)d / S[city];
                dfs(city, t, city, E[city] - d, target, ans4);
            //}
        }
    }
};
#undef int
int main()
{
#define int long long
    int T;
    cin >> T;
    int kase = 0;
    while (T--) {
        cout << "Case #" << ++kase << ": ";
        int N, Q;
        cin >> N >> Q;
        for (int i = 0; i < N; i++) {
            cin >> E[i] >> S[i];
        }
        int D[200][200] = {};
        for (int i = 0; i < N; i++) {
            edge[i].clear();
            for (int j = 0; j < N; j++) {
                cin >> D[i][j];
                if (D[i][j] != -1) {
                    edge[i].push_back(make_pair(j, D[i][j]));
                }
            }
        }
        while (Q--) {
            int u, v;
            cin >> u >> v;
            u--;
            v--;
            ans = 1e18;
            dfs(u, u, u, E[u], v, 0);
            printf("%.7f\n", ans);
        }
    }
    return 0;
}
