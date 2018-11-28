#include <iostream>
#include <algorithm>
#include <iomanip> 

using namespace std;

int f[102][102][102][5], inf, rems[5];

inline void upd(int &a, int b){
    if (a < b) {
        a = b;
    }
}

int main(int argc, const char * argv[]) {
    freopen("/Users/vadimantiy/Developer/codejam17/task1/task1/input.txt", "r", stdin);
    freopen("/Users/vadimantiy/Developer/codejam17/task1/task1/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int caseNumber;
    cin >> caseNumber;
    for (int casen = 0; casen < caseNumber; casen++) {
        memset(f, -63, sizeof(f));
        memset(rems, 0, sizeof(rems));
        int inf = -f[0][0][0][0];
        cerr << casen << '\n';
        cout << "Case #" << casen + 1 << ": ";
        int n, p;
        cin >> n >> p;
        for (int i = 1; i <= n; i++) {
            int x;
            cin >> x;
            rems[x%p]++;
        }
        f[rems[1]][rems[2]][rems[3]][0] = 0;
        for (int i = rems[1]; i >= 0; i--)
            for (int j = rems[2]; j >= 0; j--)
                for (int k = rems[3]; k >= 0; k--)
                    for (int rem = 3; rem >= 0; rem--) if (f[i][j][k][rem] != -inf) {
                        int updval = f[i][j][k][rem] + (rem == 0);
                        if (i > 0) {
                            upd(f[i - 1][j][k][(rem - 1 + p)%p], updval);
                        }
                        if (j > 0) {
                            upd(f[i][j - 1][k][(rem - 2 + p)%p], updval);
                        }
                        if (k > 0) {
                            upd(f[i][j][k - 1][(rem - 3 + p)%p], updval);
                        }
                    }
        int dp_max = -inf;
        for (int rem = 0; rem <= 3; rem++) {
            dp_max = max(dp_max, f[0][0][0][rem]);
        }
        int ans = rems[0] + dp_max;
        cout << ans << "\n";
    }
    return 0;
}
