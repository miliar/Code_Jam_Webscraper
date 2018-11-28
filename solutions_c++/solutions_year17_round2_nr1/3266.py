#include <bits/stdc++.h>
using namespace std;
using ll = long long;

typedef std::numeric_limits< double > dbl;
int T, D, N;

double solve(vector<pair<int, int>>& ps) {
    double slowest_time = 0.0; 
    for (int i=0; i<ps.size(); i++) {
        double curr_time = (1.0*D - ps[i].first) / ps[i].second;
        if (curr_time > slowest_time) slowest_time = curr_time;
    }
    return (double) D / slowest_time; 
}

int main(int argc, char* argv[]) {
    ifstream infile(argv[1]);
    //ofstream outfile(argv[2]);
    vector<pair<int, int>> ps;
    infile >> T;
    cout.precision(dbl::max_digits10);
    for (int i=1; i<=T; i++) {
        infile >> D >> N;
        ps.clear();
        for (int j=1; j<=N; j++) {
            int k, s;
            infile >> k >> s;
            ps.push_back({k, s});
        }
        printf("Case #%d: %f\n", i, solve(ps));
    }
}
