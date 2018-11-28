#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main () {
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int t1 = 1; t1 <= t; ++t1) {
        cout << "Case #" << t1 << ": ";
        int n, k;
        cin >> n >> k;
        long double x;
        cin >> x;
        vector <long double> p (n);
        for (int i = 0; i < n; ++i)
            cin >> p[i];
        sort (p.begin(), p.end());
        for (int i = 1; i < n; ++i) {
            long double goal = p[i];
            long double have = p[i-1];
            long double add = min (goal - have, x / i);
   //         cout << endl;
    //        cout << "Goal " << goal << " Have " << have << " Add " << add << endl;
            for (int j = 0; j < i; ++j)
                p[j] += add;
            x -= add * i;
        }
        if (x > 0) {
            long double add = x / n;
            for (int i = 0; i < n; ++i)
                p[i] += add;
        }
        long double ans = 1.;
        for (int i = 0; i < n; ++i)
            ans *= p[i];
        cout << fixed << setprecision(10) << ans << endl;
    }
}
