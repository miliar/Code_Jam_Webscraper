#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
    ifstream    f("in.txt");
    ofstream    g("out.txt");
    int         T; f >> T;
    
    for (int test = 1; test <= T; test++) {
        int                     N, K; f >> N >> K;
        vector<pair<int64_t, int64_t>>  P(N);
        
        for (int i = 0; i < N; i++) f >> P[i].first >> P[i].second;
        sort(P.begin(), P.end(), [&](const pair<int64_t, int64_t> &a, const pair<int64_t, int64_t> &b) {
            return a.first*a.second > b.first*b.second;
        });
        
        long double ans = 0;
        for (int base = 0; base < N; base++) {
            vector<int64_t> A;
            for (int i = 0; i < N; i++) if (i != base) {
                if (P[i].first <= P[base].first) A.push_back(P[i].first*P[i].second);
            }
            
            if (A.size() < K-1) continue;
            
            long double area = M_PI*P[base].first*P[base].first + 2*M_PI*P[base].first*P[base].second;
            for (int i = 0; i < K-1; i++) area += 2*M_PI*A[i];
            
            ans = max(ans, area);
        }
        
        g << setprecision(7) << fixed << "Case #" << test << ": " << ans << endl;
    }
    
    return 0;
}
