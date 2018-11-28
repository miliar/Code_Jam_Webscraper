#pragma region template
#define _CRT_SECURE_NO_WARNINGS
#include <climits>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <bitset>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <set>
#include <list>
#include <random>
#include <deque>
#include <functional>
#include <fstream>
#include <complex>
#include <numeric>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <sstream>

using namespace std;

typedef long double ld;
typedef long long ll;

const int ALL = 720 * 2;

struct interval {
    int left, right, who;
};

bool operator<(interval a, interval b) {
    return a.left < b.left;
}

void solve() {
    int ac, aj;
    cin >> ac >> aj;
    int n = ac + aj;
    vector<interval> a(ac + aj);
    for (int i = 0; i < ac + aj; i++) {
        cin >> a[i].left >> a[i].right;
        if (i >= ac) {
            a[i].who = 1;
        }
    }
    sort(a.begin(), a.end());
    vector<vector<int>> own(2);
    vector<int> s(2);
    int non = 0;
    int result = 0;

    for (int i = 0; i < n; i++) {
        s[a[i].who] += a[i].right - a[i].left;

        int j = (i + 1) % n;
        int len = (a[j].left - a[i].right + ALL) % ALL;
        if (a[i].who == a[j].who) {
            own[a[i].who].push_back(len);
            s[a[i].who] += len;
        }
        else {
            result++;
            non += len;
        }
    }

    for (int t = 0; t < 2; t++) {
        sort(own[t].begin(), own[t].end());
    }
    if (s[0] > s[1]) {
        swap(s[0], s[1]);
        swap(own[0], own[1]);
    }

    //cout << non << " " << s[0] << " " << s[1] << endl;

    if (s[0] + non >= s[1]) {
        cout << result;
        return;
    }
    s[0] += non;
    
    for (int i = int(own[1].size()) - 1; i >= 0; --i) {
        s[0] += own[1][i];
        s[1] -= own[1][i];
        result += 2;
        if (s[0] >= s[1]) {
            break;
        }
    }
    cout << result;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
