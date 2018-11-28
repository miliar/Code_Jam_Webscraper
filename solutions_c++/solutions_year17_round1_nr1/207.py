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

char arr[110][110];

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        int n,m;
        cin >> n >> m;
        rep(i,0,n) {
            rep(j,0,m) {
                cin >> arr[i][j];
            }
        }
        bool found = false;
        rep(i,0,n) {
            int at = 0;
            while (at < m && arr[i][at] == '?') {
                at++;
            }
            if (at == m) {
                if (found) {
                    rep(j,0,m) {
                        arr[i][j] = arr[i-1][j];
                    }
                }
                continue;
            }
            found = true;
            rep(j,0,at) {
                arr[i][j] = arr[i][at];
            }
            while (at < m) {
                if (arr[i][at] == '?' && arr[i][at-1] != '?') {
                    arr[i][at] = arr[i][at-1];
                }
                at++;
            }
        }
        for (int i = n-2; i >= 0; i--) {
            rep(j,0,m) {
                if (arr[i][j] == '?') {
                    assert(arr[i+1][j] != '?');
                    arr[i][j] = arr[i+1][j];
                }
            }
        }

        cout << "Case #" << (t+1) << ":" << endl;
        rep(i,0,n) {
            rep(j,0,m) {
                cout << arr[i][j];
            }
            cout << endl;
        }
    }

    return 0;
}

