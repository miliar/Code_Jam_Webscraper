#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdint>
#include <climits>
#include <queue>
#include <iomanip>

struct Testcase {
    int N;
    int K;
    double U;
    std::vector<double> Pi;
};

std::vector<Testcase> tcs;
std::vector<double> solution;
int n_testcases = 0;

void read_input() {
    std::cin >> n_testcases;
    for(int i=0; i < n_testcases; i++) {
        Testcase tc;
        std::cin >> tc.N >> tc.K >> tc.U;
        tc.Pi.resize(tc.N);
        for(int i=0; i < tc.N; i++) {
            std::cin >> tc.Pi[i];
        }
        tcs.push_back(tc);
    }
    solution.reserve(n_testcases);

}

void write_output() {
    for(int i=0; i < n_testcases; i++) {
        auto& s = solution[i];
        std::cout << "Case #" << i+1 << ": "  << std::setprecision(10) << s << std::endl;
    }
}

int find_min(std::vector<double>& Pi) {
    double min = Pi[0];
    int idx = 0;
    for(int i = 1; i < Pi.size(); i++) {
        if(min > Pi[i]) {
            min = Pi[i];
            idx = i;
        }
    }

    return idx;
}

void solve() {
    double increment = 0.000001;
    double epsilon =   0.0;
    for(auto& tc: tcs) {
        //
        // std::cout << tc.N << " " << tc.K << std::endl;
        // std::cout << tc.U << std::endl;
        // for(auto& pi : tc.Pi) {
        //     std::cout << pi << " ";
        // }
        // std::cout << std::endl;

        while(tc.U > epsilon) {
            int ind_min = find_min(tc.Pi);
            // std::cout << "min ind " << ind_min << " min val " << tc.Pi[ind_min] << std::endl;
            tc.Pi[ind_min] += increment;
            tc.U -= increment;
        }

        double pi = tc.Pi[0];
        for(int i = 1; i < tc.Pi.size(); i++) {
            pi *= tc.Pi[i];
        }

        solution.push_back(pi);
    }
}

int main() {
    read_input();
    solve();
    write_output();
}
