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

int DP[111][111][111][5] = {};

struct solver {
    void solve() {
        // function<int (int)> dfs=[&](auto x) { return 0; };
        // auto comp=[&](auto x, auto y){ return 0; };
        int N, P;
        cin>>N>>P;
        int CNT[5] = {};
        int sum=0;
        rep(i,N){int X;cin>>X;CNT[X%P]++;sum+=X;}
        memset(DP, 0, sizeof(DP));
        DP[0][0][0][0] = 0;
        fo(a,0,CNT[1])
            fo(b,0,CNT[2])
                fo(c,0,CNT[3]) {
                    fo(rem,0,P-1) {
                        int res=DP[a][b][c][rem];
                        if (rem == 0) res++;

                        int &n1=DP[a+1][b][c][(rem+1)%P];
                        n1=max(n1, res);

                        int &n2=DP[a][b+1][c][(rem+2)%P];
                        n2=max(n2, res);

                        int &n3=DP[a][b][c+1][(rem+3)%P];
                        n3=max(n3, res);
                    }
                }
        int mini = (int)1e9;
        mini=DP[CNT[1]][CNT[2]][CNT[3]][sum%P];
        db(mini);
        cout<<CNT[0] + mini<<endl;
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
