#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

int T, N, C, M;
vector<int> P[1005];
bool vis[1005];

pair<int, int> go()
{
    int a = (P[1].size() > P[2].size()) ? 1 : 2;
    int b = 3 - a;
    int ans = 0, need = 0;
    sort(P[1].begin(), P[1].end());
    sort(P[2].begin(), P[2].end());
    for (int i = 0; i < P[b].size(); i++)
    {
        int idx = 0;
        for (; idx < P[a].size(); idx++)
            if (P[a][idx] > P[b][i])
                break;
        bool found = false;
        for (; idx < P[a].size(); idx++)
            if (!vis[idx])
            {
                vis[idx] = true;
                found = true;
                break;
            }
        if (!found)
        {
            for (int j = 0; j < P[a].size(); j++)
                if (!vis[j])
                {
                    vis[j] = true;
                    if (P[b][i] == 1)
                        need++;
                    else
                        ans += P[a][j] == P[b][i];
                    break;
                }
        }
    }
    return make_pair(need + P[a].size(), ans);
}

int main()
{
	ios::sync_with_stdio(0);

    freopen("B.in", "r", stdin);
    freopen("Bout.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> C >> M;
        for (int i = 1; i <= C; i++)
            P[i].clear();
        memset(vis, 0, sizeof(vis));

        for (int i = 0, p, b; i < M; i++)
        {
            cin >> p >> b;
            P[b].push_back(p);
        }

        pair<int, int> ans = go();
        cout << "Case #" << t << ": " << ans.first << " " << ans.second << "\n";
    }

	return 0;
}
