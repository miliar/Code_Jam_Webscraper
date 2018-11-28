#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define popc32(x) __builtin_popcount(x)
#define popc64(x) __builtin_popcountll(x)
#define MOD 1000007
#define INF 1e9
#define EPS 1e-9

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;

static const double PI = 2 * acos(0);

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    //////////////start//////////////

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cout << "Case #" << tc << ": ";

        ll in;
        cin >> in;
        string numstr = to_string(in);

        bool finished = false;
        while (!finished) {
            if (numstr.size() == 1)
                break;
            for (int i = numstr.sz-1; i >= 1; i--) {
                if (numstr[i] < numstr[i-1]) {
                    for (int j = i-1; j >= 0; j--) {
                        if (j == 0 && numstr[j] == '1') {
                            numstr.erase(numstr.begin());
                            rep(i, numstr.sz) {
                                numstr[i] = '9';
                            }
                        }
                        else if (numstr[j] > '0') {
                            numstr[j]--;
                            for (int k = j+1; k < numstr.sz; k++)
                                numstr[k] = '9';
                            break;
                        }
                    }
                }
                else if (i == 1) {
                    finished = true;
                }
            }
        }

        cout << numstr << endl;
    }

    //////////////end////////////////
    return 0;
}
