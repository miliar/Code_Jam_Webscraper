#include <algorithm>
#include <iterator>
#include <iostream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>

using namespace std;

double solve()
{
    int d, n;
    cin >> d >> n;
    double mtime = 0;
    int start = 0, speed = 0;
    for(int i = 0; i < n; i++) {
        cin >> start >> speed;
        mtime = max(mtime, 1.0 * (d - start) / speed);
    }

    return d / mtime;
}

int main()
{
    int tests;
    cin >> tests;

    cout << fixed << setprecision(9);
    for(int t = 1; t <= tests; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }

    return 0;
}
