#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main(int argc, char* argv[]) {
    ifstream in ("B-large.in");
    ofstream out ("output.out");
    
    int T;
    in >> T;
    char N[19];
    char input;
    int size;
    
    for (int i = 0; i < T; i++) {
        size = 1;
        in >> input;
        while (input != '\n') {
            N[size - 1] = input;
            size++;
            in >> noskipws >> input;
        }
        
        if (size == 1) {
            out << "Case #" << i+1 << ": " << N[0] << endl;
        } else {
            out << "Case #" << i+1 << ": ";
            for (int i = size - 1; i != 0; i--) {
                if (N[i] < N[i-1]) {
                    N[i-1] = N[i-1] - 1;
                    for (int j = i; j < size; j++) {
                        N[j] = '9';
                    }
                }
            }
            int start = 1;
            for (int i = 0; i < size - 1; i++) {
                if (!(start == 1 && N[i] == '0')) {
                    out << N[i];
                    start = 0;
                }
            }
            out << endl;
        }
    }
}
                
