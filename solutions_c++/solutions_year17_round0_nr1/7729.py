#include <iostream>
#include <string>

#define forn(i, n) for(int i = 0; i < n; ++i)
#define fore(i, a, b) for(int i = a; i < b; ++i)

using namespace std;

void test(int t) {
    string s;
    int n, k;
    cin >> s >> k;
    n = s.size();
    int res = 0;
    forn(i, n - k + 1) {
        if (s[i] == '+') {
            continue;
        }
        fore(j, i, i + k) {
            s[j] = s[j] == '-' ? '+' : '-';
        }
        res++;
    }
    fore(i, n - k, n) {
        if (s[i] == '-') {
            res = -1;
            break;
        }
    }
    cout << "Case #" << t << ": ";
    if (res == -1) {
        cout << "IMPOSSIBLE";
    }
    else {
        cout << res;
    }
    cout << endl;
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

