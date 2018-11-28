#include <algorithm>
#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

using sol_type = double;

long long D, N;
vector<long long> K, S;

void read_data();
sol_type find_solution();

int main() {

    int cases;
    int case_num =0;

    cin >> cases;

    while (cases--) {
        ++case_num;
        read_data();
        auto solution = find_solution();
        cout << "Case #" << case_num << ": ";
        cout << fixed << setprecision(9)  <<  solution << endl;
    }
    return 0;
}

void read_data(){
    cin >> D;
    cin >> N;
    K.resize(N);
    S.resize(N);
    for(auto i = 0; i < N; ++i)
        cin >> K[i] >> S[i];
}

sol_type find_solution(){
    double t = 0;
    for (auto i = 0u; i < K.size(); ++i)
        t = max(t, static_cast<double>(D - K[i]) / S[i]);
    return D / t;
}
