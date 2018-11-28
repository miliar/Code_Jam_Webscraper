#include <iostream>
#include <vector>

#define forn(i, n) for(int i = 0; i < n; ++i)
#define fore(i, a, b) for(int i = a; i < b; ++i)

using namespace std;

void test(int tNum) {
    int r, c;
    cin >> r >> c;
    vector<vector<char> > v(r, vector<char>(c));
    forn(i, r) {
        forn(j, c) {
            cin >> v[i][j];
        }
    }
    forn(i, r) {
        forn(j, c) {
            if (v[i][j] == '?') {
                continue;
            }
            int k = j + 1;
            while (k < c && v[i][k] == '?') {
                v[i][k] = v[i][j];
                k++;
            }
            k = j - 1;
            while (k >= 0 && v[i][k] == '?') {
                v[i][k] = v[i][j];
                k--;
            }
        }
    }
    forn(i, r) {
        forn(j, c) {
            if (v[i][j] == '?') {
                continue;
            }
            int k = i + 1;
            while (k < r && v[k][j] == '?') {
                v[k][j] = v[i][j];
                k++;
            }
            k = i - 1;
            while (k >= 0 && v[k][j] == '?') {
                v[k][j] = v[i][j];
                k--;
            }
        }
    }
    cout << "Case #" << tNum << ":" << endl;
    forn(i, r) {
        forn(j, c) {
            cout << v[i][j];
        }
        cout << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    forn(i, t) {
        test(i + 1);
    }
    return 0;
}

