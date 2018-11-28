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

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int mn = 0;
        rep(i,0,size(s) - k + 1) {
            if (s[i] == '-') {
                mn++;
                rep(j,0,k) {
                    s[i+j] = s[i+j] == '+' ? '-' : '+';
                }
            }
        }
        bool any = false;
        rep(i,0,size(s)) {
            if (s[i] == '-') {
                any = true;
                break;
            }
        }
        cout << "Case #" << (t+1) << ": ";
        if (any) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << mn << endl;
        }
    }

    return 0;
}

