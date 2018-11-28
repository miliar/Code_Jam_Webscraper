#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <iomanip>

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

map< pair<vector<int>, pair<int, int> >, int> mem;

int rec(vector<int> mod, int rem, int p) {
    auto key = make_pair(mod, make_pair(rem, p));
    if(mem.count(key)) {
        return mem[key];
    }
    

    int res = 0;
    rep(i, mod.size()) {
        if(mod[i]) {
            vector<int> cur_mod = mod;
            cur_mod[i]--;
            int hit = rec(cur_mod, (rem - i + p) % p, p);
            res = std::max(res, hit + ((rem == 0) ? 1 : 0));
        }
    }
    mem[key] = res;
    return res;
}

int main() {
    int np; cin>>np;
    rep(i, np){
        cout << "Case #"<<(i+1)<<": ";

        int n,p; cin>>n>>p;
        vector<int> mod;
        rep(i, p) {
            mod.push_back(0);
        }
        rep(i, n) {
            int cur; cin>>cur;
            mod[cur % p]++;
        }

        cout << rec(mod, 0, p) << endl;;
    }
}
