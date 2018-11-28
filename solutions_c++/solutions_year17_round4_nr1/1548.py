#include <bits/stdc++.h>

using namespace std;

const int MAXN = 110;

int A[MAXN][MAXN][MAXN][MAXN][4];
int n, p;

inline int get_ost(int x)
{
    int ost = p - (x % p);
    if (ost == p) {
        ost = 0;
    }
    return ost;
}

inline void update(int &a,const  int &b) {
    if (a == -1 or a < b) {
        a = b;
    }
}

void solve(int test_num)
{
    cin >> n >> p;

    vector<int> cnt(4, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[get_ost(x)]++;
    }

    memset(A, -1, sizeof(A));
//     cerr << A[109][109][109][109][0] << endl;
    A[cnt[0]][cnt[1]][cnt[2]][cnt[3]][0] = 0;
//         cerr << A[109][109][109][109][0] << endl;
    for (int i = MAXN - 1; i >= 0; i--) {
        for (int j = MAXN - 1; j >= 0; j--) {
            for (int k = MAXN - 1; k >= 0; k--) {
                for (int q = MAXN - 1; q >= 0; q--) {
                    for (int ost = 0; ost < p; ost++) {
//                         cerr << ost << endl;
//                             cerr << A[109][109][109][109][ost] << endl;

        int cur_val = A[i][j][k][q][ost];
        if (cur_val == -1) {
            continue;
        }
        int cur_cnt[4] = {i, j, k, q};

//         cerr << cur_val << ' ' << i << ' ' << j << ' ' << k << ' ' << p << endl;

        for (int take = 0; take < p; take++) {
            if (cur_cnt[take] == 0) {
                continue;
            }
            int new_ost = get_ost((take - ost + p) % p);
            cur_cnt[take]--;
            update(
                A[cur_cnt[0]][cur_cnt[1]][cur_cnt[2]][cur_cnt[3]][new_ost],
                cur_val + (ost == 0 ? 1 : 0)
            );
            cur_cnt[take]++;
        }
                    }
                }
            }
        }
    }

    cout << "Case #" << test_num + 1 << ": ";
    int best_ans = A[0][0][0][0][0];
    for (int i = 1; i < p; i++) {
        best_ans = max(best_ans, A[0][0][0][0][i]);
    }
    cout << best_ans;
    cout << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.precision(15);
    cout.setf(ios::fixed);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        solve(i);
    }
}
