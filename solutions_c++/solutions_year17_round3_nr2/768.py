#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <map>
#include <utility>
#include <iomanip>

#define FOR(i,n) for(int i=0;i<int(n);++i)

using namespace std;

using ull = unsigned long long;

void test() {
    int na,nb; cin >> na >> nb;
    vector<tuple<int ,int, char>> in(na+nb);
    
    int ta=720, tb=720;
    FOR (i,na) {
        cin >> get<0>(in[i]);
        cin >> get<1>(in[i]);
        get<2>(in[i]) = 'A';
        ta -= get<1>(in[i]) - get<0>(in[i]);
    }
    FOR (i, nb) {
        cin >> get<0>(in[i+na]);
        cin >> get<1>(in[i+na]);
        get<2>(in[i+na]) = 'B';
        tb -= get<1>(in[i+na]) - get<0>(in[i+na]);
    }
    
    sort(in.begin(), in.end());
    
    vector<pair<int, char>> me;
    
    int res = 0;
    
//    me.emplace_back(720-get<0>(me.back())+get<0>(me[0]),
//                    get<0>(me[0])
//                    );
//    me.emplace_back(720-get<0>(me.back()),get<0>(me.back()));
    FOR(i, in.size()) {
        if (get<2>(in[i]) != get<2>(in[(i+1)%in.size()])) {
            res++;
            continue;
        }
        
        auto x = get<0>(in[(i+1)%in.size()])- get<1>(in[i]);
        if (x < 0) x+= 1440;
        me.emplace_back(x, get<2>(in[i]));
    }
    
    sort(me.begin(), me.end());
//    cout << me.size() << endl;
    FOR(i, me.size()) {
        if (me[i].second == 'A') {
            if (me[i].first <= ta) {
                ta -= me[i].first;
            } else {
                res += 2;
//                assert(me[i].first <= tb);
                tb -= me[i].first + ta;
                ta = 0;
            }
        } else if (me[i].second == 'B') {
            if (me[i].first <= tb) {
                tb -= me[i].first;
            } else {
                res += 2;
//                assert(me[i].first <= ta);
                
                ta -= me[i].first + tb;
                tb = 0;
            }
        } else {
            cout << "-" << (int)me[i].second << "-"<< endl;
            assert(false);
        }
    }
    
    cout << res << endl;
    
}

int main() {
    
    int tn; cin >> tn;
    FOR (t, tn) {
        cerr << t << endl;
        cout << "Case #" << t+1 << ": ";
        test();
    }
    
    return 0;
}
