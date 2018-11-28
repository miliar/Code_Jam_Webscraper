#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 10;
const int INF = (int)(1e9);

char flip(char c) {
    return (c == '+') ? '-' : '+';
}

void run() {
    string s; int k;
    cin >> s >> k;
    int res = 0;
    for(int i = 0; i + k - 1 < s.length(); ++i) {
        if (s[i] == '-') {
            for(int j = i; j < i + k; ++j) s[j] = flip(s[j]);
            ++res;
        }
    }
    for(int i = 0; i < s.length(); ++i)
        if (s[i] == '-') {
            cout << "IMPOSSIBLE\n";
            return;
        }
    cout << res << endl;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cout << "Case #" << tc << ": ";
        run();
    }
}

