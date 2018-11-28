
#include <vector>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <set>
//#include "optimization.h"

using namespace std;

int c[256];

int main(){
    c['-'] = '+';
    c['+'] = '-';
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int t, n;
    string s;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        int ans = 0;
        cin >> s >> n;
        for (int i = 0; i < s.size(); i++)
            if (s[i] == '-' && i + n - 1 < s.size()){
                for (int j = 0; j < n; j++)
                    s[i+j] = c[s[i + j]];
                ans++;
            }
        bool bb = false;
        for (int i = 0; i < s.size(); i++)
            if (s[i] != '+')
                bb = true;
        cout << "Case #" << tt << ": ";
        if (bb)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << "\n";
    }
    return 0;
}
