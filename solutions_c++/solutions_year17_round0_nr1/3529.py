#include <iostream>

using namespace std;
int T;
int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string seq;
        int K;
        cin >> seq;
        cin >> K;
        int flips = 0;
//        cerr << "Seq " << seq << "\n";
        for(int i = 0; i < int(seq.size())-K+1; i++) {
//            cerr << "Do " << i << "\n";
            if(seq[i] == '-') {
                // Flip
                for(int j = 0; j < K; j++) {
                    seq[i+j] = seq[i+j] == '+' ? '-' : '+';
                }
                flips++;
            }
        }
//        cerr << "Flips done\n";
        bool impossible = false;
        for(auto x: seq) {
            if(x == '-') {
                // Impossible
                impossible = true;
            }
        }
        cout << "Case #" << t << ": "; 
        if(impossible) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << flips << "\n";
        }
    }
}
