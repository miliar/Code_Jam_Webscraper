//
// Created by jeraz on 4/22/17.
//
#include <iostream>
#include <vector>

using namespace std;

int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {

        int d, n;
        cin >> d >> n;
        vector<double> times;
        for (int j = 0; j < n; ++j) {
            int pos, speed;
            cin >> pos >>speed;
            double time = ((double)d - (double)pos) / (double)speed;
            times.push_back(time);
        }
        double max = 0;
        for (int k = 0; k < n; ++k) {
            if (times[k] > max) {
                max = times[k];
            }
        }
        double out = d / max;
        cout  << fixed << "Case #" << i << ": "<< out << endl;
    }
}