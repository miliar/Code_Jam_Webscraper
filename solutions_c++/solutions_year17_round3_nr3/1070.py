#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <functional>
#include <unordered_set>
#include <unordered_map>

using namespace std;

struct Solve {

    Solve(vector<double>& cores, int K, double U) {
        // maximize probability of success
        sort(cores.begin(), cores.end());

        for (auto d : cores) {
            cout << d << ", ";
        }cout << endl;
        cout << U << endl;

        for (int i = 0; i < cores.size(); ++i) {
            double core = cores[i];

            for (int j = i; j < cores.size(); ++j) {
                double corej = cores[j];
                bool a = (corej > core) && (U > 0);
                bool b = (j == cores.size() - 1) && (U > 0);

                double add = 0;
                if (a) {
                    add = min(U/(j), corej - core);
                } else if (b) {
                    add = min(U / cores.size(), 1 - corej);
                    j += 1;
                }

                if (a || b) {
                    for (int k = j - 1; k >= 0; --k) {
                        cores[k] += add;
                        U -= add;
                    }
                    break;
                }
            }
        }

        for (auto d : cores) {
            cout << d << ", ";
        }cout << endl;
        cout << U << endl;

        answer = to_string(success(cores, K));
    }

    string answer = "-1";

    double failure(const vector<double>& cores, int K) {
        // probability of cores.size() - K + 1 failures
        return 1 - success(cores, K);
    }

    double success(const vector<double>& cores, int K) {
        // probability of cores remaining above K.
        // e.g. 0.5 0.5 0.5 0.5 > 2?
        double p =  1;
        for (auto r : cores) {
            p *= r;
        }
        return p;
    }

private:

};

int main() {

    ofstream ofs;
    ifstream ifs;

    ifs.open("in.txt");
    ofs.open("out.txt", ofstream::out | ofstream::app);

    size_t T; // size of input

    ifs >> T;

    int _case = 1;

    /**
     * PROBLEM VARS GO HERE.
     */
    int N, K;
    double U, P;

    while (T-- > 0) {

        ifs >> N >> K >> U;

        vector<double> cores;

        while (N-- > 0) {
            ifs >> P;
            cores.push_back(P);
        }

        Solve solution(cores, K, U);

        ofs << "Case #" << _case++ << ": " << solution.answer << endl;
    }

    return 0;
}