#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

#define _USE_MATH_DEFINES

#include <cmath>

using namespace std;

/*
struct myclass {
    bool operator() (int i, int j) {
        if (Ri[i] < Ri[j])
            return true;
        else if (Ri[i] > Ri[j])
            return false;
        else {
            return Hi[i] < Hi[j];
        }
    }

    unsigned* Ri;
    unsigned* Hi;

} myTempObject;
*/

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
        int N, P;
        cin >> N >> P;
        int* counts = new int[P];
        for (int i = 0; i < P; ++i)
            counts[i] = 0;

        int temp;
        for (int i = 0; i < N; ++i) {
            cin >> temp;
            ++(counts[temp % P]);
        }

        int ans = 0;

        if (P == 2) {
            ans += counts[0];
            ans += counts[1] / 2;
            if (counts[1] % 2 != 0)
                ++ans;
        } else if (P == 3) {
            ans += counts[0];
            int min = counts[1];
            if (counts[2] < min)
                min = counts[2];
            ans += min;

            counts[1] -= min;
            counts[2] -= min;

            if (counts[1] != 0) {
                ans += counts[1] / 3;
                if (counts[1] % 3 != 0)
                    ++ans;
            }

            if (counts[2] != 0) {
                ans += counts[2] / 3;
                if (counts[2] % 3 != 0)
                    ++ans;
            }

        }

        cout << "Case #" << caseIndex << ": " << ans << "\n";
        delete[] counts;

	}
}

