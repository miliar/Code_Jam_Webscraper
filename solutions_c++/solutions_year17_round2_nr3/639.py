#include <iostream>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <queue>

using namespace std;

#define N 111
#define inf 1e18

int e[N], s[N];
long long dist[N], d[N][N];
double f[111];
bool used[N];
priority_queue <pair<double, int>, vector<pair<double, int> >, greater<pair<double, int> > > q;

int main(int argc, const char * argv[]) {
    freopen("/Users/vadimantiy/Developer/codejam17/task3/task3/input.txt", "r", stdin);
    freopen("/Users/vadimantiy/Developer/codejam17/task3/task3/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int caseNumber;
    cin >> caseNumber;
    for (int casen = 0; casen < caseNumber; casen++) {
        cerr << casen << '\n';
        cout << "Case #" << casen + 1 << ": ";
        int queries = 1;
        int n;
        cin >> n >> queries;
        for (int i = 1; i <= n; i++) {
            cin >> e[i] >> s[i];
        }
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++) {
                cin >> d[i][j];
            }
        // floyd
        for (int k = 1; k <= n; k++)
            for (int i = 1; i <= n; i++)
                for (int j = 1; j <= n; j++)
                    if (d[i][k] != -1 && d[k][j] != -1) {
                        if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j]) {
                            d[i][j] = d[i][k] + d[k][j];
                        }
                    }
        while (queries--) {
            for (int i = 1; i <= n; i++){
                f[i] = inf;
                used[i] = false;
            }
            int start, finish;
            cin >> start >> finish;
            while (!q.empty()) q.pop();
            f[start] = 0;
            q.push(make_pair(f[start], start));
            while (!q.empty()) {
                int u = q.top().second;
                q.pop();
                if (used[u]) {
                    continue;
                }
                used[u] = true;
                if (u == finish) {
                    break;
                }
                for (int v = 1; v <= n; v++)
                    if (!used[v] && d[u][v] != -1 && d[u][v] <= e[u]) {
                        double upd = f[u] + double(d[u][v]) / s[u];
                        if (f[v] > upd) {
                            f[v] = upd;
                            q.push(make_pair(f[v], v));
                        }
                    }
            }
            cout << setprecision(10) << f[finish];
            if (queries > 0) cout << " "; else cout << '\n';
        }
    }
    return 0;
}
