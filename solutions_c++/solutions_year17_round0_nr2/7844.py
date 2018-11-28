#include <bits/stdc++.h>

using namespace std;

int main(){
    ifstream input("b.in");
    ofstream output;
    output.open ("b.out");
    unsigned long long T;

    input >> T;
    for(unsigned int i = 0; i < T; i++) {
        string N;
        input >> N;
        int ch = 0;
        for(int j = 1; j < N.size(); j++) {
            if(N[j] < N[j - 1]) {
                N[ch] = N[ch] - 1;
                if(N[ch] < '1' && ch != 0) N[ch] = '9';
                for(int k = ch + 1; k < N.size(); k++) {
                    N[k] = '9';
                }
                break;
            } else if(N[j] != N[j - 1]) {
                ch = j;
            }
        }
        if(N[0] == '0') N = N.substr(1, N.size() - 1);
        output << "Case #" << (i + 1) << ": " << N << endl;
    }
    output.close();
    return 0;
}
