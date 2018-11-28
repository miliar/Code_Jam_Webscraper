#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define FOR2(i, s, n) for (int i = (s); i <= (n); ++i)
#define REP(i, n) FOR(i, 0, n)

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef vector<int> vi;


int R, C;
string cakes[30];
set<char> alphabets;
vector<char> alps;

bool try_fill(int r, int c, char ch) {
    int sr = r, er = r;
    int sc = c, ec = c;

    REP(i, R) {
        REP(j, C) {
            if (cakes[i][j] == ch) {
                sr = min(i, sr);
                er = max(i, er);

                sc = min(j, sc);
                ec = max(j, ec);
            }
        }
    }

    FOR2(i, sr, er) {
        FOR2(j, sc, ec) {
            if (cakes[i][j] != '?' && cakes[i][j] != ch) return false;
        }
    }

    FOR2(i, sr, er) {
        FOR2(j, sc, ec) {
            cakes[i][j] = ch;
        }
    }
    return true;
}

void solve()
{
    alphabets.clear();
    alps.clear();

    cin >> R >> C;
    REP(i, R) cin >> cakes[i];

    REP(i, R) {
        REP(j, C) {
            if (cakes[i][j] != '?' && alphabets.count(cakes[i][j]) == 0) {
                alphabets.insert(cakes[i][j]);
                alps.pb(cakes[i][j]);
            }
        }
    }

    REP(i, R) {
        REP(j, C) {
            if (cakes[i][j] == '?') {
                REP(k, alps.size()) {
                    if(try_fill(i,j, alps[k])) break;
                }                
            }
        }
    }

    cout << endl;
    REP(i, R) {
        cout << cakes[i] << endl;
    }


}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}