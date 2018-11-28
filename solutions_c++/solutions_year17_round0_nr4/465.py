#include <iostream>
#include <map>
#include <queue>

#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define FOR2(i, s, n) for (int i = (s); i <= (n); ++i)
#define REP(i, n) FOR(i, 0, n)

using namespace std;
typedef long long ll;

void solve()
{
    int N, M;
    cin >> N >> M;

    int val = 0;

    int diag_r[110] = {0, };
    int diag_c[110] = {0, };
    int origin[110][110] = {0, };
    int record[110][110] = {0, };

    int top_inval[110] = {0, };
    int bot_inval[110] = {0, };

    REP(i, M) {
        char x;
        int r, c;
        cin >> x >> r >> c;
        if (x == 'o' || x == '+') {
            origin[r][c] += 2;
            ++val;
            int lt = c - r + 1;
            int rt = c + r - 1;
            if (lt >= 1) top_inval[lt] = 1;
            if (rt <= N) top_inval[rt] = 1;

            int lb = c - (N - r);
            int rb = c + (N - r);
            if (lb >= 1) bot_inval[lb] = 1;
            if (rb <= N) bot_inval[rb] = 1;
        }
        if (x == 'o' || x== 'x') {
            diag_r[r] = c;
            diag_c[c] = r;
            origin[r][c] += 1;
            ++val;
        }
    }

    int s = 1;

    FOR2(i, 1, N) {
        if (diag_r[i] > 0) continue;
        while(s <= N) {
            if (diag_c[s] == 0) break;
            ++s;
        }
        diag_r[i] = s;
        diag_c[s] = i;
        record[i][s] += 1;
        ++val;
    }

    FOR2(i, 1, N) {
        if (top_inval[i] == 0) {
            top_inval[i] = 1;
            record[1][i] += 2;
            ++val;

            int lb = i - (N - 1);
            int rb = i + (N - 1);
            if (lb >= 1) bot_inval[lb] = 1;
            if (rb <= N) bot_inval[rb] = 1;
        }
    }

    FOR2(i, 1, N) {
        if (bot_inval[i] == 0) {
            bot_inval[i] = 1;
            record[N][i] += 2;
            ++val;
        }
    }

    cout << val << " ";
    int cnt = 0;
    FOR2(i, 1, N) {
        FOR2(j, 1, N) {
            if (record[i][j]) ++cnt;
        }
    }
    cout << cnt << endl;
    FOR2(i, 1, N) {
        FOR2(j, 1, N) {
            if (record[i][j] == 0) continue;

            int rr = record[i][j] + origin[i][j];
            if (rr == 3) cout << "o " << i << " " << j << endl;
            if (rr == 1) cout << "x " << i << " " << j << endl;
            if (rr == 2) cout << "+ " << i << " " << j << endl;
        }
    }
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}