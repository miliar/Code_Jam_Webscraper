#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>
#include <string>
#include <climits>
#include <queue>
#include <iomanip>
using namespace std;

int main() {
    int T, D, N;
    double maxTime = 0.0;
    cin >> T;
    for ( int i = 0; i < T; i++) {
        cin >> D;
        cin >> N;
        int K, S;
        for ( int j = 0; j < N; j++) {
          cin >> K;
          cin >> S;
          double curr  = (static_cast<double>(D) - static_cast<double>(K)) / static_cast<double>(S);
          if (curr > maxTime) maxTime = curr;
        }
        cout << "Case #" << i+1 <<": " << fixed << setprecision(6) << (static_cast<double>(D) / maxTime)   << endl;
        maxTime = 0.0;
    }
    return 0;
}
