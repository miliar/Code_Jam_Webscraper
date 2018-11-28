#include <bits/stdc++.h>
using namespace std;

#define int long long
#define ll long long
#define vi vector<int>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++i)
#define FOR(i, a, b) for (int i = (int)a, _b = b; i <= _b; ++i)
#define FORD(i, a, b) for (int i = (int)a ,_b = b; i >= _b; --i)

#define MAX(a, b) (a > b ? a : b)
#define MIN(a, b) (a < b ? a : b)

#define DEBUG(X) { cerr << #X << " = " << (X) << endl; }

#define MAXN 100100

int GI(int &a){return scanf("%I64d", &a);}

int n, i, j, k, tmp, m, x, b, q, l, y, t;

vi v1, v2, v3;
int a[MAXN];
int mi, ma;
char s[30][30];

int32_t main(){
    freopen("AL.in", "rt", stdin);
    freopen("AL.out", "wt", stdout);

    GI(t);
    for (int z = 1; z <= t; z++){
        GI(m); GI(n);
        REP(i, m)
            scanf("%s", s[i]);

        for (int i = 0; i < m; i++){
            char c = '?';
            for (int j = 0; j < n; j++){
                if (s[i][j] == '?' && c != '?'){
                    s[i][j] = c;
                }
                c = s[i][j];
            }

            for (int j = n - 1; j >= 0; j--){
                if (s[i][j] == '?' && c != '?'){
                    s[i][j] = c;
                }
                c = s[i][j];
            }

        }

        for (int j = 0; j < n; j++){
            char c = '?';
            for (int i = 0; i < m; i++){
                if (s[i][j] == '?' && c != '?'){
                    s[i][j] = c;
                }
                c = s[i][j];
            }

            for (int i = m - 1; i >= 0; i--){
                if (s[i][j] == '?' && c != '?'){
                    s[i][j] = c;
                }
                c = s[i][j];
            }

        }

        cout << "Case #" << z << ":\n";
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++)
                cout << s[i][j];
            cout << endl;
        }
    }
}
