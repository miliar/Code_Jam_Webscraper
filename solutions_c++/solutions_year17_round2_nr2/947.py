/* Task solution for GCJ 2017
 * Tested with GCC 5.4.0
 * Build command line:
 *  g++ -std=gnu++14 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        cout << "Case #" << T << ": ";
        r -= g;
        y -= v;
        b -= o;
        if (r == 0 && y == 0 && b == 0) {
            if (g > 0 && v == 0 && o == 0) {
                for (int i = 0; i < g; ++i) {
                    cout << "RG";
                }
                cout << endl;
                continue;
            }
            if (v > 0 && g == 0 && o == 0) {
                for (int i = 0; i < v; ++i) {
                    cout << "YV";
                }
                cout << endl;
                continue;
            }
            if (o > 0 && g == 0 && v == 0) {
                for (int i = 0; i < o; ++i) {
                    cout << "BO";
                }
                cout << endl;
                continue;
            }
        }
        string R(2 * g + 1, 'R'), Y(2 * v + 1, 'Y'), B(2 * o + 1, 'B');
        for (int i = 0; i < g; ++i) {
            R[2 * i + 1] = 'G';
        }
        for (int i = 0; i < v; ++i) {
            Y[2 * i + 1] = 'V';
        }
        for (int i = 0; i < o; ++i) {
            B[2 * i + 1] = 'O';
        }
        if (r < y) {
            swap(r, y);
            swap(g, v);
            swap(R, Y);
        }
        if (y < b) {
            swap(y, b);
            swap(v, o);
            swap(Y, B);
        }
        if (r < y) {
            swap(r, y);
            swap(g, v);
            swap(R, Y);
        }
        if (y <= 0 || b < 0 || (b == 0 && o > 0) || r > y + b) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        while (y > b) {
            cout << R << Y;
            R.resize(1);
            Y.resize(1);
            --r;
            --y;
        }
        while (r > y) {
            cout << R << Y << R[0] << B;
            R.resize(1);
            Y.resize(1);
            B.resize(1);
            r -= 2;
            --y;
            --b;
        }
        while (r > 0) {
            cout << R << Y << B;
            R.resize(1);
            Y.resize(1);
            B.resize(1);
            --r;
            --y;
            --b;
        }
        cout << endl;
    }
    return 0;
}
