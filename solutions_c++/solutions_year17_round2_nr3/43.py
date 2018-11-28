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

#define NNN 111
#define QQQ 111

struct solver {
    void solve() {
        int N, Q;
        cin>>N>>Q;
        ld E[NNN],S[NNN];
        ld D[NNN][NNN]={};
        ld D2[NNN][NNN]={};
        fo(i,1,N){cin>>E[i]>>S[i];}
        fo(i,1,N)fo(j,1,N)cin>>D[i][j];
        fo(k,1,N)fo(i,1,N)fo(j,1,N) {
            if(D[i][k]>0&&D[k][j]>0) {
                ld ndi=D[i][k]+D[k][j];
                if (D[i][j]==-1||D[i][j]>ndi) {
                    D[i][j]=ndi;
                }
            }
        }
        fo(i,1,N)fo(j,1,N) {
            if(D[i][j]>0 && D[i][j]<=E[i]) {
                ld new_time=D[i][j]/S[i];
                if (D2[i][j] <= 0 || D2[i][j] > new_time) D2[i][j]=new_time;
            }
        }
        fo(k,1,N)fo(i,1,N)fo(j,1,N) {
            if(D2[i][k]>0&&D2[k][j]>0) {
                ld ndi=D2[i][k]+D2[k][j];
                if (D2[i][j]<=0||D2[i][j]>ndi) {
                    D2[i][j]=ndi;
                }
            }
        }
        fo(k,1,Q){int U,V;cin>>U>>V;
            cout<<" "<<D2[U][V];
        }
        cout<<endl;
        if(cond)
        fo(i,1,N){fo(j,1,N) {
                cerr<<D2[i][j]<<" ";
            }
            cerr<<endl;
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
        if (gcj) cout << "Case #" << i << ":";
        solver s;
        s.solve();
    }
	return 0;
}
