#ifdef NALP_PROJECT
#pragma hdrstop
#else
#define _SECURE_SCL 0
#endif

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:200000000")

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cassert>

#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <bitset>
#include <memory.h>

#include <iostream>
#include <fstream>
#include <sstream>

#ifdef _WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define y1 YYY1
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define Cerr cerr
#define Endl endl

template<typename T> inline T Abs(T x) { return (x >= 0) ? x : -x; }
template<typename T> inline T Sqr(T x) { return x * x; }
template<typename T> inline string ToString(T x) { stringstream st; st << x; string s; st >> s; return s; }
template<typename T> inline int Bit(T mask, int b) { return (b >= 0 && (mask & (T(1) << b)) != 0) ? 1 : 0; }
template<typename T1, typename T2> std::ostream& operator<<(std::ostream &out, const pair<T1, T2>& a) { out << "(" << a.first << ", " << a.second << ")"; return out; }
template<typename T> std::ostream& operator<<(std::ostream &out, const vector<T>& a) { out << "[" << a.size() << "]{ "; forn(i, a.size()) { out << a[i] << " "; } out << "}"; return out; }

inline int NextInt() { int x; if (scanf("%d", &x) != 1) throw; return x; }
inline int64 NextInt64() { int64 x; if (scanf(LLD, &x) != 1) throw; return x; }
inline double NextDouble() { double x; if (scanf("%lf", &x) != 1) throw; return x; }

const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double EPS = 1E-9;
const long double PI = 3.1415926535897932384626433832795;

const int MAXN = 110;

using TRESULT = int;

int N, P, grams[MAXN], package[MAXN][MAXN];
pair<int, int> a[MAXN][MAXN];


pair<int, int> CalcRange(const int64 p, const int64 g) {
    pair<int, int> ans(+INF, -INF);
    for (int c = 1; c <= 3 * p; ++c) {
        const int64 need = c * g;
        if (9 * need <= p * 10 && p * 10 <= 11 * need) {
            ans.second = max(ans.second, c);
            ans.first = min(ans.first, c);
        }
    }

    return ans;
}

int Get(int mask, vector<int>& d);

int Get1(int mask, vector<int>& d, int x, int y, int minX, int maxX) {
    if (minX > maxX) {
        return -INF;
    }

    if (y == P) {
        return -INF;
    }

    if (x == N) {
        return 1 + Get(mask, d);
    }

    const int pos = x * P + y;
    int ans = Get1(mask, d, x, y + 1, minX, maxX);
    if (Bit(mask, pos)) {
        ans = max(ans, Get1(mask ^ (1 << pos), d, x + 1, 0, max(minX, a[x][y].first), min(maxX, a[x][y].second)));
    }
    return ans;
}

int Get(int mask, vector<int>& d) {
    int& ans = d[mask];
    if (ans != -1) {
        return ans;
    }

    ans = max(0, Get1(mask, d, 0, 0, -INF, +INF));
    return ans;
}

TRESULT StupidSolution() {
    vector<int> d(1 << (N * P), -1);
    return Get((1 << (N*P)) - 1, d);
}

pair<int, int> GetBetter(const multiset<pair<int, int>>& st, int value) {
    pair<int, int> result(-INF, +INF);
    for (const auto& x : st) {
        if (x.first <= value && value <= x.second && x.second < result.second) {
            result = x;
        }
    }

    return result.first < 0 ? mp(+1, -1) : result;
}

bool Fetch(vector<multiset<pair<int, int>>>& l, int value) {
    vector<pair<int, int>> c(l.size());
    forn(i, l.size()) {
        const pair<int, int> pick = GetBetter(l[i], value);
        if (pick.first > pick.second) return false;
        c[i] = pick;
    }

    forn(i, l.size()) {
        l[i].erase(l[i].find(c[i]));
    }

    return true;
}

void Solve(bool skipThisTest) {
    if (true) {
        cerr << "\tinput mode: read test." << endl;
        N = NextInt();
        P = NextInt();
        forn(i, N) {
            grams[i] = NextInt();
        }

        forn(i, N) {
            forn(j, P) {
                package[i][j] = NextInt();
            }
        }

        if (skipThisTest) return;
    } else {
        cerr << "\tinput mode: generated test." << endl;

        N = 3;
        P = 5;
        forn(i, N) {
            grams[i] = rand() % 100 + 1;
        }

        forn(i, N) {
            forn(j, P) {
                package[i][j] = rand() % 100 + 1;
            }
        }
    }

    set<int> st;
    vector<multiset<pair<int, int>>> l(N);
    forn(i, N) {
        forn(j, P) {
            a[i][j] = CalcRange(package[i][j], grams[i]);
            if (a[i][j].first <= a[i][j].second) {
                st.insert(a[i][j].first);
                l[i].insert(a[i][j]);
            }
        }
    }

    TRESULT ans = 0;
    while (!st.empty()) {
        while (Fetch(l, *st.begin())) {
            ++ans;
        }

        st.erase(st.begin());
    }

    cout << ans << endl;

    cerr << "\tclever answer is '" << ans << "'." << endl;
    if (N * P <= 16) {
        const TRESULT stupidAnswer = StupidSolution();
        cerr << "\tstupid answer is '" << stupidAnswer << "'." << endl;
        assert(ans == stupidAnswer);
    }
}

int main(int argc, char * argv[]) {
#ifdef NALP_PROJECT
    freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
#else
#endif

    int minTest = 1, maxTest = INF;
    if (argc == 3) {
        minTest = atoi(argv[1]);
        maxTest = atoi(argv[2]);
    }

    cout.precision(10);
    cout.setf(ios::fixed);

    cerr.precision(10);
    cerr.setf(ios::fixed);

    srand((unsigned int)time(0));
    const int tests = NextInt();
    clock_t totalStartTime = clock();
    for (int test = 1; test <= tests; test++) {
        clock_t startTime = clock();
        cerr << "Case #" << test << endl;
        const bool skipThisTest = (test < minTest || test > maxTest);
        if (!skipThisTest) cout << "Case #" << test << ": ";
        Solve(skipThisTest);

        char formattedTime[100];
        const clock_t time = clock() - startTime;
        sprintf(formattedTime, "%d.%03d", int(time / CLOCKS_PER_SEC), int(time % CLOCKS_PER_SEC));
        cerr << "time for test is " << formattedTime << " s." << endl << endl;
    }

    char formattedTime[100];
    const clock_t totalTime = clock() - totalStartTime;
    sprintf(formattedTime, "%d.%03d", int(totalTime / CLOCKS_PER_SEC), int(totalTime % CLOCKS_PER_SEC));
    cerr << string(20, '=') << endl;
    cerr << "TOTAL TIME IS " << formattedTime << " s." << endl;

    return 0;
}
