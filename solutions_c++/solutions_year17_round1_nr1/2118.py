#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
#define pb push_back
#define mp make_pair
#define INF LLONG_MAX
char alpha[26][26];
int main() {

    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    int r, c, f;
    char s;
    int tt = t;
    while (t--) {
        cin >> r >> c;
        f = -1;
        char q = '?';
        vector<int> R(r, -1);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> s;
                if (R[i] == -1 && s != q) {
                    R[i] = j;
                }
                alpha[i][j] = s;
            }
            if (f == -1 && R[i] != -1) {
                f = i;
            }
        }

        for (int i = 0; i < r; i++) {
            if (R[i] != -1) {
                int tmp = R[i];
                for (int j = R[i]; j >= 0; j--) {
                    if (alpha[i][j] == q) {
                        alpha[i][j] = R[i];
                    } else {
                        R[i] = alpha[i][j];
                    }
                }
                R[i] = tmp;
                for (int j = R[i]; j < c; j++) {

                    if (alpha[i][j] == q) {
                        alpha[i][j] = R[i];
                    } else {
                        R[i] = alpha[i][j];
                    }
                }
            }
        }


        if (f != -1) {
            for (int i = f; i >= 0; i--) {
                if (R[i] == -1) {
                    for (int j = 0; j < c; j++) {
                        alpha[i][j] = alpha[f][j];
                    }
                }
            }

            for (int i = f; i < r; i++) {
                if (R[i] == -1) {
                    for (int j = 0; j < c; j++) {
                        alpha[i][j] = alpha[f][j];
                    }
                } else {
                    f = i;
                }
            }
        }

        cout << "Case #" << tt - t << ":" << endl;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << alpha[i][j];
            }
            cout << endl;
        }

    }

    return 0;
}