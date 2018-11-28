#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>

using namespace std;

int main() {
    int T; cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ": ";
        string s; int k;
        cin >> s >> k;
        int ct = 0;
        for(int i = 0; i <= s.length() - k; i++) {
            if(s[i] == '-') {
                ct++;
                for(int j = 0; j < k; j++) {
                    if(s[i+j] == '-')
                        s[i+j] = '+';
                    else
                        s[i+j] = '-';
                }
            }
        }
        bool possible = true;
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '-')
                possible = false;
        }
        if(possible)
            cout << ct << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
