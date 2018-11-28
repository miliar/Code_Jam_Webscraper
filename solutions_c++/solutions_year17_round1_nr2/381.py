#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int N = 100;

int n, p, q[N][N], cand[N], r[N];
bool used[N][N];

bool valid(int re, int num, int tot) {
    re *= num;
    return re * 9 <= tot * 10 && tot * 10 <= re * 11;
}
void _main() {
    cin >> n >> p;
    for(int i = 0; i < n; ++i) cin >> r[i];
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < p; ++j) cin >> q[i][j];
        sort(q[i], q[i] + p);
    }
    int ans = 0;
    memset(used, false, sizeof(used));
    
    for(int i = 0; i < p; ++i) {
        int base = q[0][i];
        for(int _num = base * 0.9 / r[0]; _num <= base * 1.15 / r[0]; ++_num) {
            if(_num < 0 || !valid(r[0], _num, base)) continue;
            // cout << base << ' ' << _num << endl;
            memset(cand, -1, sizeof(cand));
            cand[0] = i;
            bool flag = true;
            for(int x = 1; x < n; ++x) {
                for(int j = 0; j < p; ++j) if(!used[x][j] && valid(r[x], _num, q[x][j])) {
                    cand[x] = j;
                    break;
                } 
                if (cand[x] == -1) {
                    flag = false;
                    break;
                }
            }
            
            if(!flag) continue;
            for(int ii = 0; ii < n; ++ii) used[ii][cand[ii]] = true;
            ans ++;
            break;
        }
    }
    cout << ans << endl;
}
int main() {
    int t, cas = 0;
    for (scanf("%d", &t); t--; ) {
        printf("Case #%d: ", ++cas);
        _main();
    }
    return 0;
}
