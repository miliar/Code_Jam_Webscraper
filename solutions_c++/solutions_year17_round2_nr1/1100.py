#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int d, n;
    cin >> d >> n;
    int k, s;
    long double maxT = -1;
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &k, &s);
        maxT = max(maxT, ((long double)d - k) / s);
    }
    long double v = d / maxT;
    cout.precision(10);
    cout << fixed << v << endl;
}

int main() {
    int cntTests;
    cin >> cntTests;
    for (int curTest = 0; curTest < cntTests; curTest++) {
        cout << "Case #" << curTest + 1 << ": ";
        solve();
    }
}