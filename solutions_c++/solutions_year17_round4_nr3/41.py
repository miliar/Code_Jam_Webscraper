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


namespace sat2 {
#define sss 21010
    int n;
    vv<short> ed[sss];
    int zb[sss];
    vv<short> kol;

    void init(int n_) {
        rep (i, sss) {
            ed[i].reserve(4000);
        }
        n = n_ * 2;
        rep (i, n) ed[i].clear(), zb[i] = 0;
        kol.clear();
    }

    void dfs(int i) {
        if (zb[i] != -2) return;
        zb[i] = -1;
        fore (it, ed[i]) dfs(*it);
        kol.pb(i);
    }

    void dfs2(int i, int id) {
        if (zb[i] != -1) return;
        zb[i] = id;
        fore (it, ed[1^i]) dfs2(1^*it, id);
    }

    void clear() {
        rep (i, n) ed[i].clear();
        kol.clear();
    }

    void addcond(int x, int y) { // x or y
        ed[x^1].pb(y);
        ed[y^1].pb(x);
    }

    bool solve(vv <int> &ret) { // var * 2
        rep (i, n) zb[i] = -2;

        db("");
        rep (i, n) dfs(i);
        reverse(all(kol));

        rep (i, n) dfs2(kol[i], i);
        rep (i, n) if (zb[i] == zb[i^1]) return false;
        rep (i, n) ret.pb(zb[i] >= zb[i^1]);

        return true;
    }
};

int R,C;
char A[66][66];

int dr[]={0,0,-1,1};
int dc[]={-1,1,0,0};
vector<pair<int,int> > what;

bool hits(int r, int c, int d) {
    db(r<<" "<<c<<" "<<d);
    if (A[r][c]=='|'||A[r][c]=='-') return true;
    if (A[r][c]=='#')return false;
    if(A[r][c]=='.')
        what.push_back(pair<int,int>(r,c));
    if (A[r][c] == '/') d^=3;
    if (A[r][c] == '\\') d^=2;
    r+=dr[d];
    c+=dc[d];
    return hits(r,c,d);
}

struct solver {
    void solve() {
        sat2::init(10000);
        vector<int>possib[5000];
        // function<int (int)> dfs=[&](auto x) { return 0; };
        // auto comp=[&](auto x, auto y){ return 0; };
        cin>>R>>C;
        db("")
        fo(r,0,R+1)fo(c,0,C+1)A[r][c]='#';
        db("")
        fo(r,1,R)fo(c,1,C)cin>>A[r][c];
        db("")
        fo(r,1,R)fo(c,1,C) if(A[r][c]=='|' || A[r][c] == '-') {
            int cnt=(r-1)*50+(c-1);
            what.clear();
            int can=0;
            if (!(hits(r,c-1,0)||hits(r,c+1,1))) {
                can++;
                fore(it, what) {
                    int pkt=(it->first-1)*50+(it->second-1);
                    possib[pkt].push_back(2*cnt);
                }
                possib[(r-1)*50+(c-1)].push_back(2*cnt);
            }
            db(r<<" "<<c<<" "<<can);

            what.clear();
            if (!(hits(r-1,c,2)||hits(r+1,c,3))) {
                can++;
                fore(it, what) {
                    int pkt=(it->first-1)*50+(it->second-1);
                    possib[pkt].push_back(2*cnt+1);
                }
                possib[(r-1)*50+(c-1)].push_back(2*cnt+1);
            }
            db(r<<" "<<c<<" "<<can);

            if(can==0) {
                cout<<"IMPOSSIBLE"<<endl;
                return;
            }
            cnt++;
        }
        db("")
        fo(r,1,R)fo(c,1,C)if(A[r][c]=='.'||A[r][c]=='|'||A[r][c]=='-'){
            int pkt=(r-1)*50+(c-1);
            db(r<<" "<<c<<" "<<possib[pkt].size());
            if (possib[pkt].size() == 0) {
                cerr<<"WTF "<<r<<" "<<c<<endl;
                cout<<"IMPOSSIBLE"<<endl;
                return;
            }
            if (possib[pkt].size() == 1) {
                sat2::addcond(possib[pkt][0],possib[pkt][0]);
                db(possib[pkt][0]<<" "<<possib[pkt][0]);
            }
            if (possib[pkt].size() == 2) {
                sat2::addcond(possib[pkt][0],possib[pkt][1]);
                db(possib[pkt][0]<<" "<<possib[pkt][1]);
            }
        }
        db("")
        vector<int>ret;
        if (!sat2::solve(ret)) {
            cout<<"IMPOSSIBLE"<<endl;
            return;
        }
        db("")
        fo(r,1,R)fo(c,1,C)if(A[r][c]=='-'||A[r][c]=='|'){
            int pkt=(r-1)*50+(c-1);
            if (ret[2*pkt]==1)A[r][c]='-';
            if (ret[2*pkt]==0)A[r][c]='|';
        }
        db("")
        cout<<"POSSIBLE"<<endl;
        db("")
        fo(r,1,R){
            fo(c,1,C) {
                cout<<A[r][c];
            }
            cout<<endl;
        }
        db("")
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
