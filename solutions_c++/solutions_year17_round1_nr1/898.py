#include "stdafx.h"
#include "R1A_A.h"

vector<pair<char, int>> GetPositions(string& s) {
    vector<pair<char, int>> res;
    for (int i = 0; i < s.size(); ++i)
        if (s[i] != '?')
            res.push_back(make_pair(s[i], i));
    return res;
}

void Print(vector<pair<char, int>> v, int c) {
    int p = 0;
    for (int i = 0; i < v.size(); ++i) {
        while (v[i].second + 1 - p) {
            cout << v[i].first;
            ++p;
        }
    }
    while (c-p) {
        cout << v[v.size() - 1].first;
        ++p;
    }
    cout << endl;
}

void R1A_A::Solve() {
    int r, c;
    cin >> r >> c;
    cout << endl;
    vector<pair<char, int>> prev, cur;
    string s;
    int rep = 1;
    for (int i = 0; i < r; ++i) {
        cin >> s;
        cur = GetPositions(s);
        if (cur.size() == 0 && prev.size() == 0)
            ++rep;
        else if (cur.size() == 0)
            Print(prev, c);
        else {
            for (int j = 0; j < rep; ++j)
                Print(cur, c);
            rep = 1;
            prev = cur;
        }
    }
}
