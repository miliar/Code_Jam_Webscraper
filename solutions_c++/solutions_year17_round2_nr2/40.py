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
        auto print=[&](vector<int> x) {
            string PAT = "ROYGBV";
            fore (it, x) {
                cout<<PAT[*it];
            }
        };
        int count[16]={};
        int N; cin>>N;
        rep(i,6)cin>>count[i];
        string sim = "";
        int last=8;
        int zero=0;rep(i,6)if(count[i]==0)zero++;
        //1 -> 4
        //3 -> 6
        //5 -> 8
        int pairs[3][2]={{1,4},{3,0},{5,2}};
        rep(d,3) {
            int le=pairs[d][0]; int ri=pairs[d][1];
            if(zero==4&&count[le]>0&&count[ri]>0&&count[le]==count[ri]) {
                vector<int>res;
                rep(x,count[le]){res.push_back(le);res.push_back(ri);}
                print(res);

                return;
            }
        }
        int bestX=8;
        rep (i,6)if(i!=last&&count[i]>count[bestX])bestX = i;

        vector<int>res;
        int reduced[6] = {};
        rep(d,3) {
            int le=pairs[d][0]; int ri=pairs[d][1];
            if (count[le] > 0 && count[le] >= count[ri]) {
                cout << "IMPOSSIBLE";
                return;
            }
            count[ri] -= count[le];
            reduced[ri] += count[le];
            N -= 2*count[le];
            count[le] = 0;
        }
        rep(i,6)db(i<<" "<<count[i]);
        while (N > 0) {
            if (last != bestX && count[bestX] > 0) {
                count[bestX]--;
                last=bestX;
                N--;
                res.push_back(bestX);
                continue;
            }

            int best=8;
            rep (i,6)if(i!=last&&i!=bestX&&count[i]>count[best])best = i;

            if (best == 8) {
                cout << "IMPOSSIBLE";
                return;
            }
            count[best]--;
            N--;
            res.push_back(best);
            last=best;
        }
        if (res[0] == res.back()) {
            cout << "IMPOSSIBLE";
            return;
        }
        vector<int>res2;
        fore(it, res) {
            res2.push_back(*it);
            rep(x,reduced[*it]) {
                res2.push_back((*it + 3)%6);
                res2.push_back(*it);
            }
            reduced[*it] = 0;
        }
        print(res2);
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
