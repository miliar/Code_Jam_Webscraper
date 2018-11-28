#include <bits/stdc++.h>

using namespace std;

typedef long long li;

void solve(int test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) 
        solve(i + 1);
}

const int MAXN = 110;
int n, m;
string s[MAXN];

void solve(int test_number) {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }

    int prev = 0;
    for (int i = 0; i < n; i++) {
        vector<int> pos;
        int prev_j = 0;
        for (int j = 0; j < m; j++) {
            if (s[i][j] != '?') {
                pos.push_back(j);
                for (int x = prev; x <= i; x++) {
                    for (int y = prev_j; y <= j; y++) {
                        s[x][y] = s[i][j];
                    }
                }
                prev_j = j + 1;
            }
        }
        if (pos.size() != 0) {
            for (int x = prev; x <= i; x++) {
                for (int y = 0; y < m; y++) {
                    if (s[x][y] == '?') {
                        s[x][y] = s[x][y - 1];
                    }
                }
            }
            prev = i + 1;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (s[i][j] == '?') {
                s[i][j] = s[i - 1][j];
            }
        }
    }

    cout << "Case #" << test_number << ":" << endl;
    for (int i = 0; i < n; i++) {
        cout << s[i] << endl;
    }

}
