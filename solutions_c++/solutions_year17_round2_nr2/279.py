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

int main() {

    srand(0);

#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("brackets.in", "r", stdin);
    //freopen("brackets.out", "w", stdout);
#endif

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cout << "Case #" << tt << ": ";

        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;

        bool bad = false;

        vector<string> red(r, "R"), yellow(y, "Y"), blue(b, "B");
        while (o) {
            if (blue.size() < 2) {
                break;
            }
            o--;
            auto uu = blue.back();
            blue.pop_back();
            auto vv = blue.back();
            blue.pop_back();
            blue.pb(uu + "O" + vv);
        }

        while (g) {
            if (red.size() < 2) {
                break;
            }
            g--;
            auto uu = red.back();
            red.pop_back();
            auto vv = red.back();
            red.pop_back();
            red.pb(uu + "G" + vv);
        }

        while (v) {
            if (yellow.size() < 2) {

                break;
            }
            v--;
            auto uu = yellow.back();
            yellow.pop_back();
            auto vv = yellow.back();
            yellow.pop_back();
            yellow.pb(uu + "V" + vv);
        }

        string ans;

        if (v + o + g > 1) {
            bad = true;
        } else if (v == 1) {
            if (red.size() + blue.size()) {
                bad = true;
            } else {
                if (yellow.size() == 1) {
                    ans = "V" + yellow[0];
                } else {
                    bad = true;
                }
            }
        } else if (g == 1) {
            if (yellow.size() + blue.size()) {
                bad = true;
            } else {
                if (red.size() == 1) {
                    ans = "G" + red[0];
                } else {
                    bad = true;
                }
            }
        } else if (o) {
            if (red.size() + yellow.size()) {
                bad = true;
            } else {
                if (blue.size() == 1) {
                    ans = "O" + blue[0];
                } else {
                    bad = true;
                }
            }
        } else {

            vector<vector<string>> a({red, blue, yellow});
            sort(a.begin(), a.end(), [](const vector<string> &u, const vector<string> &v) {
                return u.size() < v.size();
            });

            if (a[2].size() > 1 && a[2].size() > a[0].size() + a[1].size()) {
                bad = true;
            }

            if (!bad) {
                int extra = (int) a[2].size() - (int) a[1].size() - (int) a[0].size();
                extra = -extra;


                for (int i = 0; i < a[2].size(); i++) {
                    ans += a[2][i];
                    if (a[1].size()) {
                        ans += a[1].back();
                        a[1].pop_back();
                    } else {
                        ans += a[0].back();
                        a[0].pop_back();
                    }
                    if (extra) {
                        --extra;
                        ans += a[0].back();
                        a[0].pop_back();
                    }
                }


            }
        }


        if (bad) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }


    return 0;
}
