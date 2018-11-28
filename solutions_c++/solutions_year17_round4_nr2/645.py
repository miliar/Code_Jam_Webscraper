#include <iostream>
#include <string.h>
#include <queue>
#include <tuple>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <map>
#include <unordered_set>
#include <numeric>
#include <assert.h>

using namespace std;

const int N = (int) 2e5;

void solve(int test) {
    cout << "Case #" << test << ": ";
    int n, c, m;
    cin >> n >> c >> m;
    vector <int> seat(n), cust(c);
    for (int i = 0; i < m; i++) {
        int p, b;
        cin >> p >> b;
        p--, b--;
        seat[p]++;
        cust[b]++;
    }
    int MIN = *max_element(cust.begin(), cust.end());
    int l = MIN - 1;
    int r = m;
    while (l + 1 < r) {
        int mid = (l + r) / 2;
        int free = 0;
        bool bad = false;
        for (int i = 0; i < n; i++) {
            if (seat[i] <= mid) {
                free += mid - seat[i];
            } else {
                if (free < seat[i] - mid) {
                    bad = true;
                    break;
                }
                free -= (seat[i] - mid);
            }
        }
        if (bad) {
            l = mid;
        } else {
            r = mid;
        }
    }
    int rides = r;
    int promote = 0;
    for (int i = 0; i < n; i++) {
        if (seat[i] > rides) {
            promote += (seat[i] - rides);
        }
    }
    cout << rides << " " << promote << "\n";
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}