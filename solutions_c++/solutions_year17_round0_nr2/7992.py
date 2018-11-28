#include <bits/stdc++.h>
using namespace std;
bool isTide(long long n) {
    long long last = n % 10;
    n /= 10;
    while (n) {
        if (n % 10 > last) {
            return 0;
        }
        last = n % 10;
        n /= 10;
    }
    return 1;
}
int main() {
    
    ifstream in("in.txt");
    ofstream out("out.txt");
    long long T, k;
    in >> T;
    for (int i = 0; i < T; ++i) {
        in >> k;
        if (isTide(k)) {
            out << "Case #" << i + 1 << ": " << k << endl;
            continue;
        }
        string s = to_string(k);
        int idx = 0;
        for (int j = 0; j < s.size() - 1; ++j) {
            if (s[j] - '0' > s[j + 1] - '0') {
                idx = j;
                break;
            }
        }
        for (int j = idx; j >= 0; --j) {
            if (s[idx] == s[j]) {
                idx = j;
            } else break;
        }
        for (int j = idx + 1; j < s.size(); ++j) {
            s[j] = '9';
        }
        s[idx] -= 1;
        k = stoll(s);
        out << "Case #" << i + 1 << ": " << k << endl;
        
    }
}