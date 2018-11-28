#define STRINGIZE(x) #x
#define STRINGIZE2(x) STRINGIZE(x)
#define FP STRINGIZE2(FILEPATH)

#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
using namespace std;

long long n;

bool read() {
    cin >> n;
    return true;
}

long long naive(long long n) {
    string s;
    while (n > 0) {
        s = to_string(n);
        
        bool ok = true;
        for (int i = 0; i + 1< s.size(); i++) {
            if (s[i] > s[i + 1]) {
                ok = false;
                break;
            }
        }
        
        if (ok) {
            return n;
        }
        
        n--;
    }
    
    return n;
}

void solve(int test) {
    printf("Case #%d: ", test + 1);
    
    string s = to_string(n);
    
    long long result = 0;
    if (s.size() == 1) {
        result = n;
    } else {
        for (int pref = 0; pref <= s.size(); pref++) {
            bool ok = true;
            long long cur = 0;
            
            for (int i = 0; i < pref; i++) {
                if (i && s[i - 1] > s[i]) {
                    ok = false;
                }
                cur = cur * 10 + int(s[i] - '0');
            }
            
            if (!ok) {
                break;
            }
            
            if (pref < s.size()) {
                if (s[pref] >= '0' && (pref == 0 || s[pref - 1] <= s[pref] - 1)) {
                    cur = cur * 10 + int(s[pref] - '0' - 1);
                    for (int i = pref + 1; i < s.size(); i++) {
                        cur = cur * 10 + 9;
                    }
                    
                    result = max(result, cur);
                }
            } else {
                result = max(result, cur);
            }
        }
    }
    
    cout << result << endl;
}

int main() {
    freopen(FP "input.txt", "rt", stdin);
    freopen(FP "output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    for (int test = 0; test < testCount; test++) {
        assert(read());
        solve(test);
    }
    
    return 0;
}
