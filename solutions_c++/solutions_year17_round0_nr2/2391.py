#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>

#define FOR(i,n) for(int i=0;i<int(n);++i)

using namespace std;

using ull = unsigned long long;

void test() {
    string s; cin >> s;
    auto st = stoull(s);
    for(int i=0;i<s.size()-1 && i>=0;++i) {
        //cout << i << " " << s << endl;
        if (s[i] > s[i+1]) {
            if (s[i] > '1') {
                s[i]--;
                fill(s.begin()+i+1, s.end(), '9');
                i -= 2;
            } else {
                s[i] = '9';
                s.pop_back();
                fill(s.begin(), s.end(), '9');
                break;
            }
        }
    }
    
    assert(stoull(s) <= st);
    FOR (i, s.size()-1) {
        //cout << i << " " << s << endl;
        assert (s[i] <= s[i+1]);
    }
    cout << s << endl;
}

int main() {
    
    int tn; cin >> tn;
    FOR (t, tn) {
        cout << "Case #" << t+1 << ": ";
        test();
    }
    
    return 0;
}
