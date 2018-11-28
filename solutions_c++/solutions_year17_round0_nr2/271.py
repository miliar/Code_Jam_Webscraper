#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>
#include <ctime>
#include <limits>
#include <tuple>
#include <complex>
#include <numeric>
#include <future>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = acos(-1.0);

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}

template<typename T>
bool chmin(T &x, T y) {
    if (x > y) {
        x = y;
        return true;
    }
    return false;
}

template<typename T>
bool chmax(T &x, T y) {
    if (x < y) {
        x = y;
        return true;
    }
    return false;
}

template<typename U, typename V>
ostream &operator<<(ostream &s, const pair<U, V> &x) {
    s << "(" << x.fst << ", " << x.snd << ")";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const vector<U> &x) {
    s << "[";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "]";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const set<U> &x) {
    s << "{";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "}";
    return s;
}

template<int sz>
ostream operator<<(ostream &s, const bitset<sz> &x) {
    for (int i = 0; i < sz; i++) {
        s << x[i];
    }
    return s;
}


//--------------------------------------------------------------------------

bool good(string s) {
    for (int i = 0; i + 1 < s.size(); i++) {
        if (s[i] > s[i + 1]) {
            return false;
        }
    }
    return true;
}

int main(int argc, char* argv[]) {

    srand(time(NULL));

#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("sum.in", "r", stdin);
    //freopen("sum.out", "w", stdout);
#endif

    int t;
    cin >> t;
    int tt = 0;
    while (t--) {
        tt++;
        cout << "Case #" << tt << ": ";

        string s;
        cin >> s;

        if (good(s)) {
            cout << s << endl;
            continue;
        }

        ll val = stoll(s);
        ll pw = 1;
        ll ans = 0;
        for (int i = 0; i < 19; i++) {
            ll nval = val - pw;
            nval -= val % pw;
            nval += pw - 1;
            if (nval > 0 && nval <= val && good(to_string(nval))) {
                chmax(ans, nval);
            }
            pw *= 10;
        }

        if (s.size() > 1) {
            s.pop_back();
            fill(s.begin(), s.end(), '9');
            chmax(ans, stoll(s));
        }

        cout << ans << endl;
    }

    return 0;
}
