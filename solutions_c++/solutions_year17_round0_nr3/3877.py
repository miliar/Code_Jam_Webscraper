#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iterator>
#include <utility>
#include <algorithm>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define sz(v) ((long long)v.size())
#define mp make_pair
#define FOR(i,n) for(long long i = 0;i < (n);++i)
#define MOD 1000000007

void solve() {
    int n, k;
    cin >> n >> k;
    priority_queue<int> s;
    s.push(n);
    FOR(i, k) {
        int max_segment = s.top();
        s.pop();
        int left = (max_segment - 1) / 2;
        int right = max_segment - 1 - left;
        s.push(left);
        s.push(right);
        if (i == k - 1) {
            cout << max(left, right) << " " << min(left, right) << endl;
        }
    }
}

int main() {
    int T;
    cin >> T;
    FOR(iter, T) {
        cout << "Case #" << iter + 1 << ": ";
        solve();
    }
}