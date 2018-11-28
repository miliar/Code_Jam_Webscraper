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


int solve(std::string &s, int k) {
    int num = 0;

    for (int i = 0; i <= s.size() - k; ++i) {
        if (s[i] == '+') continue;

        ++num;
        for (int j = i; j < i + k; ++j)
            if (s[j] == '+') s[j] = '-';
            else s[j] = '+';
    }

    for (int i = 0; i < s.size(); ++i)
        if (s[i] == '-')
            return -1;
    return num;
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int casnum;
    cin >> casnum;

    for(int casid = 1; casid <= casnum; ++casid) {
        string s;
        int k;
        cin >> s >> k;

        int ret = solve(s, k);
        printf("Case #%d: ", casid);
        cout << (ret == -1 ? "IMPOSSIBLE" : to_string(ret)) << endl;
    }
    return 0;
}

