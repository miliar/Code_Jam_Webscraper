#include<iostream>
#include<string>
#include<bitset>
#define HAPPY '+'
#define SAD '-'

using namespace std;

inline bool isTidy(string s) {
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] < s[i - 1]) return false;
    }
    return true;
}

string solve(string k) {
    while (!isTidy(k)) {
        for (int i = k.size() - 2; i >= 0; --i) {
            if (k[i] > k[i + 1]) {
                k[i] -= 1;
                for (int j = i + 1; j < k.size(); ++j) k[j] = '9';
                break;
            }
        }
    }
    int i = 0;
    for (; i < k.size() && k[i] == '0'; ++i);
    return k.substr(i);
}

int main() {
    long long t;
    string s;
    cin >> t;
    for (long long i = 1; i <= t; ++i) {
        cin >> s;
        cout << "Case #" << i << ": " << solve(s) << endl;
    }
    return 0;
}
