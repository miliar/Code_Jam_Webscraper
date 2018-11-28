#include <iostream>
#include <string>
#include <vector>
#include <cmath>


#define FOR(i,n) for(int i=0;i<int(n);++i)

using namespace std;


void test() {
    string s; int k;
    cin >> s >> k;
    
    s = '+' + s + '+';
    vector<int> st(s.size()-1, 0);
    int res = 0;
    FOR(i, s.size()-1) {
        string pos{s.begin()+i, s.begin()+i+2};
        if (pos == "+-" || pos == "-+") {
            if (i<k || !st[i-k]) {
                st[i] = 1;
                res++;
            }
        } else {
            if (i>=k && st[i-k]) {
                st[i] = 1;
                res++;
            }
        }
    }
    
    for (auto i: vector<int>{max(st.end()-k+1, st.begin()),st.end()}) {
        if (i) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    
    cout << res << endl;
}

int main() {
    
    int tn; cin >> tn;
    FOR (t, tn) {
        cout << "Case #" << t+1 << ": ";
        test();
    }
    
    return 0;
}
