#include <stdio.h>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <numeric>
using namespace std;

void solve()
{
    string s;
    cin >> s;
    int i = 0;
    while (i < s.size() - 1 && s[i] <= s[i + 1]) {
        ++i;
    }
    if (i == s.size() - 1) {
        cout << s << '\n';
        return;
    }
    while (i > 0 && s[i] == s[i - 1]) {
        --i;
    }
    if (s[i] > '1') {
        for (int j = 0; j < s.size(); j++) {
            if (j < i) {
                cout << s[j];
            }
            if (j == i) {
                cout << char(s[j] - 1);
            }
            if (j > i) {
                cout << '9';
            }
        }
        cout << '\n';
        return;
    }
    for (int j = 0; j < s.size() - 1; j++) {
        cout << '9';
    }
    cout << '\n';
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}