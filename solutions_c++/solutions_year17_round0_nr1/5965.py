#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main(int argc, char* argv[]) {
    ifstream in ("A-large.in");
    ofstream out ("test.out");
    
    int T;
    char input;
    char S[2000];
    int num;
    int K;
    int fail;
    int flip;
    in >> T;
    for (int i = 0; i < T; i++) {
        flip = 0;
        fail = 0;
        num = 0;
        in >> skipws >> input;
        int j = 0;
        while (input == '+' || input == '-') {
            num++;
            S[j] = input;
            in >> noskipws >> input;
            j++;
        }
        
        in >> K;
        
        j = 0;
        for (j = 0; j < num - K + 1; j++) {
            if (S[j] == '-') {
                flip++;
                for (int k = 0; k < K; k++) {
                    if (S[j+k] == '-') {
                        S[j+k] = '+';
                    } else {
                        S[j+k] = '-';
                    }
                }
            }
        }
        
        for (j ; j < num; j++) {
            if (S[j] == '-') {
                fail = 1;
            }
        }
        
        if (fail == 1) {
            out << "Case #" << i + 1 << ": IMPOSSIBLE\n";
        } else {
            out << "Case #" << i + 1 << ": " << flip << "\n";
        }
    }
    return 0;
}
