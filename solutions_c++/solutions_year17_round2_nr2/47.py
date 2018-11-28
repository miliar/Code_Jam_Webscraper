#include <iostream>
#include <algorithm>

using namespace std;

int n, r, o, y, g, b, v;

void solve(int x) {
    cin >> n >> r >> o >> y >> g >> b >> v;
    int u = (r>0)+(y>0)+(b>0);
    cout << "Case #" << x << ": ";
    if (b == o && !g && !r && !y && !v) {
        for (int i = 0; i < b; i++) cout << "BO";
        cout << "\n";
        return;
    }
    if (g == r && !b && !o && !y && !v) {
        for (int i = 0; i < g; i++) cout << "GR";
        cout << "\n";
        return;
    }
    if (y == v && !b && !o && !g && !r) {
        for (int i = 0; i < y; i++) cout << "YV";
        cout << "\n";
        return;
    }
    if (u == 1) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    if ((o && o > b-1) || (g && g > r-1) || (v && v > y-1)) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    b -= o; r -= g; y -= v;
    string s = "";
    int a = 0;
    if (r >= y && r >= b) {
        for (int i = 0; i < r; i++) s += "R";
        r = 0;
    } else if (y >= r && y >= b) {
        for (int i = 0; i < y; i++) s += "Y";
        y = 0;
    } else if (b >= r && b >= y) {
        for (int i = 0; i < b; i++) s += "B";
        b = 0;
    }
    string s2 = "";
    while (r) {
        if (s == "") break;
        s2 += "R";
        s2 += s[s.size()-1];
        s.pop_back();
        r--;
    }
    while (y) {
        if (s == "") break;
        s2 += "Y";
        s2 += s[s.size()-1];
        s.pop_back();
        y--;
    }
    while (b) {
        if (s == "") break;
        s2 += "B";
        s2 += s[s.size()-1];
        s.pop_back();
        b--;
    }
    if (s != "") {
        cout << "IMPOSSIBLE\n";
        return;
    }
    reverse(s2.begin(),s2.end());
    string s3 = "";
    while (r) {
        if (s2 == "") break;
        s3 += "R";
        s3 += s2[s2.size()-1];
        s2.pop_back();
        r--;
    }
    while (y) {
        if (s2 == "") break;
        s3 += "Y";
        s3 += s2[s2.size()-1];
        s2.pop_back();
        y--;
    }
    while (b) {
        if (s2 == "") break;
        s3 += "B";
        s3 += s2[s2.size()-1];
        s2.pop_back();
        b--;
    }
    while (s2 != "") {
        s3 += s2[s2.size()-1];
        s2.pop_back();
    }
    for (int i = 0; i < s3.size()-1; i++) {
        if (s3[i] == s3[i+1]) {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    if (s3[0] == s3[s3.size()-1]) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    string s4;
    for (int i = 0; i < s3.size(); i++) {
        if (s3[i] == 'B' && o) {
            for (int i = 0; i < o; i++) s4 += "BO";
            o = 0;
        }
        if (s3[i] == 'R' && g) {
            for (int i = 0; i < g; i++) s4 += "RG";
            g = 0;
        }
        if (s3[i] == 'Y' && v) {
            for (int i = 0; i < v; i++) s4 += "YV";
            v = 0;
        }
        s4 += s3[i];
    }
    cout << s4 << "\n";
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
