#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

#define MAX_N 1111

struct horse {
    int initial;
    int speed;
};

horse horses[MAX_N];
double res[MAX_N];

bool cmp(const horse& h1, const horse& h2) {
    if (h1.initial != h2.initial) {
        return h1.initial < h2.initial;
    }

    return h1.speed < h2.speed;
}

int main() {

    int nTest;
    cin >> nTest;

    for (int test = 0; test < nTest; ++test) {
        int d, n;
        cin >> d >> n;


        for (int i = 0; i < n; ++i) {
            cin >> horses[i].initial >> horses[i].speed;
        }

        sort(horses, horses + n, cmp);

        res[n - 1] = 1.0 * (d - horses[n - 1].initial) / horses[n - 1].speed;

        for (int i = n - 2; i >= 0; --i) {
            double max_speed = 1.0 * (d - horses[i].initial) / res[i + 1];

            if (max_speed > horses[i].speed)
                max_speed = horses[i].speed;

            res[i] = 1.0 * (d - horses[i].initial) / max_speed;
        }

        cout << "Case #" << test + 1 << ": " << setprecision(10)  << d / res[0] << endl;
    }

    return 0;
}
