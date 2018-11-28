#include <iostream>

using namespace std;

uint64_t all_ones(int digs) {
    uint64_t x = 0;
    uint64_t y = 1;
    for (int i = 0; i < digs; i++) {
        x += y;
        y *= 10;
    }
    return x;
}

int count_digs(uint64_t N) {
    uint64_t y = 1;
    int digs = 0;
    while (y <= N) {
        digs++;
        y *= 10;
    }
    return digs;
}

void solve() {
    uint64_t N; cin >> N;

    uint64_t X = 0;
    for (int dig = count_digs(N); dig > 0; dig--) {
        uint64_t dX = all_ones(dig);
        while (X + dX <= N && (X % 10 < 9)) {
            X += dX;
        }
    }

    cout << X << endl;
 
}

int main (void) {

    int T; cin >> T;

    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }   
    
    return 0;
};
