#include "bits/stdc++.h"
using namespace std;

const int N = 30;

string arr[N];

int main() {
    freopen ("inp.in", "r", stdin);
    freopen ("A.out", "w", stdout);
    int t; cin >> t;
    for (int qq = 1; qq <= t; qq++) {
       int n, m; cin >> n >> m;
       for (int i = 1; i <= n; i++) {
            cin >> arr[i];
            for (int j = 1; j < (int) arr[i].size(); j++) {
                if (arr[i][j] == '?') {
                    arr[i][j] = arr[i][j - 1];
                }
            }
            for (int j = (int) arr[i].size() - 2; j >= 0; j--) {
                if (arr[i][j] == '?') {
                    arr[i][j] = arr[i][j + 1];
                }
            }
        }
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < (int) arr[i].size(); j++) {
                if (arr[i][j] == '?') {
                    arr[i][j] = arr[i - 1][j];
                }
            }
        }
        for (int i = n - 1; i >= 1; i--) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == '?') {
                    arr[i][j] = arr[i + 1][j];
                }
            }
        }
        cout << "Case #" << qq << ":\n";
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < m; j++) {
                cout << arr[i][j];
            }
            cout << '\n';
        }
    }
}