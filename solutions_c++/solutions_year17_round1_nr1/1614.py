#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
    ifstream in ("A-large.in");
    ofstream out("out.out");
    
    int T;
    in >> T;
    int R;
    int C;
    for (int i = 0; i < T; i++) {
        in >> R;
        in >> C;
        char cake[R][C];
        
        for (int j = 0; j < R; j++) {
            for (int k = 0; k < C; k++) {
                in >> cake[j][k];
            }
        }
        
        
        for (int j = 1; j < R; j++) {
            for (int k = 0; k < C; k++) {
                if (cake[j][k] == '?') {
                    cake[j][k] = cake[j-1][k];
                }
            }
        }
        
        for (int j = R-2; j >= 0; j--) {
            for (int k = 0; k < C; k++) {
                if (cake[j][k] == '?') {
                    cake[j][k] = cake[j+1][k];
                }
            }
        }
        
        for (int k = 1; k < C; k++) {
            for (int j = 0; j < R; j++) {      
                if (cake[j][k] == '?') {
                    cake[j][k] = cake[j][k-1];
                }
            }
        }
        
        for (int k = C-2; k >= 0; k--) {
            for (int j = 0; j < R; j++) {
                if (cake[j][k] == '?') {
                    cake[j][k] = cake[j][k+1];
                }
            }
        }
        out << "Case #" << i+1 << ":\n";
        for (int j = 0; j < R; j++) {
            for (int k = 0; k < C; k++) {
                out << cake[j][k];
            }
            out << endl;
        }
        
    }
    
    return 0;
}
