#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = 2147483647;

bool lt(vector<int> a, vector<int> b) {
    assert(size(a) == size(b));
    rep(i,0,size(a)) {
        if (a[i] != b[i]) {
            return a[i] < b[i];
        }
    }
    return true;
}

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        string S;
        cin >> S;

        vector<int> s(size(S), 0);
        rep(i,0,size(S)) {
            s[i] = S[i] - '0';
        }

        vector<int> cur(size(s), 0);
        int d = 0;
        rep(at,0,size(s)) {
            int now = d,
                def = d;
            while (now <= 9) {
                rep(k,at,size(s)) {
                    cur[k] = now;
                }
                if (lt(cur, s)) {
                    def = now;
                    now++;
                } else {
                    break;
                }
            }
            cur[at] = def;
            d = def;
        }
        cout << "Case #" << (t+1) << ": ";
        int at = 0;
        while (cur[at] == 0) at++;
        rep(i,at,size(cur)) {
            cout << cur[i];
        }
        cout << endl;
    }
    return 0;
}

