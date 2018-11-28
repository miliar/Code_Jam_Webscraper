#include <cstdio>
#include <string>
#include <iostream>

long long stingToLL(std::string const& a) {
    long long ret = 0;
    for (int i = 0; i < a.length(); i++) {
        ret *= 10;
        ret += a[i]-'0';
    }
    return ret;
}

bool isOK(std::string const &a, std::string const &b) {
    long long lla = stingToLL(a.c_str());
    long long llb = stingToLL(b.c_str());
    return lla <= llb;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int w = 1; w <= T; w++) {
        std::string s;
        std::cin >> s;
        std::string ans = s;
        for (int i = 0; i < s.length(); i++) {
            if (i != 0)
                ans[i] = std::max(ans[i-1], s[i]);
            else
                ans[i] = s[i];
            for (int j = i + 1; j < s.length(); j++) {
                ans[j] = ans[i];
            }
            if (!isOK(ans, s)) {
                ans[i]--;
                for (int j = i + 1; j < s.length(); j++) {
                    ans[j] = '9';
                }
                break;
            }
        }
        printf("Case #%d: %lld\n", w, stingToLL(ans.c_str()));
    }
    return 0;
}