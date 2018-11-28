#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

long long solve(long long n) {
    string s = to_string(n);
    int i = 1;
    for (; i < s.size(); ++i) {
        if (s[i-1] > s[i]) {
            break;
        }
    }
    if (i == s.size()) {
        //cout << n << endl;
        //return true;
        return n;
    }
    s[i-1] -= 1;
    while (i < s.size()) s[i++] = '9';
    return solve(stoll(s));
}

int main() {
    int t;
    cin >> t;
    int i = 0;
    while (i++ < t) {
        long long k;
        cin >> k;
        cout << "Case #" << i << ": " << solve(k) << endl;
    }
}
