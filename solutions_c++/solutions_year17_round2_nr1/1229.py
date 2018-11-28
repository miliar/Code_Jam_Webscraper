#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
        double answer = 100.00f;

        long int D;
        unsigned int N;

        cin >> D >> N;

        long int* dis = new long int[N];
        unsigned int* speed = new unsigned int[N];

        for (unsigned i = 0; i < N; ++i) {
            cin >> dis[i] >> speed[i];
        }

        double one = 1.0f;
        double maxTime = 0.0f;

        for (unsigned i = 0; i < N; ++i) {
            double time = one * (D - dis[i]) / speed[i];
            
            if (i == 0 || time > maxTime)
                maxTime = time;
        }
        
        answer = one * D / maxTime;

        cout << "Case #" << caseIndex << ": " << std::fixed << std::setprecision(6) << answer << "\n";

        delete[] dis;
        delete[] speed;
	}
}
