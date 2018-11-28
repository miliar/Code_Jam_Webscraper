#include <bits/stdc++.h>
#define fr(i, n) for (int i = 0; i < n; i++)
#define frab(i, a, b) for (int i = a; i < b; i++)
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = 2e15 + 10;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int N = 5e5 + 10;
const int M = 1e3 + 10;

string solve() {
    int n, a, ab, b, bc, c, ac;
    cin >> n >> a >> ab >> b >> bc >> c >> ac;
    string s;
    if (ab > c || ac > b || bc > a) return "IMPOSSIBLE";
    if (n / 2 < max(a + ab + ac, max(c + ac + bc, b + ab + bc))) return "IMPOSSIBLE";
    int a1 = a - bc;
    int b1 = b - ac;
    int c1 = c - ab;
    if ((a1 + b1 + c1) / 2 < max(max(a1, b1), c1)) return "IMPOSSIBLE";

    fr(i, a1 + b1 + c1)
        s += '0';
    int len = a1 + b1 + c1;

    if (a1 >= b1 && a1 >= c1) {
        for (int i = 0; i < len && a1; i += 2)
            s[i] = 'R', a1--;
        for (int i = len - 1; i >= 0 && b1; i--)
            if (s[i] == '0' && (i == len - 1 || s[i + 1] != 'Y'))
                s[i] = 'Y', b1--;
        for (int i = 0; i < len; i++)
            if (s[i] == '0')
                s[i] = 'B';
        a1 = b1 = c1 = 0;
    }
    else if (b1 >= a1 && b1 >= c1) {
        for (int i = 0; i < len && b1; i += 2)
            s[i] = 'Y', b1--;
        for (int i = len - 1; i >= 0 && a1; i--)
            if (s[i] == '0' && (i == len - 1 || s[i + 1] != 'R'))
                s[i] = 'R', a1--;
        for (int i = 0; i < len; i++)
            if (s[i] == '0')
                s[i] = 'B';
        a1 = b1 = c1 = 0;
    }
    else if (c1 >= b1 && c1 >= a1) {
        for (int i = 0; i < len && c1; i += 2)
            s[i] = 'B', c1--;
        for (int i = len - 1; i >= 0 && b1; i--)
            if (s[i] == '0' && (i == len - 1 || s[i + 1] != 'Y'))
                s[i] = 'Y', b1--;
        for (int i = 0; i < len; i++)
            if (s[i] == '0')
                s[i] = 'R';
        a1 = b1 = c1 = 0;
    }

    string ans;
    fr(i, s.size())
        if (s[i] == 'R') {
            ans += s[i];
            while (bc)
                ans += "GR", bc--;
        }
        else if (s[i] == 'Y') {
            ans += s[i];
            while (ac)
                ans += "VY", ac--;
        }
        else {
            ans += s[i];
            while (ab)
                ans += "OB", ab--;
        }
    if (ans.size())
        if (ab + ac + bc)
            return "IMPOSSIBLE";
    while (ac) {
        ans += "VY";
        ac--;
    }

    if (ans.size() && bc) return "IMPOSSIBLE";
    else while (bc) {
        ans += "GR";
        bc--;
    }

    if (ans.size() && ab) return "IMPOSSIBLE";
    else while (ab) {
        ans += "OB";
        ab--;
    }

    return ans;
}

int main() {
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    //ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    fr(i, t) {
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }
}
