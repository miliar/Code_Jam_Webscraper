#include<bits/stdc++.h>
#define INF 0x7fffffff
#define INFLL 1e17
#define PI 2*acos(0.0)
#define show(x) cout<< #x <<" is "<< x <<"\n"
using namespace std;

#define FS first
#define SC second
#define PB(t) push_back(t)
#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<PII> VPII;

int main() {
    #ifndef ONLINE_JUDGE
        freopen("RA-large.in", "rt", stdin);
        freopen("outputA.txt", "wt", stdout);
    #endif

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T, cas = 0, r, c;

    for (cin >> T; cas < T; cas++) {
        cin >> r >> c;
        vector<string> tab(r);
        for (int i = 0; i < r; i++) {
            cin >> tab[i];
        }

        for (int i = 0; i <r; i ++) {
            for (int j = 0; j < c; j++) {
                while (j < c && tab[i][j] == '?') {
                    j++;
                }
                if (j == c) {
                    continue;
                }
                for (int k = j - 1; k >= 0; k--) {
                    if (tab[i][k] == '?') {
                        tab[i][k] = tab[i][j];
                    } else {
                        break;
                    }
                }
                for (int k = j + 1; k < c; k++) {
                    if (tab[i][k] == '?') {
                        tab[i][k] = tab[i][j];
                    } else {
                        break;
                    }
                }
            }
        }

        for (int i, k, j = 0; j < c; j++) {
            for (i = 0; i < r; i++) {
                if (tab[i][j] == '?') {
                    for (k = i - 1; k >= 0; k--) {
                        if (tab[k][j] != '?') {
                            break;
                        }
                    }
                    if (k >= 0) {
                        for (int k2 = i; k2 > k; k2--) {
                            tab[k2][j] = tab[k][j];
                        }
                        continue;
                    }
                    for (k = i + 1; k < r; k++) {
                        if (tab[k][j] != '?') {
                            break;
                        }
                    }
                    if (k < r) {
                        for (int k2 = i; k2 <= k; k2++) {
                            tab[k2][j] = tab[k][j];
                        }
                        continue;
                    }
                    cout << "algo fallo\n";
                }
            }
        }
        cout << "Case #" << cas + 1 <<":\n";
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout <<tab[i][j];
            }
            cout << "\n";
        }

    }


return 0;
}
