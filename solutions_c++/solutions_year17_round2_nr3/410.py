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

const int N = 105;
double e[N], s[N], d[N][N], dp[N][N], dist[N];

int main(int argc, char *argv[]) {
    ios_base::sync_with_stdio(false);

    int ntest; cin >> ntest;
    REPU(it, 1, ntest + 1) {
        int n, q; cin >> n >> q;
        REPU(i, 0, n) {
            cin >> e[i] >> s[i];
        }
        REPU(i, 0, n) REPU(j, 0, n) {
			cin >> d[i][j];
		}
		REPU(k, 0, n) REPU(i, 0, n) REPU(j, 0, n) {
			if (d[i][k] >= 0 && d[k][j] >= 0) {
				if (d[i][j] < 0) d[i][j] = d[i][k] + d[k][j];
				else amin(d[i][j], d[i][k] + d[k][j]);
			}
		}
		REPU(i, 0, n) REPU(j, 0, n) {
			if (i == j) dp[i][j] = 0;
			else if (d[i][j] > 0 && e[i] >= d[i][j]) {
				dp[i][j] = d[i][j] / s[i];
			}
			else dp[i][j] = -1;
		}
		REPU(k, 0, n) REPU(i, 0, n) REPU(j, 0, n) {
			if (dp[i][k] >= 0 && dp[k][j] >= 0) {
				if (dp[i][j] < 0) dp[i][j] = dp[i][k] + dp[k][j];
				else amin(dp[i][j], dp[i][k] + dp[k][j]);
			}
		}
		printf("Case #%d:", it);
        REPU(i, 0, q) {
            int u, v; cin >> u >> v;
            printf(" %.10f", dp[u - 1][v - 1]);
        }
		puts("");
    }

	return 0;
}
