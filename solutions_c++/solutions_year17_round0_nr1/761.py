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

int main(int argc, char *argv[]) {
    ios_base::sync_with_stdio(false);

    int ntest; cin >> ntest;
    REPU(it, 1, ntest + 1) {
        string s; int k; cin >> s >> k;
        const int n = s.size();
        vector<int> states(n);
        REPU(i, 0, n) states[i] = s[i] == '+' ? 1 : 0;
        bool ok(true);
        int done = 0;
        REPU(i, 0, n) if (states[i] == 0) {
            int to = i + k;
            if (to > n) {
                ok = false; break;
            }
            done++;
            REPU(j, i, to) states[j] ^= 1;
        }
        if (ok) printf("Case #%d: %d\n", it, done);
        else printf("Case #%d: IMPOSSIBLE\n", it);
    }

	return 0;
}
