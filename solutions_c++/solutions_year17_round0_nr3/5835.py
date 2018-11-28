#include <cassert>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <numeric>
#include <bitset>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <functional>
#include <cstring>
#include <ctime>
#include <memory.h>
#include <future>
#include <iomanip>

#define y1 AAA_BBB
#define y0 AAA_AAA

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef vector<int> vi;
typedef vector<i64> vi64;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef vector<vi64> vvi64;

template <class T> T inline sqr(T x) {
    return x * x;
}

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;
const int inf  = 1e9;

pii solve(int n, int k) {
    pii ans;
    set<int> a;
    forn (t, k) {
        int mins = -1, maxs;
        int mi;

        int ls, rs;
        forn (i, n) {
            if (!a.empty()) {
                auto it = a.lower_bound(i);
                if (it != a.end() && (*it == i)) {
                    ls = -2;
                    rs = -2;
                }
                else {
                    if (it == a.end()) {
                        rs = n - 1 - i;
                    }
                    else {
                        rs = *it - i - 1;
                    }

                    if (it != a.begin()) {
                        --it;
                        ls = i - *it - 1;
                    } else {
                        ls = i;
                    }
                }
            }
            else {
                ls = i;
                rs = n - 1 - i;
            }
            int Mins = min(ls, rs);
            int Maxs = max(ls, rs);
            if (mp(mp(Mins, Maxs), -i) > mp(mp(mins, maxs), -mi)) {
                mins = Mins;
                maxs = Maxs;
                mi = i;
            }
        }
        a.insert(mi);
        if (t == k - 1) {
            ans.fi = maxs;
            ans.se = mins;
        }
    }
    return ans;
}

int main() {
    //auto start = chrono::system_clock::now();
    string name = "C-small";    string path = "";

    freopen((path + name + ".in").c_str(), "r", stdin);
    freopen((path + name + ".out").c_str(), "w", stdout);

    int test_cases;
    cin >> test_cases;
    vector<future<pii>> futures(test_cases);

    for (int test_case = 1; test_case <= test_cases; test_case++) {
        int n , k;
        cin >> n >> k;
        futures[test_case - 1] = async(launch::async, solve, n, k);
    }

    for (int test_case = 1; test_case <= test_cases; test_case++) {
        pii res = futures[test_case - 1].get();
        cout << "Case #" << test_case << ": " << fixed << setprecision(10) << res.first << " " << res.second << endl;
        cout.flush();
    }

    fclose(stdout);
    fclose(stdin);
    //cerr << chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now() - start).count() << endl;
    return 0;
}
