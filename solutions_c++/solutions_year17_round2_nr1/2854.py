#include <iostream>
#include <iomanip>

using namespace std;

void printResult(int nr, long double result) {
    cout << "Case #" << nr << ": ";
    cout << std::fixed << std::setprecision(6) << result << "\n";
}

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    int d, n, k, s;

    for (int i = 1; i <= t; i++) {
        cin >> d >> n;

        long double result = 999999999999999999LL;
        long double tmp;

        for (int j = 0; j < n; j++) {
            cin >> k >> s;

            tmp = (d-k);
            tmp = tmp/((long double) s);
            tmp = d/tmp;

            if (tmp < result) {
                result = tmp;
            }
        }

        printResult(i, result);
    }

    return 0;
}