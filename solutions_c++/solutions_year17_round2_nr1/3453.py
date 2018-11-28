//
// Created by XelaPi.
//
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {

    int num;

    cin >> num;

    for (int i = 0; i < num; i++) {
        cout << "Case #" << (i + 1) << ": ";

        double d, n;

        vector<pair<long double, long double>> horses;

        cin >> d >> n;

        for (int j = 0; j < n; ++j) {
            long double distance, speed;

            cin >> distance >> speed;

            horses.push_back(make_pair(distance, speed));
        }

        long double maxTime = 0;

        long double maxD, maxS;

        for (pair<long double, long double> horse : horses) {
            long double testTime = (d - horse.first) / horse.second;

            if (testTime > maxTime) {
                maxTime = testTime;
                maxD = d - horse.first;
                maxS = horse.second;
            }
        }

        long double speed = d * maxS / maxD;

        string output = to_string(speed);

        output.erase(std::remove(output.begin(), output.end(), '+'), output.end());

        cout << output << endl;
    }

    return 0;
}