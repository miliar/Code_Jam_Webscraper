#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <ctime>
#include <cstdlib>
#include <unordered_set>
#include <deque>
#include <queue>

using namespace std;

typedef long long ll;

int main() {
    int tests;
    cin >> tests;
    for (int test_id = 0; test_id < tests; ++test_id) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        
        int result = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '-') {
                
                if (i + k - 1 >= s.length()) {
                    result = -1;
                    break;
                }
                
                for (int j = 0; j < k; ++j) {
                    if (s[i + j] == '-')
                        s[i + j] = '+';
                    else
                        s[i + j] = '-';
                }
                
                result += 1;
            }
        }
        
        if (result == -1)
            cout << "Case #" << test_id + 1 << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << test_id + 1 << ": " << result << endl;
    }
}
