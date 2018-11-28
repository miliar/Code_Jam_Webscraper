#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define div   ___div
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }

/* Author: Van Hanh Pham */

/** END OF TEMPLATE - ACTUAL SOLUTION COMES HERE **/

const string NO_ANSWER = "IMPOSSIBLE";

string findString(int r, int y, int b) {
    string res;
    if (r > 0) {
        res.push_back('R');
        r--;
    } else if (y > 0) {
        res.push_back('Y');
        y--;
    } else if (b > 0) {
        res.push_back('B');
        b--;
    }

    while (r > 0 || y > 0 || b > 0) {
        if (res.back() == 'R') res.push_back(y > b || (y == b && res[0] == 'Y') ? 'Y' : 'B');
        else if (res.back() == 'Y') res.push_back(b > r || (b == r && res[0] == 'B') ? 'B' : 'R');
        else res.push_back(r > y || (r == y && res[0] == 'R') ? 'R' : 'Y');
        if (res.back() == 'R') r--;
        else if (res.back() == 'Y') y--;
        else if (res.back() == 'B') b--;

        if (r < 0 || y < 0 || b < 0) return NO_ANSWER;
    }

    if (res.size() > 1 && res.front() == res.back()) return NO_ANSWER;

    return res;
}

int element(char c) {
    int res = 0;
    if (c == 'R' || c == 'O' || c == 'V') res |= MASK(0);
    if (c == 'Y' || c == 'G' || c == 'O') res |= MASK(1);
    if (c == 'B' || c == 'V' || c == 'G') res |= MASK(2);
    return res;
}

void check(const string &s, int r, int o, int y, int g, int b, int v) {
    assert(s.size() == r + o + y + g + b + v);
    map<char, int> cnt;
    FORE(it, s) cnt[*it]++;
    assert(cnt['R'] == r);
    assert(cnt['O'] == o);
    assert(cnt['Y'] == y);
    assert(cnt['G'] == g);
    assert(cnt['B'] == b);
    assert(cnt['V'] == v);

    REP(i, s.size()) {
        int a = element(s[i]);
        int b = element(s[(i + 1) % s.size()]);
        assert((a & b) == 0);
    }
}

string duplicate(int n, string s) {
    string res;
    REP(love, n) res += s;
    return res;
}

string solve(int r, int o, int y, int g, int b, int v) {
    int sum = r + o + y + g + b + v;

    if (sum == g + r) return g == r ? duplicate(g, "GR") : NO_ANSWER;
    if (sum == v + y) return v == y ? duplicate(v, "VY") : NO_ANSWER;
    if (sum == o + b) return o == b ? duplicate(o, "OB") : NO_ANSWER;

    if ((g >= r && g > 0) || (v >= y && v > 0) || (o >= b && o > 0)) return NO_ANSWER;

    string arrange = findString(r - g, y - v, b - o);
    if (arrange == NO_ANSWER) return NO_ANSWER;

    if (g > 0) {
        string tmp = duplicate(g, "RG") + "R";
        REP(i, arrange.size()) if (arrange[i] == 'R') {
            arrange = arrange.substr(0, i) + tmp + arrange.substr(i + 1);
            break;
        }
    }
    if (v > 0) {
        string tmp = duplicate(v, "YV") + "Y";
        REP(i, arrange.size()) if (arrange[i] == 'Y') {
            arrange = arrange.substr(0, i) + tmp + arrange.substr(i + 1);
            break;
        }
    }
    if (o > 0) {
        string tmp = duplicate(o, "BO") + "B";
        REP(i, arrange.size()) if (arrange[i] == 'B') {
             arrange = arrange.substr(0, i) + tmp + arrange.substr(i + 1);
             break;
        }
    }

    return arrange;
}

int main(void) {
    int t; cin >> t;
    REP(pmp, t) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        string tmp = solve(r, o, y, g, b, v);
        if (tmp != NO_ANSWER) check(tmp, r, o, y, g, b, v);
        printf("Case #%d: %s\n", pmp + 1, tmp.c_str());
    }

    return 0;
}

/*** LOOK AT MY CODE. MY CODE IS AMAZING :D ***/
