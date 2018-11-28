#include <cstdio>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>
#include <set>
#include <deque>
#include <utility>
#include <chrono>
#include <sstream>
#include <iomanip>

#define INF 1 << 30
#define MOD 1000000007
#define PI 3.14159265358979
#define rep(i, n) for (int (i) = 0; (i) < (int)(n); (i)++)
#define reu(i, l, r) for (int (i) = (int)(l); (i) < (int)(r); (i)++)
#define D(x) cout << x << endl
#define d(x) cout << x
#define all(x) (x).begin(), (x).end()
#define pub(x) push_back(x)
#define pob() pop_back()
#define puf(x) push_front(x)
#define pof() pop_front()
#define mp(x, y) make_pair((x), (y))
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<long long> vll;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef pair<int, int> pii;
typedef pair<long, long> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
template<typename T, typename U> inline void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if (x < y) x = y; }

static const int dx[] = {0, 0, 1, -1};
static const int dy[] = {-1, 1, 0, 0};

void solve(int t) {
        int r, c;
        cin >> r >> c;
        string s[30];
        rep (i, r) {
                cin >> s[i];
        }
        string ans[30];
        rep(i, r) {
                int p = -1;
                rep(j, c) {
                        if (j == c - 1 && s[i][j] == '?') {
                                if ( p != -1) {
                                        for (int k = j; k > p; k--) {
                                                s[i][k] = s[i][p];
                                        }
                                } else {
                                        break;
                                }
                        }
                        if (s[i][j] != '?') {
                                int pre = p;
                                p = j;
                                for (int k = p; k > pre; k--) {
                                        s[i][k] = s[i][p];
                                }
                        }
                }
        }

        bool flag[30];
        bool yet = false;
        rep (i, r) {
                flag[i] = true;
        }
        rep(i, r) {
                int p = -1;
                rep(j, c) {
                        if (j == c - 1 && s[i][j] == '?') {
                                if ( p != -1) {
                                        for (int k = j; k > p; k--) {
                                                s[i][k] = s[i][p];
                                        }
                                } else {
                                        yet = true;
                                        flag[i] = false;
                                        break;
                                }
                        }
                        if (s[i][j] != '?') {
                                int pre = p;
                                p = j;
                                for (int k = p; k > pre; k--) {
                                        s[i][k] = s[i][p];
                                }
                        }
                }
        }

        D("Case #" << t << ":");
        bool first = false;
        string prev;
        rep(i, r) {
                if (!flag[i] && !first) {
                        continue;
                }
                else if (flag[i]) {
                        if (!first && i != 0) {
                                first = true;
                                rep (k, i + 1) {
                                        D(s[i]);
                                }
                                prev = s[i];
                        } else {
                                first = true;
                                D(s[i]);
                                prev = s[i];
                        }
                } else {
                        D(prev);
                }
        }
        return;
}

int main() { 
        int t;
        cin >> t;
        rep (i, t) {
                solve(i + 1);
        }
        return 0;
}

