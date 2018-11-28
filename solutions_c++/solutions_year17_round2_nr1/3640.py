#include <iostream>

using namespace std;

int main() {
    int numberOfTestCases;
    cin >> numberOfTestCases;
    for (int testCase = 1; testCase <= numberOfTestCases; ++testCase) {
        int D, n;
        cin >> D >> n;
        double maxTime = 0;
        for (int i = 1; i <= n; ++i) {
            int k, s;
            cin >> k >> s;
            double time = (D - k) / double(s);
            maxTime = max(maxTime, time);
        }
        double maxSpeed = D / maxTime;
        printf("Case #%d: %f\n",testCase,maxSpeed);
    }
    return 0;
}