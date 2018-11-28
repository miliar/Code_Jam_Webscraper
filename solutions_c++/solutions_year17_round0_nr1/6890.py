#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream inf("A.in");
ofstream outf("A.out");

char flip(char c) {
    if (c == '-')
        return '+';
    else
        return '-';
}

int main() {

    int caseCnt; inf >> caseCnt;

    string S;
    int K;
    int flipCnt;
    int imposFlag;
    // Iterate over each case
    for (int i=0; i < caseCnt; i++) {

        inf >> S;
        inf >> K;

        // Iterate through string
        flipCnt = 0;
        imposFlag = 0;
        for (int j = S.length()-1; j >= 0; j--) {
            if (S[j] == '-') {
                // Flips
                flipCnt++;
                for (int k=0; k < K; k++) {
                    if (j-k >= 0)
                        S[j-k] = flip(S[j-k]);
                    else
                        imposFlag++;
                }
            }
        }
        if (imposFlag != 0)
            outf << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        else
            outf << "Case #" << i+1 << ": " << flipCnt << endl;
    }

    inf.close();
    outf.close();
    return 0;
}
