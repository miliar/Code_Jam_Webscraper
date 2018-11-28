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

int solve(string s, int k) {

    int n = s.length();
    vi a(n);
    forn (i, n)
        a[i] = (s[i] == '+');
    int ans = 0;
    forn (i, n - k + 1) {
        if (!a[i]) {
            ans++;
            forn (j, k)
                a[i + j] ^= 1;
        }
    }
    if (find(all(a), 0) != a.end())
        return -1;
    return ans;
}

int main() {
    //auto start = chrono::system_clock::now();
    string name = "A-large";
    string path = "";

    freopen((path + name + ".in").c_str(), "r", stdin);
    freopen((path + name + ".out").c_str(), "w", stdout);

    int test_cases;
    cin >> test_cases;
    vector<future<int>> futures(test_cases);

    for (int test_case = 1; test_case <= test_cases; test_case++) {
        string s;
        int k;
        cin >> s >> k;

        futures[test_case - 1] = async(launch::async, solve, s, k);
    }

    for (int test_case = 1; test_case <= test_cases; test_case++) {
        int res = futures[test_case - 1].get();
        cout << "Case #" << test_case << ": " << fixed << setprecision(10) << (res >= 0 ? to_string(res) : "IMPOSSIBLE") << endl;
        cout.flush();
    }

    fclose(stdout);
    fclose(stdin);
    //cerr << chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now() - start).count() << endl;
    return 0;
}
