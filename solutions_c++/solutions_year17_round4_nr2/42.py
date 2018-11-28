#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define rep(i,b) for(auto i=(0);i<(b);++i)
#define fo(i,a,b) for(auto i=(a);i<=(b);++i)
#define ford(i,a,b) for(auto i=(a);i>=(b);--i)
#define fore(a,b) for(auto a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
#define i2 array<int,2>
#define i3 array<int,3>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

struct solver {
    void solve() {
        int CNT[1111]={};
        int POS[1111]={};
        // function<int (int)> dfs=[&](auto x) { return 0; };
        // auto comp=[&](auto x, auto y){ return 0; };
        int N,C,M;
        cin>>N>>C>>M;
        rep(i,M) {
            int P,B;
            cin>>P>>B;
            CNT[B]++;
            POS[P]++;
        }
        int rides=0;
        fo(c,1,C)rides=max(CNT[c], rides);
        fo(res,rides,M) {
            int left=0;
            bool ok=1;
            int had_to_add = 0;
            fo(pos,1,N) {
                int reminder=POS[pos]-res;
                left-=reminder;
                if (reminder > 0) {
                    if (reminder>left) {
                        ok=0;
                        break;
                    }
                    left-=reminder;
                    had_to_add+=reminder;
                }
                else if(reminder<0) {
                    left+=-reminder;
                }
            }
            if (ok) {
                cout<<res<<" "<<had_to_add<<endl;
                return;
            }
        }
    }
};

const int multi = 0;
const int gcj = 1;

int main(int argc, char ** argv) {
    ios::sync_with_stdio(false); cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    std::cout.setf(ios::fixed);
    std::cout.precision(10);
    // auto f = [&](){return 0;};

    int t;
    if (multi | gcj)
        cin >> t;
    else
        t = 1;

    fo (i, 1, t) {
        if (cond) cerr << __LINE__ << " " << i << endl;
        if (gcj) cout << "Case #" << i << ": ";
        solver s;
        s.solve();
    }
	return 0;
}
