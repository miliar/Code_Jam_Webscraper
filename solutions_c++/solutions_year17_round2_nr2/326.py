#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll inf = 1e14 + 7;

int kases, n;
int r, o, y, g, b, v;

int find_pos(string s, char x) {
    char c1, c2;
    switch (x) {
        case 'R': c1 = 'V'; c2 = 'O'; break;
        case 'O': c1 = 'R'; c2 = 'Y'; break;
        case 'Y': c1 = 'O'; c2 = 'G'; break;
        case 'G': c1 = 'Y'; c2 = 'B'; break;
        case 'B': c1 = 'G'; c2 = 'V'; break;
        case 'V': c1 = 'B'; c2 = 'R'; break;
    }
    int candidate = -1;
    for (int i = 1; i < s.length(); ++i) {
        if (s[i] == c1 || s[i - 1] == c1 || s[i] == c2 || s[i - 1] == c2 ||
            s[i] == x || s[i - 1] == x)
            continue;
        candidate = i;
        if (s[i] == s[i - 1])
            return candidate;
    }
    if (candidate != -1) return candidate;
    return s.length() - 1;
}

int judge(string s) {
    char c1[] = {'R', 'R', 'O', 'O', 'Y', 'Y', 'G', 'G', 'B', 'B', 'V', 'V'};
    char c2[] = {'V', 'O', 'R', 'Y', 'O', 'G', 'Y', 'B', 'G', 'V', 'B', 'R'};
    for (int i = 1; i < s.length(); ++i)
        for (int j = 0; j < 12; ++j)
            if ((s[i] == c1[j] && s[i - 1] == c2[j]) || s[i] == s[i - 1])
                return 0;
    return 1;
}

string insert(string s, int pos, char n) {
    return s.substr(0, pos) + n + s.substr(pos);
}

string put(string res, int val, char x) {
    if (res == "") {
        if (val == 0) return "";
        return string(val + 1, x);
    } else {
        for (int i = 0; i < val; ++i)
            res = insert(res, find_pos(res, x), x);
        return res;
    }
}

int main() {
    #ifdef ULTMASTER
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif
    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        string s = put("", r, 'R');
        s = put(s, o, 'O');
        s = put(s, y, 'Y');
        s = put(s, g, 'G');
        s = put(s, b, 'B');
        s = put(s, v, 'V');
        cout << "Case #" << kase << ": ";
        if (judge(s)) cout << s.substr(0, s.length() - 1) << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
