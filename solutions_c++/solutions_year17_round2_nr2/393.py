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

typedef pair<int, char> P;

int main(int argc, char *argv[]) {
    ios_base::sync_with_stdio(false);

    int ntest; cin >> ntest;
    REPU(it, 1, ntest + 1) {
        int n, r, o, y, g, b, v; cin >> n >> r >> o >> y >> g >> b >> v;
        int mx = max(1, n / 2);
        string res(n, '.');
        vector<P> st;
        st.push_back(P(r, 'R'));
        st.push_back(P(y, 'Y'));
        st.push_back(P(b, 'B'));
        sort(ALL(st)); reverse(ALL(st));
        char key = st[0].second;
        if (st[0].first > mx) res = "IMPOSSIBLE";
        else {
            int idx = 0;
            char pre = '.';
            while (idx < n) {
                sort(ALL(st), [&key](P p1, P p2) {
                    if (p1.first != p2.first) return p1.first > p2.first;
                    if (p1.second == key) return true;
                    if (p2.second == key) return false;
                    return p1.second < p2.second;
                });
                char nxt = '.';
                REPU(i, 0, 3) if (st[i].second != pre) {
                    st[i].first -= 1;
                    nxt = st[i].second;
                    break;
                }
                pre = nxt;
                assert(nxt != '.');
                res[idx++] = nxt;
            }
            REPU(i, 0, n) {
                int j = (i + 1) % n;
                if (res[i] == '.' || res[i] == res[j]) assert(0);
            }
        }
		printf("Case #%d: %s\n", it, res.c_str());
    }

	return 0;
}
