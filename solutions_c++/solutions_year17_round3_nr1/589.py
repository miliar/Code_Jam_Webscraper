#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

#define _USE_MATH_DEFINES

#include <cmath>

using namespace std;


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

struct myclass2 {
    bool operator() (int i, int j) {
        return (long)Ri[i] * (long)Hi[i] < (long)Ri[j] * (long)Hi[j];
    }

    unsigned* Ri;
    unsigned* Hi;

} myTempObject2;

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
        unsigned N, K;
        cin >> N >> K;

        unsigned* Ri = new unsigned[N];
        unsigned* Hi = new unsigned[N];

        for (unsigned i = 0; i < N; ++i)
            cin >> Ri[i] >> Hi[i];

        
        vector<unsigned> radius_sort;
        for (unsigned i = 0; i < N; ++i)
            radius_sort.push_back(i);
        myTempObject.Ri = Ri;
        myTempObject.Hi = Hi;

        myTempObject2.Ri = Ri;
        myTempObject2.Hi = Hi;

        sort(radius_sort.begin(), radius_sort.end(), myTempObject);

        double result = 0;

        while (radius_sort.size() >= K) {
            unsigned lastIndex = radius_sort.back();
            double tempResult = 1.0f * 2 * M_PI * Ri[lastIndex] * Hi[lastIndex] + M_PI * Ri[lastIndex] * Ri[lastIndex];
            radius_sort.pop_back();

            if (!radius_sort.empty()) {
                vector<unsigned> surface = radius_sort;
                sort(surface.begin(), surface.end(), myTempObject2);

                unsigned count = 1;
                while (count != K) {
                    tempResult += 1.0f * 2 * M_PI * Ri[surface.back()] * Hi[surface.back()];
                    surface.pop_back();
                    ++count;
                }

            }
            if (tempResult > result)
                result = tempResult;
            
            while (!radius_sort.empty() && Ri[lastIndex] == Ri[radius_sort.back()])
                radius_sort.pop_back();

        }

        cout << "Case #" << caseIndex << ": " << std::fixed << std::setprecision(9) << result << "\n";

        delete[] Ri;
        delete[] Hi;
	}
}
