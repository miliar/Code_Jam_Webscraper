#include <iostream>
#include <c++/vector>
#include <c++/fstream>
#include <c++/cmath>
#include <c++/algorithm>
#include <functional>
#include <c++/cfloat>

using namespace std;

struct Solve {
    Solve(vector<pair<double, double>>& horses, double D) {

        // vector of K position of horse and S speed of the horse
        // find maximum speed that passes no horse

        // we are at 0 and can go any speed, including FTL.

        // For each horse calculate the speed at which we would arrive at the same time as it
        // then take the minimum of those speeds.

        double min_ttd = 0;

        for (auto& r : horses) {

            double position = r.first;
            double speed = r.second;

            // time to dest
            double ttd = (D - position) / speed;
            if (min_ttd < ttd) {
                min_ttd = ttd;
            }
        }

        answer = to_string(D / min_ttd);

    }

    string answer = "\n";
};

int main() {

    ofstream ofs;
    ifstream ifs;

    ifs.open("in.txt");
    ofs.open("out.txt", ofstream::out | ofstream::app);


    size_t T; // size of input

    ifs >> T;

    int _case = 1;

    double D, N;
    double K, S;

    while (T-- > 0) {
        ifs >> D;
        ifs >> N;

        vector<pair<double, double>> data;

        cout << D << ", " << N << endl;

        while (N-- > 0) {
            ifs >> K;
            ifs >> S;
            data.emplace_back(make_pair(K, S));
        }

        Solve solution(data, D);

        ofs << "Case #" << _case++ << ": " << solution.answer << endl;
    }

    return 0;
}