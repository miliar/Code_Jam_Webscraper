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

int main() {
    int np; cin>>np;
    rep(i, np){
        string s_raw; cin >> s_raw;
        vector<bool> s;
        for(auto& c : s_raw) {
            s.push_back(c=='+');
        }
        
        int k; cin >> k;
        int n = s.size();
        bool good = true;
        int ans = 0;
        rep(i, n) {
            if(!s[i]) {
                int upper = i+k;
                if(i+k <= n) {
                    ans++;
                    For(j, i, upper) {
                        s[j] = !s[j];
                    }
                } else {
                    good = false;
                }
            }
        }

        cout << "Case #"<<(i+1)<<": ";
        if(good) {
            cout << ans;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
}
