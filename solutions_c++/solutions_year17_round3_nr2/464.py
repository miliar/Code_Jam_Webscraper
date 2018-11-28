#include <bits/stdc++.h>
using namespace std;
char enl = '\n';
#define rep(i, from, to) for (int i = from; i < (to); ++i)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int, int>> vii;
typedef long double ld;

void solve() {

    int ac, aj;
    cin >> ac >> aj;

    int oo = 1e9;

    vector<vector<vi>> minper(24*60+1, vector<vi>(721, vi(4, oo)));

    vector<bool> mc(24*60+1);
    vector<bool> mj(24*60+1);



    rep(i,0,ac) {
        int c, d;
        cin >> c >> d;
        rep(j,c,d) {
            mc[j] = true;
        }
    }
    rep(i,0,aj) {
        int c, d;
        cin >> c >> d;
        rep(j,c,d) {
            mj[j] = true;
        }
    }

    if (!mj[0]) {
        minper[0][1][0] = 0;
        minper[0][1][1] = oo;
    }
    if (!mc[0]) {
        minper[0][0][2] = oo;
        minper[0][0][3] = 0;
    }


    rep(m,1,24*60+1) {
        rep(c, 0, 721) {
            rep(bj,0,2) {
                minper[m][c][2*1+bj] = min(minper[m-1][c][2*1+bj], minper[m-1][c][bj] + 1);
                if (c > 0) {
                    minper[m][c][bj] = min(minper[m-1][c-1][bj], minper[m-1][c-1][2*1 + bj] + 1);
                } else {
                    minper[m][0][bj] = oo;
                }
                if (mc[m]) {
                    minper[m][c][2*1+bj] = oo;
                }
                if (mj[m]) {
                    minper[m][c][bj] = oo;
                }
            }
        }
    }

    int allmin = oo;
    rep(i,0,4) {
        if (i == 2 || i == 1) {
            allmin = min(minper[24*60-1][720][i]+1, allmin);
        } else {
            allmin = min(minper[24*60-1][720][i], allmin);
        }
    }

    cout << allmin << endl;




}








    
        




int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << (i+1) << ": ";
        solve();
    }



    return 0;
}
