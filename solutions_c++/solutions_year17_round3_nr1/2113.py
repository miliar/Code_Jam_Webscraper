#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

const long N_MAX = 1000;
double R[N_MAX];
double H[N_MAX];

struct pancake {
    double R, H;
};

bool cmp_pancakes(pancake &l, pancake &r) {
    return l.R > r.R;
}

vector<pancake> pancakes;
double best_result_no_pi;

double get_exposed_area_no_pi(double R, double H, double Rover) {
    return R * R + 2 * R * H - Rover * Rover;
}

void helper(int N, int K, int i, int count, double current_result) {
    if(i >= N) {
        return;
    }
    
    for(int j = i + 1; j < N - (K - count) + 1; ++j) {
        double Rover = 0;
        if(count < K && j < N) {
            Rover = pancakes[j].R;
        }

        double exposed_area = get_exposed_area_no_pi(pancakes[i].R, pancakes[i].H, Rover);
        double new_result = current_result + exposed_area;

        if(new_result > best_result_no_pi) {
            best_result_no_pi = new_result;
        }

        if(count == K) {
            break;
        }
    
        helper(N, K, j, count + 1, new_result);
    }
}

double solve(int N, int K) {
    sort(pancakes.begin(), pancakes.begin() + N, cmp_pancakes);
    
    best_result_no_pi = 0;
    
    for(int i = 0; i < N - K + 1; ++i) {
        helper(N, K, i, 1, 0);
    }
    
    return best_result_no_pi * M_PI;
}

int main(int argc, char** argv) {
    int T;
    cin >> T;
    
    for(int t = 1; t <= T; ++t) {
        long K, N;
        cin >> N >> K;
        
        pancakes.clear();
        for(int i = 0; i < N; ++i) {
            pancake p;
            cin >> p.R >> p.H;
            pancakes.push_back(p);
        }
        
        cout << "Case #" << t << ": " << fixed << setprecision(9) << solve(N, K) << "\n";
    }
    
    return 0;
}

