#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
    int T;
    long long N, K;
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> N >> K;
        long long storage = 1;
        long long people = K;
        long long rs = 0;
        long long rl = 1;
        long long size_large = N;
        while(people > storage) {
            people -= storage;
            if(size_large % 2 == 0) {
                rs += storage;
            } else {
                rl += storage;
            }
            size_large /= 2;
            storage = storage << 1;
        }

        if(people > rl) {
            size_large--;
        }

        long long Dr = size_large / 2;
        long long Dl = size_large / 2 - (size_large % 2 == 0);

        cout << "Case #" << (t+1) << ": ";
        cout << Dr << " " << Dl;
        cout << endl;
    }
}
