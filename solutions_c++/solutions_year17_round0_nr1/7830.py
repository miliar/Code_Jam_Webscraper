#include <bits/stdc++.h>

using namespace std;

int main(){
    ifstream input("a.in");
    ofstream output;
    output.open ("a.out");
    unsigned long long T;

    input >> T;
    for(unsigned int i = 0; i < T; i++) {
        string N;
        int K;
        input >> N >> K;
        int j = 0, op = 0;
        for(; j < N.size() - K + 1; j++) {
            if(N[j] == '-') {
                op++;
                for(int k = 0; k < K; k++) {
                    N[k + j] = N[k + j] == '-' ? '+' : '-';
                }
            }
        }
        for(; j < N.size(); j++) {
            if(N[j] == '-') {
                op = -1;
                break;
            }
        }
        if(op == -1) {
            output << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << endl;
        } else {
            output << "Case #" << (i + 1) << ": " << op << endl;
        }
    }
    output.close();
    return 0;
}
