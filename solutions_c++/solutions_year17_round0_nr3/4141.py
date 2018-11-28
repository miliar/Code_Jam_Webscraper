#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

#define X first
#define Y second

using namespace std;


typedef long long ll;




void printcase(int k, ll a, ll b) {
    cout << "Case #" << k << ": ";
    cout << a << ' ' << b << endl;
}

vector<pair<int, int> > dt;

void go(int n) {
    dt.push_back({(n) / 2, (n - 1) / 2});
    if (n / 2)
        go(n / 2);
    if ((n - 1) / 2)
        go((n - 1) / 2);
}
int main() {
//#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
//#endif
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        ll k, n;
        cin >> n >> k;
        dt.clear();
        go(n);
        sort(dt.rbegin(), dt.rend());
        if (k >= dt.size())
            printcase(tt + 1, 0, 0);
        else
            printcase(tt + 1, dt[k - 1].X, dt[k - 1].Y);
    }


    return 0;
}