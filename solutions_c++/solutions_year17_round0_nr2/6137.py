#include <iostream>
#include <string>

using namespace std;


bool is_tidy(string n) {
    for (int i = 1; i < n.size(); ++i) {
        if (n[i] < n[i-1])
            return false;
    }
    return true;
}

void make_nine(string& n, int p) {
    for (int i = p; i < n.size(); ++i)
        n[i] = '9';
}

unsigned long long maximum_tidy(unsigned long long n) {
    string s = to_string(n);

    while (is_tidy(s) == false) {
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] < s[i-1]) {
                s[i-1] = s[i-1] - 1;
                make_nine(s, i);
                break;
            }
        }

    }

    return stoull(s);
}

int main() {
    int T;
    cin >> T;

    for (int kase = 1; kase <= T; ++kase) {
         unsigned long long n;
         cin >> n;

         printf("Case #%d: %llu\n", kase, maximum_tidy(n));
    }

    return 0;
}
