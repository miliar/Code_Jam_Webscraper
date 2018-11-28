#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>

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

pair<int, pair<int, int>> compute(vector<bool>& occ, bool nonempty) {
    int best_idx=-1;
    int best_min=-1;
    int best_max=-1;

    For(i, 0, occ.size()) {
        if(!nonempty || !occ[i]) {
            int ls = 0;
            while(i-ls-1 >= 0 && !occ[i-ls-1]) {
                ls++;
            }
            int rs = 0;
            while(i+rs+1 < occ.size() && !occ[i+rs+1]) {
                rs++;
            }
            int cur_min = std::min(ls, rs);
            int cur_max = std::max(ls, rs);
            if(cur_min > best_min || (cur_min == best_min && cur_max > best_max)) {
                best_idx = i;
                best_min = cur_min;
                best_max = cur_max;
            }
        }
    }

    assert(best_idx != -1);
    return make_pair(best_idx, make_pair(best_min, best_max));
}

int main() {
    int np; cin>>np;
    rep(i, np){
        int in_n, in_k; cin>>in_n>>in_k;

        int n = in_n+2;
        vector<bool> occ(n, false);
        occ[0] = occ[n-1] = true;

        pair<int, pair<int, int>> temp;
        rep(i, in_k) {
            temp = compute(occ, true);
            occ[temp.first] = true;
        } 

        cout << "Case #"<<(i+1)<<": "<<temp.second.second<<" " <<temp.second.first<<endl;;
    }
}
