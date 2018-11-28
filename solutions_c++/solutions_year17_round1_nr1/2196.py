#include <string>
#include <iostream>
#include <vector>

using namespace std;

int cnt(string &s) {
    int cc = 0;
    for (auto c : s) { if (c=='?') cc++; }
    return cc;
}

void solve() {
    int r, c;
    cin >> r >> c;
    vector<string> m;
    string s;
    for (int i = 0; i < r; ++i) {
        cin >> s;
        m.push_back(s);
    //    cout << s;
    }
    for (int i = 0; i < r; ++i) {
        if (c==cnt(m[i]))
            continue;
        for (int j=1; j < c; ++j)
            if (m[i][j] == '?' && m[i][j-1] != '?')
                m[i][j] = m[i][j-1];
        for (int j=c-2; j >= 0; --j)
            if (m[i][j] == '?' && m[i][j+1] != '?')
                m[i][j] = m[i][j+1];
    }

    for (int i = 1; i < r; ++i) {
        if (cnt(m[i]) == c && cnt(m[i-1]) != c) {
            m[i] = m[i-1];
        }
    }
    for (int i = r -2 ; i >= 0; --i) {
        if (cnt(m[i]) == c && cnt(m[i+1]) != c) {
            m[i] = m[i+1];
        }
    }
    for (int i=0; i < r; ++i) {
        cout << m[i] <<endl;
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ":\n";
        solve();
    }
}
