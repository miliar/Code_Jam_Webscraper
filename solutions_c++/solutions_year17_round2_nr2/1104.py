//#include <iostream>
//
//using namespace std;
//typedef long long ll;
//
//
//int main() {
//    freopen("../C-small-attempt1.in", "r", stdin);
//    freopen("../C-small.out1", "w", stdout);
//    int T;
//    cin >> T;
//    for (int cas = 1; cas <= T; cas++) {
//        printf("Case #%d: ", cas);
//
//        int n, q;
//        cin >> n >> q;
//        int e[n + 10], s[n + 10];
//        int d[n + 10][n + 10];
//        for (int i = 1; i <= n; i++) {
//            cin >> e[i] >> s[i];
//        }
//        for (int i = 1; i <= n; i++) {
//            for (int j = 1; j <= n; j++) {
//                cin >> d[i][j];
//            }
//        }
//        double dis[n + 10];
//        dis[1] = 0;
//        for (int i = 2; i <= n; i++) {
//            dis[i] = dis[i - 1] + d[i - 1][i];
//            //cout << i << " " << dis[i] << endl;
//        }
//        double dp[n + 10];
//        for (int i = 1; i <= n; i++) {
//            dp[i] = 999999999999999999.0;
//        }
//        dp[1] = 0;
//        for (int i = 1; i <= n; i++) {
//            for (int j = i + 1; j <= n; j++) {
//                if (dis[j] - dis[i] <= e[i]) {
//                    dp[j] = min(dp[j], dp[i] + ((dis[j] - dis[i]) / s[i]));
//                }
//            }
//        }
//        while (q--) {
//            int ss, ee;
//            cin >> ss >> ee;
//            printf("%.10f\n", dp[n]);
//        }
//
//    }
//
//    return 0;
//}
#include <iostream>
#include<vector>

using namespace std;
typedef long long ll;
char R = 'R';
char G = 'Y';
char B = 'B';
vector<char> ve[1110];

int main() {
    freopen("../B-small-attempt1.in", "r", stdin);
    freopen("../B-small.out1", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> g >> y >> b >> v;
        int tr = 0, tg = 0, tb = 0;
        if (r >= g && g >= b) {
            R = 'R';
            G = 'Y';
            B = 'B';
            tr = r;
            tg = g;
            tb = b;
        } else if (r >= b && b >= g) {
            R = 'R';
            G = 'B';
            B = 'Y';
            tr = r;
            tg = b;
            tb = g;
        } else if (g >= r && r >= b) {
            R = 'Y';
            G = 'R';
            B = 'B';
            tr = g;
            tg = r;
            tb = b;
        } else if (g >= b && b >= r) {
            R = 'Y';
            G = 'B';
            B = 'R';
            tr = g;
            tg = b;
            tb = r;
        } else if (b >= g && g >= r) {
            R = 'B';
            G = 'Y';
            B = 'R';
            tr = b;
            tg = g;
            tb = r;
        } else if (b >= r && r >= g) {
            R = 'B';
            G = 'R';
            B = 'Y';
            tr = b;
            tg = r;
            tb = g;
        }
        if (tr > tg + tb) {
            printf("IMPOSSIBLE\n");
        } else {
            for (int i = 1; i <= tr; ++i) {
                ve[i].clear();
            }
            while (tg > 0 || tb > 0) {
                for (int i = 1; i <= tr; ++i) {
                    if (ve[i].size() == 0) {
                        if (tg > 0) {
                            tg--;
                            ve[i].push_back(G);
                        } else if (tb > 0) {
                            tb--;
                            ve[i].push_back(B);
                        }
                    } else {
                        int l = ve[i].size();
                        if (ve[i][l - 1] == G) {
                            if (tb > 0) {
                                tb--;
                                ve[i].push_back(B);
                            }
                        }
                        if (ve[i][l - 1] == B) {
                            if (tg > 0) {
                                tg--;
                                ve[i].push_back(G);
                            }
                        }
                    }
                }
            }
            string ans = "";
            for (int i = 1; i <= tr; ++i) {
                ans += R;
                for (int j = 0; j < ve[i].size(); ++j) {
                    ans += ve[i][j];
                }
            }
            cout << ans << endl;

        }

    }

    return 0;
}