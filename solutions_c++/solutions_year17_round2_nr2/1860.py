#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <sstream>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cstdlib>
using namespace std;

bool valid(int a, int b) {
    //cout << a << ' ' << b << endl;
    return a >= b + 1 || b == 0;
}

int getRemain(int a, int b) {
    if (b == 0) return a;
    return a - (b + 1);
}

string convertToString(vector<char> & v) {
    string s(v.size(), 'a');
    for (int i = 0; i < v.size(); ++i) {
        s[i] = v[i];
    }
    return s;
}

string makeColor(int a, int b, char c1, char c2) {
    if (b == 0) {
        return "";
    }
    //cout << a << ' ' << b << ' ' << c1 << ' '  << c2 << endl;
    vector<char> v;
    for (int i = 0; i < b * 2 + 1; ++i) {
        v.push_back(i % 2 == 0 ? c1 : c2);
    }

    return convertToString(v);
}

typedef pair<int, char> pr;

bool create(int r1, int r2, int r3, char c1, char c2, char c3, char start, char end, vector<char> &v) {
    vector<pr> a(3);
    a[0] = pr(r1, c1);
    a[1] = pr(r2, c2);
    a[2] = pr(r3, c3);
    int prev = start;
    while (a[0].first > 1 || a[1].first > 1 || a[2].first > 1) {
        sort(a.begin(), a.end());
        int index = a[2].second == prev ? 1 : 2;
        if (a[index].first == 0) {
            return false;
        }
        v.push_back(a[index].second);
        --a[index].first;
        prev = a[index].second;
    }
    int remain = 0;
    for (int i = 0; i < 3; ++i) {
        if (a[i].first > 0) {
            ++remain;
            v.push_back(a[i].second);
        }
    }
    v.push_back(end);
    v.insert(v.begin(), start);
    for (int i = 0; i < 24; ++i) {
        next_permutation(v.end() - remain - 1, v.end() - 1);
        bool done = true;
        for (int j = max((int)v.size() - remain - 2, 0); j < v.size() - 1; ++j) {
            //cerr  << "?? " << j << ' ' << v[j] << " vs " << v[j+1]<<endl;
            if (v[j] == v[j + 1] || (j > 0 && v[j] == v[j - 1])) {
                //cout << "?? " << v[j] << " vs " << v[j+1]<<endl;
                done = false;
            }
        }
        if (done) {
            v.pop_back();
            v.erase(v.begin());
            return true;
        }
    }
    return false;
}

string solve(int r1, int r2, int r3, char c1, char c2, char c3, string s1, string s2, string s3) {
    //cerr << r1 << ' ' << r2 << ' ' << r3 << ' ' << c1 << ' ' << c2 << ' ' << c3 << ' ' << s1 << ' '<< s2 << ' ' << s3 << endl;
    if (r2 > r1 && r2 >= r3) {
        return solve(r2, r1, r3, c2, c1, c3, s2, s1, s3);
    }
    if (r3 > r1 && r3 >= r2) {
        return solve(r3, r1, r2, c3, c1, c2, s3, s1, s2);
    }

    if ((s1.size() == 0) + (s2.size() == 0) + (s3.size() == 0) == 1 &&
        r1 == 0 && r2 == 0 && r3 == 0) {
        return "IMPOSSIBLE";
    }
    if (r1 == 0 && r2 == 0 && r3 == 0) {
        return s1 + s2 + s3;
    }

    if (s1.size() == 0 && s2.size() == 0 && s3.size() == 0) {
        vector<char> v;
        if (create(r1 - 1, r2, r3, c1, c2, c3, c1, c1, v)) {
            return c1 + convertToString(v);
        }
    }
    
    if (s2.size() && s3.size()) {
        vector<char> v;
        if (create(r1, r2, r3, c1, c2, c3, s2[0], s3[0], v)) {
            return s1 + s2 + convertToString(v) + s3;
        } else {
            return "IMPOSSIBLE";
        }
    }
    if (s1.size() && s3.size()) {
        vector<char> v;
        if (create(r1, r2, r3, c1, c2, c3, s1[0], s3[0], v)) {
            return s1 + s2 + s3 + convertToString(v);
        } else {
            return "IMPOSSIBLE";
        }
    }
    if (s1.size() && s2.size()) {
        vector<char> v;
        if (create(r1, r2, r3, c1, c2, c3, s1[0], s2[0], v)) {
            return s1 + convertToString(v) + s2 + s3;
        } else {
            return "IMPOSSIBLE";
        }
    }
    if (s1.size()) {
        vector<char> v;
        if (create(r1, r2, r3, c1, c2, c3, s1[0], s1[0], v)) {
            return s1 + convertToString(v);
        } else {
            return "IMPOSSIBLE";
        }
    }
    if (s2.size()) {
        vector<char> v;
        if (create(r1, r2, r3, c1, c2, c3, s2[0], s2[0], v)) {
            return s2 + convertToString(v);
        } else {
            return "IMPOSSIBLE";
        }
    }
    if (s3.size()) {
        vector<char> v;
        if (create(r1, r2, r3, c1, c2, c3, s3[0], s3[0], v)) {
            return s3 + convertToString(v);
        } else {
            return "IMPOSSIBLE";
        }
    }
    return "IMPOSSIBLE";
}

bool validate(string s, int n) {
    if (s == "IMPOSSIBLE" ) return true;
    if (s.size() != n) {
        return false;
    }
    for (int i = 0; i < s.size(); ++i) {
        char c = s[(i + 1) % s.size()];
        if (s[i] == c) {
            return false;
        }
    }
    return true;
}

int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        cout << "Case #" << cc << ": ";
        string sol;
        int n;
        int a[6];
        cin >> n;
        for (int i = 0; i < 6; ++i) {
            cin >> a[i];
        }
        //  R, O, Y, G, B, and V.
        //  0  1  2  3  4      5

        int numOfZero = 0;
        for (int i = 0; i < 6; ++i) {
            if (a[i] == 0) {
                ++numOfZero;
            }
        }
        if (a[4] == a[1] && a[1] && numOfZero == 4) {
            //cerr << "??" << endl;
            string s1 = makeColor(a[4], a[1], 'B', 'O');
            cout << s1.substr(1) << endl;
        } else if (a[0] == a[3] && a[3] && numOfZero == 4) {
            string s1 = makeColor(a[0], a[3], 'R', 'G');
            cout << s1.substr(1) << endl;
        } else if (a[2] == a[5] && a[5] && numOfZero == 4) {
            string s1 = makeColor(a[2], a[5], 'Y', 'V');
            cout << s1.substr(1) << endl;
        } else if (!valid(a[4], a[1]) ||
            !valid(a[0], a[3]) ||
            !valid(a[2], a[5])) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            string s1 = makeColor(a[4], a[1], 'B', 'O');
            string s2 = makeColor(a[0], a[3], 'R', 'G');
            string s3 = makeColor(a[2], a[5], 'Y', 'V');
            int r1 = a[4] + a[1] - s1.size(); // B
            int r2 = a[0] + a[3] - s2.size(); // R
            int r3 = a[2] + a[5] - s3.size(); // Y
            string sol = solve(r1, r2, r3, 'B', 'R', 'Y', s1, s2, s3);
            if (!validate(sol, n)) {
                cerr << "?? " <<a[0] << ' '<< a[2] << ' ' << a[4] << endl;
                cerr << "err: " << sol << endl;
                throw 0;
            }
            //if (sol == "IMPOSSIBLE") {
            //    cerr << "?? " <<a[0] << ' '<< a[2] << ' ' << a[4] << endl;
            //}
            cout << solve(r1, r2, r3, 'B', 'R', 'Y', s1, s2, s3) << endl;
        }
        
    }
}
