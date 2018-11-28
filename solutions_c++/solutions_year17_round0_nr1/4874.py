#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cmath>
using namespace std;

string flip (string s, int start, int k) {
    string res = s.substr(0, start);
    
    for (int i = start; i < start + k; i++) {
        if (s[i] == '+')
            res += '-';
        else
            res += '+';
    }
    
    res += s.substr(start+k);
    return res;
}

bool haySignoMenos (string s) {
    for (int i = 0; i < (int) s.size(); i++) {
        if (s[i] == '-')
            return true;
    }
    return false;
}

int main () {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t, k;
    cin >> t;
    
    string s;
    for (int tc = 1; tc <= t; tc++) {
        cin >> s >> k;
        int len = s.size();

        int last = len, res = 0;
        for (int i = 0; i < last; i++) {
            if (s[i] == '-') {
                s = flip(s, i, k);
                res++;
            }
            last = len-k-i;
            if (s[len-i-1] == '-') {
                s = flip(s, len-k-i, k);
                res++;
            }
        }
        
        cout << "Case #" << tc << ": ";
        if (haySignoMenos(s))
            cout << "IMPOSSIBLE" << endl;
        else
            cout << res << endl;
    }
}

