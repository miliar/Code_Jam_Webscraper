#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
        unsigned N, K;
        cin >> N >> K;
        double U;
        cin >> U;
        vector<double> P;

        for (int i = 0; i < N; ++i) {
            double p;
            cin >> p;
            P.push_back(p);
        }

        double total = U;
        for (int i = 0; i < N; ++i)
            total += P[i];

        double each = total / N;
        double result = 1;
        double delta = 0;
        if (each < 1) {
            sort(P.begin(), P.end());
            while (P.back() > each) {
                result *= P.back();
                total -= P.back();
                --N;
                P.pop_back();
                each = total / (N);
            }
            for (int i = 0; i < N; ++i) {
                result *= each;
            }
        }


        cout << "Case #" << caseIndex << ": " << result << "\n";
	}
}
