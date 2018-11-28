#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 10;
const int INF = (int)(1e9);

string alter(char start, char nxt, int n_rep, bool extra) {
    string res = "";
    for(int i = 0; i < n_rep; ++i) {
        res.push_back(start); res.push_back(nxt);
    }
    if (extra) res.push_back(start);
    return res;
}

string gen(int n, int n1, char c1, int n2, char c2, int n3, char c3) {
    assert(n == n1 + n2 + n3);
    if (n == 0) return "";
    if (n2 > n1) {
        swap(n1, n2); swap(c1, c2);
    }
    if (n3 > n1) {
        swap(n1, n3); swap(c1, c3);
    }
    if (n == 1) return ("" + c1);
    //cout << n1 << " " << n2 << " " << n3 << endl;

    for(int e = 0; e <= n1; ++e)
        for(int g = 0; g <= n1 - e; ++g) {
            int l = n1 - e - g;
            int en3 = n2 - g + l;
            if (en3 != n3) continue;
            if (e + g < n2) continue;
            string res = "";
            vector<int> d(n1, 0);
            for(int i = e; i < e + g; ++i) d[i] = -1;
            for(int i = e + g; i < n1; ++i) d[i] = +1;
            //cout << n1 << " " << n2 << " " << n3 << " " << e << " " << g << " " << l << endl;
            for(int i = 1; i <= n1; ++i) {
                res.push_back(c1);
                int x = (i <= e + g) ? 1 : n2;
                n2 -= x;
                string p = (d[i - 1] == -1) ? alter(c2, c3, x - 1, true) : ((d[i - 1] == 0) ? alter(c2, c3, x, false) : alter(c3, c2, x, true));
                res += p;
            }
            //cout << res << endl;
            return res;
        }
    return "";
}

void change(string &s, int n1, string c1, string c2) {
    if (n1 == 0) return;
    for(int i = 0; i < s.length(); ++i) {
        if (s[i] == c2[0]) {
            int p = i + 1;
            for(int j = 0; j < n1; ++j) {
                s.insert(p, c1); ++p;
                s.insert(p, c2); ++p;
            }
            return;
        }
    }
}

bool check(char x, char y) {
    if ((x == 'O') && (y != 'B')) return false;
    if ((y == 'O') && (x != 'B')) return false;
    if ((x == 'G') && (y != 'R')) return false;
    if ((y == 'G') && (x != 'R')) return false;
    if ((x == 'V') && (y != 'Y')) return false;
    if ((y == 'V') && (x != 'Y')) return false;
    return (x != y);
}

bool check(string &s) {
    for(int i = 0; i < s.length(); ++i) {
        int j = (i + 1) % s.length();
        if (!check(s[i], s[j])) return false;
    }
    return true;
}

string run() {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    //r, y, b
    //o = r + y, g = y + b, v = r + b
    if (o > b) return "IMPOSSIBLE";
    if (g > r) return "IMPOSSIBLE";
    if (v > y) return "IMPOSSIBLE";
    //cout << r << " " << y << " " << b << endl;
    if ((o == b) && (o > 0)) {
        if (n > o + b) return "IMPOSSIBLE";
        return alter('O', 'B', o, false);
    }
    if ((g == r) && (g > 0)) {
        if (n > g + r) return "IMPOSSIBLE";
        return alter('G', 'R', g, false);
    }
    if ((v == y) && (v > 0)) {
        if (n > v + y) return "IMPOSSIBLE";
        return alter('V', 'Y', v, false);
    }
    string res = gen(b - o + r - g + y - v, b - o, 'B', r - g, 'R', y - v, 'Y');
    //cout << ">> " << res << endl;
    if (res.length() != b - o + r - g + y - v) return "IMPOSSIBLE";
    change(res, o, "O", "B");
    change(res, g, "G", "R");
    change(res, v, "V", "Y");
    assert(check(res) == true);
    return res;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cout << "Case #" << tc << ": ";
        cout << run() << endl;
    }
}
