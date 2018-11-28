#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>

using namespace std;


int main() {
    freopen("input_a_1.txt", "r", stdin);
    freopen("output_a_1.txt", "w", stdout);
    int testCases;
    cin >> testCases;
    for (int testCase = 1; testCase <= testCases; testCase++) {
        cout << "Case #" << testCase << ": ";
        
        int n;
        string s;
        cin >> s >> n;
        int ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            if (s[i] == '-') {
                if (i + n > s.size()) {
                    ans = -1;
                    break;
                }
                ans++;
                for (int j = i; j < i + n; j++) {
                    s[j] = (s[j] == '+' ? '-' : '+');
                }
            }
        }

        if (ans == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    } 
    return 0;
}