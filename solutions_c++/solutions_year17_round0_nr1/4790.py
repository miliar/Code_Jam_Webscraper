#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 1, inf = 1000111222;

int solve(string s, int k)
{
    int ans = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-') {
            if (s.size() - i < k) {
                return -1;
            }
            ans++;
            for (int j = i; j < i + k; ++j) {
                s[j] = s[j] == '+' ? '-' : '+';
            }
        }
    }
    return ans;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    int k;
    cin >> T;
    string s;
    for (int I = 1; I <= T; ++I) {
        cin >> s >> k;
        int ans = solve(s, k);
        cout << "Case #" << I << ": ";
        if (ans == -1) cout << "IMPOSSIBLE";
        else cout << ans;
        cout << endl;
    }
    return 0;
}


