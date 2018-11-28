    #include <bits/stdc++.h>

    using namespace std;

    #define pb push_back
    #define ppb pop_back
    #define mp make_pair
    #define y0 thezeroXname
    #define x0 thezeroYname
    #define fst first
    #define snd second

    typedef long long ll;
    typedef long double ld;

    const int MAXN = 5e6 + 13;
    const int MAXK = 5e6 + 13;
    const int INF = 2e9 + 7;
    const int MD = 1e9 + 7;
    const ld EPS = 1e-9;
    const ld PI = 3.14159265359;

    string s;
    int n;

    void repair(int index) {
        for (int i = index + 1; i < n; i++) s[i] = '9';
        for (int i = index; i > -1; i--) {
            if (s[i] > '0') {
                s[i]--;
                break;
            } else {
                s[i] = '9';
            }
        }
        for (int i = 0; i < n - 1; i++) {
            if (s[i] > s[i + 1]) repair(i);   
        }
    }

    int main() {
        #ifdef LOCAL
        freopen("t.in", "r", stdin);
        freopen("t.out", "w", stdout);
        #else
        //freopen("bfs.in", "r", stdin);
        //freopen("bfs.out", "w", stdout);
        #endif

        int T;
        cin >> T;
        for (int t = 0; t < T; t++) {
            s = "";
            cin >> s;
            n = s.length();
            for (int i = 0; i < n - 1; i++) {
                if (s[i] > s[i + 1]) repair(i);
            }

            string ans = "0";
            for (int i = 0; i < n; i++) {
                if (s[i] != '0') {
                    ans = s.substr(i);
                    break;
                }
            }

            cout << "Case #" << t + 1 << ": " << ans << endl;
        }

        return 0;
    }