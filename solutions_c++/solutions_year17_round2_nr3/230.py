#include <iostream>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
void print(int testNum, string ans) {
    cout << "Case #" << testNum << ": " << ans << endl;
}

const int maxN = 200;
long double din[maxN];

long long d[maxN][maxN];
long double minDist[maxN][maxN];
bool used[maxN];

int main(void) {
    freopen("/Users/glebone/Downloads/C-large.in.txt", "r", stdin);
    freopen("/Users/glebone/ClionProjects/bsuir/result.out", "w", stdout);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        int n, q;
        cin >> n >> q;
        vector <pair <int, int> > maxWithSpeed;
        maxWithSpeed.push_back({0, 0});
        for (int i = 0; i < n; i++) {
            int x, y;
            cin >> x >> y;
            maxWithSpeed.push_back({x, y});
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cin >> d[i][j];
                if (d[i][j] == -1) {
                    d[i][j] = (long long int) 1e18;
                }
            }
        }

        for (int k = 1; k <= n; ++k)
            for (int i = 1; i <= n; ++i)
                for (int j = 1; j <= n; ++j)
                    if (d[i][k] < 1e15 && d[k][j] < 1e15)
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);



        vector <long double> ans;
        for (int p = 1; p <= q; p++) {
            int from;
            int to;
            cin >> from;
            cin >> to;
            for (int i = 1; i <= n; i++) {
                din[i] = 1e18;
                used[i] = false;
            }
            din[from] = 0;

            for (int i = 1; i <= n; i++) {
                int s = -1;
                for (int j = 1; j <= n; j++) {
                    if (!used[j]) {
                        if (s == -1 || din[j] < din[s]) {
                            s = j;
                        }
                    }
                }
                used[s] = true;

                for (int j = 1; j <= n; j++) {
                    if (!used[j]) {
                        if (d[s][j] <= maxWithSpeed[s].first) {
                            din[j] = min(din[j], din[s] + (long double)d[s][j] / maxWithSpeed[s].second);
                        }
                    }
                }
            }
            ans.push_back(din[to]);

        }
        cout << "Case #" << test << ": ";
        for (int i = 0; i < (int)ans.size(); i++) {
            printf("%.10f ", (double) ans[i]);
        }
        cout << endl;


    }
}