#include <bits/stdc++.h>
using namespace std;

const int NMAX = 1024;

int tsk;
vector<char> mn;

int main() {
    //freopen("dat.in", "r", stdin);
    //freopen("dat.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    string res, str;
    int l, r;
    char val;
    bool flag;

    cin >> tsk;
    for (int t = 1; t <= tsk; ++t) {
        cout << "Case #" << t << ": ";
        cin >> str;
        res.resize(str.size());

        flag = false;
        for (int l = 0, r = 0; r < str.size(); ++r) {
            if (flag)
                res[r] = '9';
            else {
                if (str[r] == str[l])
                    res[r] = str[r];
                else if (str[l] < str[r]) {
                    res[r] = str[r];
                    l = r; }
                else {
                    --res[l];
                    r = l;
                    flag = true; } } }

        flag = false;
        for (int i = 0; i < res.size(); ++i) {
            flag|= (res[i] != '0');
            if (flag)
                cout << res[i]; }
        cout << '\n'; }

    return 0; }
