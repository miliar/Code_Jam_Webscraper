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

void fill(vector<string>& s, int x, int y) { 
    int lmost = y, rmost = y, umost = x, bmost = x;
    for (int i = lmost; i >= 0; i--) {
        bool good = true;
        for (int h = i; h <= rmost; h++) {
            for (int v = bmost; v <= umost; v++) {
                if (s[v][h] != '?' && s[v][h] != s[x][y]) {
                    good = false;
                }
            }
        }
        if (good) 
            lmost = i;
        else
            break;
    }
    for (int i = rmost; i < s[0].sz; i++) {
        bool good = true;
        for (int h = lmost; h <= i; h++) {
            for (int v = bmost; v <= umost; v++) {
                if (s[v][h] != '?' && s[v][h] != s[x][y]) {
                    good = false;
                }
            }
        }
        if (good) 
            rmost = i;
        else
            break;
    }
    for (int i = bmost; i >= 0; i--) {
        bool good = true;
        for (int h = lmost; h <= rmost; h++) {
            for (int v = i; v <= umost; v++) {
                if (s[v][h] != '?' && s[v][h] != s[x][y]) {
                    good = false;
                }
            }
        }
        if (good) 
            bmost = i;
        else
            break;
    }
    for (int i = umost; i < s.sz; i++) {
        bool good = true;
        for (int h = lmost; h <= rmost; h++) {
            for (int v = bmost; v <= i; v++) {
                if (s[v][h] != '?' && s[v][h] != s[x][y]) {
                    good = false;
                }
            }
        }
        if (good) 
            umost = i;
        else
            break;
    }

    for (int i = bmost; i <= umost; i++) {
        for (int j = lmost; j <= rmost; j++) {
            s[i][j] = s[x][y];
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    //////////////start//////////////

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cout << "Case #" << tc << ": " << endl;

        int R, C;
        cin >> R >> C;
        vector<string> vs(R);
        rep(i, R) {
            cin >> vs[i];
        }

        set<char> checked;
        rep(i, R) {
            rep(j, C) {
                if (checked.find(vs[i][j]) == checked.end()) {
                    checked.insert(vs[i][j]);
                    fill(vs, i, j);
                }
            }
        }

        rep(i, R) {
            cout << vs[i] << endl;
        }
    }

    //////////////end////////////////
    return 0;
}
