#include <bits/stdc++.h>
using namespace std;

#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define FORE(it, a) for (auto it = a.begin(); it != a.end(); ++it)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())

vector<string> split(const string &s, char c) {
    vector<string> v;
    stringstream ss(s);
    string x;
    while (getline(ss, x, c)) v.push_back(x);
    return v;
}

#define DEBUG(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

void err(vector<string>::iterator it) {}

template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
    cerr << "[DEBUG] " << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
    err(++it, args...);
}

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) { return (a < b) ? a : b; }
template<class T, class U> inline T tmax(T a, U b) { return (a > b) ? a : b; }
template<class T, class U> inline void amax(T &a, U b) { if (b > a) a = b; }
template<class T, class U> inline void amin(T &a, U b) { if (b < a) a = b; }
template<class T> inline T tabs(T a) { return (a > 0) ? a : -a; }
template<class T> T gcd(T a, T b) { while (b != 0) { T c = a; a = b; b = c % b; } return a; }

const int N = 101;
int g[N], dp3[N][N], dp4[N][N][N];

int main(int argc, char *argv[]) {
    ios_base::sync_with_stdio(false);

    int ntest; cin >> ntest;

    REPU(i, 0, N) REPU(j, 0, N) {
        dp3[i][j] = 0;
        REPU(k, 0, N) dp4[i][j][k] = 0;
    }

    REPU(i, 0, N) REPU(j, 0, N) {
        if (i == 0 && j == 0) dp3[i][j] = 0;
        if (i > 0) {
            int v = (i - 1 + 2 * j) % 3;
            amax(dp3[i][j], dp3[i - 1][j] + (v == 0));
        }
        if (j > 0) {
            int v = (i + 2 * (j - 1)) % 3;
            amax(dp3[i][j], dp3[i][j - 1] + (v == 0));
        }
        REPU(k, 0, N) {
            if (i == 0 && j == 0 && k == 0) dp4[i][j][k] = 0;
            if (i > 0) {
                int v = (i - 1 + 2 * j + 3 * k) % 4;
                amax(dp4[i][j][k], dp4[i - 1][j][k] + (v == 0));
            }
            if (j > 0) {
                int v = (i + 2 * (j - 1) + 3 * k) % 4;
                amax(dp4[i][j][k], dp4[i][j - 1][k] + (v == 0));
            }
            if (k > 0) {
                int v = (i + 2 * j + 3 * (k - 1)) % 4;
                amax(dp4[i][j][k], dp4[i][j][k - 1] + (v == 0));
            }
        }
    }

    REPU(it, 1, ntest + 1) {
        int n, p; cin >> n >> p;
        REPU(i, 0, n) cin >> g[i];
        int ans = 1;
        if (p == 2) {
            int odd = 0;
            REPU(i, 0, n) {
                if (g[i] & 1) odd++;
            }
            int res = 1 + min(n - 1, n - odd) + max(0, odd - 1) / 2;
            amax(ans, res);
        }
        else if (p == 3) {
            vector<int> f(3, 0);
            REPU(i, 0, n) {
                f[g[i] % 3]++;
            }
            int res = min(n, dp3[f[1]][f[2]] + f[0]);
            amax(ans, res);
        }
        else if (p == 4) {
            vector<int> f(4, 0);
            REPU(i, 0, n) {
                f[g[i] % 4]++;
            }
            int res = min(n, dp4[f[1]][f[2]][f[3]] + f[0]);
            amax(ans, res);
        }
        printf("Case #%d: %d\n", it, ans);
    }

	return 0;
}
