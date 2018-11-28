#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solve(std::string str, int k) {
    int res = 0;
    
    for (int i = 0; i != str.size() - k + 1; ++i) {
        if (str[i] == '-') {
            for (int j = 0; j != k; ++j) {
                str[i + j] = str[i + j] == '-' ? '+' : '-';
            }
            ++res;
        }
    }
    
    return str.find('-') == string::npos ? res : -1;
}

int main() {
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        string str;
        int k;
        cin >> str >> k;
        int res = solve(str, k);
        
        cout << "Case #" << test + 1 << ": ";
        if (res == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << res;
        }
        
        cout << '\n';
    }
    
    return 0;
}