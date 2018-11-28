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
    int k;
    cin >> s >> k;
    int ans = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '-') {
            for (int j = i; j < i + k; j++) {
                if (j >= s.size()) {
                    cout << "IMPOSSIBLE\n";
                    return;
                }
                if (s[j] == '-') {
                    s[j] = '+';
                } else {
                    s[j] = '-';
                }
            }
            ans += 1;
        }
    }
    cout << ans << '\n';
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