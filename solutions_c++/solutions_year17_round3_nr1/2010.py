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

    using cake_t = pair<double, double>;

    Solve(vector<pair<double, double>>& cakes, int K) {

        sort(cakes.begin(), cakes.end(), [&](const cake_t& lhs, const cake_t& rhs) -> bool {
            return lhs.first > rhs.first;
        });

        answer = to_string(
            recurse(cakes, 0, K, 0)
        );
    }

    double recurse(vector<pair<double, double>>& cakes, int i, int K, double sum) {

        if ((i >= cakes.size()) || (K < 1)) return sum;

        double margin = sa(cakes[i], true);
        if (sum == 0) {
            margin += a(cakes[i]);
        }

        cout << sum << " " << margin << endl;

        return max(
            recurse(cakes, i + 1, K - 1, sum + margin),
            recurse(cakes, i + 1, K, sum)
        );

    }

    double sa(const cake_t& cake) {
        return c(cake) * cake.second + a(cake);
    }

    double sa(const cake_t& cake, bool) {
        return sa(cake) - a(cake);
    }

    double c(const cake_t& cake) {
        return M_PI * cake.first * 2;
    }

    double a(const cake_t& cake) {
        return M_PI * pow(cake.first,2);
    }

    string answer = "";

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
     double R, H;

    while (T-- > 0) {

        ifs >> N >> K;
        vector<pair<double, double>> cakes;

        int c = N;

        while (c-- > 0) {
            ifs >> R >> H;
            cakes.emplace_back(R, H);
        }

        Solve solution(cakes, K);

        ofs << "Case #" << _case++ << ": " << solution.answer << endl;
    }

    return 0;
}