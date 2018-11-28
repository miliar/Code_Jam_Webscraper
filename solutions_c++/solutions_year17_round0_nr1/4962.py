#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <memory>

using namespace std;

bool check(int from, vector<bool> &v) {
    for(int i = from; i < v.size(); ++i) {
        if(!v[i]) return false;
    }
    return true;
}

void flip(int from, int k, vector<bool> &v) {
    for(int i = from; i < from+k; ++i) {
        v[i] = !v[i];
    }
}

int main() {
    int t;
    cin >> t;
    for(int ts = 1; ts <= t; ++ts) {
        cout << "Case #" << ts << ": ";
        
        string s;
        int k;
        
        cin >> s >> k;
        vector<bool> a(s.length());
        for(int i = 0; i < a.size(); ++i) {
            a[i] = s[i] == '+';
        }

        int flips = 0;
        for(int i = 0; i < a.size(); ++i) {
            if(k > a.size() - i) {
                if(check(i, a)) cout << flips;
                else cout << "IMPOSSIBLE";
                cout << endl;
                break;
            } else if(!a[i]) {
                flip(i, k, a);
                ++flips;
            }
        }
    }
}
