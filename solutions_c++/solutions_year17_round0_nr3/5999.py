#include <iostream>
#include <map>
#include <cstring>
#include <climits>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>

using namespace std;

int T;
long N, K;

long long solve() {
    long ans = 0;
    int count = log(K) / log(2);
    long long done_p = pow(2, count) - 1;
    long long left_p = K - done_p;
    N = N - done_p;
    long long left = N % (done_p + 1);
    if (left >= left_p) {
        return N / (done_p + 1) + 1;
    } else {
        return N / (done_p + 1);
    }
}

int main() {
    ifstream cin("C-small-2-attempt0.in");
    ofstream cout("output.txt");
    // ifstream cin("in.txt");
    cin >> T;
    for (int i=1; i<=T; i++) {
        cin >> N;
        cin >> K;
        long long ans = solve();
        if (ans % 2 == 0) {
            cout << "Case #" << i << ": " << (ans+1) / 2 << " " << (ans-1) / 2 << endl;
        } else {
            cout << "Case #" << i << ": " << ans / 2 << " " << ans / 2 << endl;
        }
    }
    return 0;
}