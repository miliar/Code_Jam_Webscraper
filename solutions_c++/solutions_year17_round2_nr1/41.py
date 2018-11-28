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

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

struct solver {
    void solve() {
        ld D; int N;
        cin>>D>>N;
        ld slower = (ld)0;
        rep(i,N) {
            ld K, S;
            cin>>K>>S;
            slower=max(slower, (D-K)/S);
        }              ;
        db(D<<" "<<N<<" "<<slower);
        cout<<D/slower;
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
        if (gcj) cout << endl;
    }
	return 0;
}
