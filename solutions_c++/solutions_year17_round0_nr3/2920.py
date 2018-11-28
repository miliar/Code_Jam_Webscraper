// Bathroom Stalls
// Author: aroussau

#include <iostream>
#include <utility>
#include <vector>

using namespace std;

long long T, N, K;
pair<long long, long long> RES;

pair<long long, long long> solve(long long n, long long k) {
    if (n % 2 == 1) {
        if (k == 1) {
            return make_pair(n / 2, n / 2);
        }
        else {
            k--;
            if (k % 2 == 0) {
                return solve(n / 2, k / 2);
            }
            else {
                return solve(n / 2, k / 2 + 1);
            }
        }
    }
    else {
        if (k == 1) {
            return make_pair(n / 2, n / 2 - 1);
        }
        else {
            k--;
            
            if (k % 2 == 1) {
                return solve(n / 2, k / 2 + 1);
            }
            else {
                return solve(n / 2 - 1, k / 2);
            }
        }
    }
}

int main() {
    cin >> T;
    
    for (long long i = 1; i <= T; ++i) {
        cin >> N;
        cin >> K;
        RES = solve(N, K);
        cout << "Case #" << i << ": " << RES.first << " " << RES.second << "\n";
    }
    
    return 0;
}
