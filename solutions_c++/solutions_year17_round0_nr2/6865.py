#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ofstream outf("B.out");
ifstream inf("B.in");

void ninify(string &N, int j) {
    for (int i=j; i < N.length(); i++) {
        if (N[i] != '9')
            N[i] = '9';
        else
            break;
    }
    return;
}

int main() {

    int caseCnt; inf >> caseCnt;

    // Iterate through each case
    string N;
    for (int i=0; i < caseCnt; i++) {
        inf >> N;

        // Iterate through string
        for (int j = N.length()-1; j > 0; j--) {
            if (N[j] < N[j-1]) {
                N[j-1]--;
                ninify(N, j);
            }
        }
        // Remove leading zeros if exist
        while(N.length() > 0 && N[0] == '0') {
            N = N.substr(1, string::npos);
        }

        outf << "Case #" << i+1 << ": " << N << endl;
    }

    inf.close();
    outf.close();
    return 0;
}
