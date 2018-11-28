#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

long power(int base, int exp) {
    return pow(base, exp);
}

int main(int argc, const char * argv[]) {
    freopen("/Users/danielsong/Downloads/C-small-2-attempt0.in.txt", "r", stdin);
    freopen("/Users/danielsong/Downloads/C-small-2-attempt0.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long N, people;
        cin >> N >> people;
        long highestPower = power(2, log2(people));
        N -= highestPower - 1;
        long emptyStalls = N / highestPower;
        N -= emptyStalls * highestPower;
        if (N > people - highestPower) {
            emptyStalls += 1;
        }
        cout << "Case #" << t << ": " << emptyStalls / 2 << " ";
        if (emptyStalls % 2 == 0) {
            cout << emptyStalls / 2 - 1;
        } else {
            cout << emptyStalls / 2;
        }
        cout << endl;
    }
    
    return 0;
}
