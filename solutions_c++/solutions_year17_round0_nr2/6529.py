#include <bits/stdc++.h>

#define x first
#define y second
//#define int long long
#define forn(i, b, n) for (int i = b; i < n; ++i)
#define endl '\n'
#define all(x) x.begin(), x.end()
#define pb push_back

using namespace std;

const int MAXN = 1e5 + 5, INF = INT_MAX, MOD = 1e9 + 7;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unsigned long long u64;

main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    int t;
    cin >> t;
    forn(tt, 0, t) {
        string s;
        cin >> s;
        int n = s.size(), i1;
        for (int i = 1; i < n; ++i) {
            i1 = i;
            if (s[i] < s[i - 1]) {
                for (int j = i; j >= 1; --j) {
                    if (s[j] < s[j - 1]) {
                        s[j] = '9';
                        --s[j - 1];
                    } else {
                        break;
                    }
                }
                break;
            }
        }
        forn(i, i1 + 1, n) {
            s[i] = '9';
        }
        cout << "Case #" << tt + 1 << ": ";
        forn(i, 0, n) {
            if (s[i] != '0')
                cout << s[i];
        }
        cout << endl;
    }
}
