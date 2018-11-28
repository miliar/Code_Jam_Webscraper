#include <iostream>
#include <vector>
#include <string>

using namespace std;

string solve(string num) {
    for (int i = num.size() - 1; i >= 0; --i) {
        for (int j = i + 1; j != num.size(); ++j) {
            if (num[i] > num[j]) {
                num[i] -= 1;
                for (int k = i + 1; k != num.size(); ++k) {
                    num[k] = '9';
                }
            }
        }
    }
    
    if (num[0] == '0') return num.substr(1, num.size() - 1);
    return num;
}

bool check(const std::string &num) {
    for (int i = 1; i != num.size(); ++i) {
        if (num[i] < num[i - 1]) {
            return false;
        }
    }
    
    return true;
}

string solve_slow(const std::string &num) {
    long long n = stol(num);
    while (!check(to_string(n))) --n;
    return to_string(n);
}

void test(int maxn) {
    for (int i = 1; i != maxn; ++i) {
        if (i % 1000 == 0) cout << i << '\n';
        
        string str = to_string(i);
        string a = solve_slow(str);
        string b = solve(str);
        
        if (a != b) {
            cout << str << ' ' << a << ' ' << b << '\n';
            return;
        }
    }
}

int main() {
    // test(100000);
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        string str;
        cin >> str;
        cout << "Case #" << test + 1 << ": " << solve(str) << '\n';
    }
    
    return 0;
}