#include <bits/stdc++.h>

#define fr first
#define sc second
//#define int long long
#define all(x) x.begin(), x.end()
#define pb push_back
#define forn(i, b, n) for (int i = b; i < n; ++i)
#define endl '\n'

using namespace std;
const int MAXN = 1e3 + 2, INF = 1e9 + 9, MOD = 1e9 + 7, N = 1e5 + 1;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long ll;

main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    int n;
    cin >> n;
    forn(i, 0, n) {
        string s;
        int k;
        cin >> s >> k;
        bitset<MAXN> beb;
        int m = s.size();
        forn(j, 0, m)
            beb[j] = (s[j] == '+');
        int c = 0;
        forn(j, 0, m) {
            if (beb[j] == 0) {
                if (m - j < k) {
                    c = -1;
                    break;
                } else {
                    forn(q, j, j + k)
                        beb[q] = !beb[q];
                    ++c;
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (c == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << c << endl;
    }
}
