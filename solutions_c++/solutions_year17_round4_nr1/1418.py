#include <cstdio>
#include <iostream>

using namespace std;

int N, P, cnt[5];

void solve()
{
    cin >> N >> P;

    for (int i = 0; i < P; i++) {
        cnt[i] = 0;
    }

    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        cnt[x % P]++;
    }

    /*
    cout << endl;
    for (int i = 0; i < P; i++) {
        cout << cnt[i] << " ";
    }
    cout << endl;*/

    int sol = cnt[0];
    for (int i = 1; i <= P / 2; i++) {
        if (i == P - i) {
            sol = sol + cnt[i] / 2;
            cnt[i] = cnt[i] % 2;
        } else {
            sol = sol + min(cnt[i], cnt[P - i]);
            int val = min(cnt[i], cnt[P - i]);
            cnt[i] = cnt[i] - val;
            cnt[P - i] = cnt[P - i] - val;
        }
    }

    /*
    for (int i = 0; i < P; i++) {
        cout << cnt[i] << " ";
    }
    cout << endl;
    cout << sol << endl;*/

    int crtRest = 0;
    if (P == 4 && cnt[2] == 1) {
        crtRest = 2;
        sol++;
        cnt[2] = 0;
    }

    for (int i = 1; i < P; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            if (crtRest == 0) {
                sol++;
            }

            crtRest = (crtRest + i) % P;
            // cout << "adding " << i << " " << crtRest << " " << sol << endl;
        }
    }

    cout << sol << endl;
}

int main()
{
    freopen("chocolate.in", "r", stdin);
    freopen("chocolate.out", "w", stdout);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
