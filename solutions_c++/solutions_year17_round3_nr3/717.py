#include <cstdio>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAX_N 100

int n, k;
double a[MAX_N];

bool all_numbers_are_the_same() {
    for (int i = 1; i < n; i++)
        if (a[i] != a[i - 1])
            return false;
    return true;
}

int number_of_smallest() {
    int res = 1;
    for (int i = 1; i < n; i++) {
        if (a[i] != a[i - 1])
            return res;
        ++res;
    }
}

#define EPS 0.0000000001
double isequal(double a, double b) {
    return abs(a - b) < EPS;
}

int main() {

    int nTest;
    cin >> nTest;

    for (int test = 1; test <= nTest; test++) {
        cin >> n >> k;

        double u;
        cin >> u;

        for (int i = 0; i < n; i++)
            cin >> a[i];

        while (1) {
            if (isequal(u, 0))
                break;

            sort(a, a + n);

            if (all_numbers_are_the_same())
                break;

            int ns = number_of_smallest();
            double sm = a[ns];

            double needed_unit = (sm - a[0]) * ns;
            double real_unit = min(u, needed_unit);

            for (int i = 0; i < ns; i++)
                a[i] += real_unit / ns;

            u -= real_unit;
        }

        if (!isequal(u, 0)) {
            for (int i = 0; i < n; i++)
                a[i] += u / n;
        }

        double res = 1.0;
        for (int i = 0; i < n; i++) res *= a[i];

        cout << "Case #" << test << ": " << setprecision(10) << res << endl;
    }

    return 0;
}
