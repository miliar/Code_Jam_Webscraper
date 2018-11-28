#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

struct Horse {
    int init;
    int maxSpeed;
};

double bruteForce(int D, vector<Horse>& horses) {
    std::sort(horses.begin(), horses.end(),
              [](const Horse& a, const Horse& b) { return a.init > b.init; });
    // 1 item
    if (horses.size() == 1) {
        double time = (double)(D - horses[0].init) / (double)horses[0].maxSpeed;
        return D / time;
    }
    // 2 items
    else if (horses.size() == 2) {
        vector<double> times;
        for (const auto& horse : horses) {
            times.push_back((double)(D - horse.init) / (double)horse.maxSpeed);
        }
        // if 2nd horse is the bottleneck easy problem
        if (times[1] > times[0]) {
            return D / times[1];
        }
        // else the two meet somewhere in the middle and will take times[0] time to finish
        else {
            return D / times[0];
        }
    }
    return 0;
}
double hackyWay(int D, const vector<Horse>& horses) {
    // calculate maximum time for all
    double maxTime = 0;
    for (size_t i = 0; i < horses.size(); ++i) {
        // { cout << "initial " << initPos[i] << " max speed " << maxSpeed[i] << endl; }
        double time = (double)(D - horses[i].init) / (double)horses[i].maxSpeed;
        if (time > maxTime) {
            maxTime = time;
        }
    }
    // { cout << "max time " << maxTime << endl; }
    return D / maxTime;
}
int main() {
    int T;
    cin >> T;

    for (int c = 1; c <= T; ++c) {
        int D, N;
        cin >> D >> N;

        vector<Horse> horses;
        for (int n = 1; n <= N; ++n) {
            int init, speed;
            cin >> init >> speed;
            horses.push_back({init, speed});
        }

        // { cout << "\nD " << D << endl; }
        cout << "Case #" << c << ": " << std::fixed << std::setprecision(7) << hackyWay(D, horses)
             << endl;
    }
}