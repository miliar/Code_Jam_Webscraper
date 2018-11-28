#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <thread>
using namespace std;

string solve(const std::string &s) {
    int pre = '0';
    int l = 0, r = 0;
    while (r < s.size() && s[r] >= s[l]) {
        l = r;
        while (r < s.size() && s[r] == s[l])
            ++r;
    }

    if (r == s.size()) return s;

    std::string res = s.substr(0, l);
    res += (char)(s[l] - 1);
    res += std::string(s.size() - l - 1, '9');

    if (res.front() == '0') res.erase(res.begin());
    return res;
}

int main() {

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int casnum;
    cin >> casnum;

    for (int casid = 1; casid <= casnum; ++casid) {
        string n;
        cin >> n;
        printf("Case #%d: ", casid);
        cout << solve(n) << endl;
    }
    return 0;
}

