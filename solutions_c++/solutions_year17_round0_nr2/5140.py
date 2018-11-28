#include <iostream>
#include <fstream>
using namespace std;
//#define dbg

int main(int argc, char** argv) {

#ifndef dbg
    istream &in = cin;
    ostream& out = cout;
#else
    ifstream input("/Users/smakarenko/input.txt");
    istream &in = input;
    ofstream outf("/Users/smakarenko/out.txt");
    ostream& out = outf;
#endif
    int T;
    in >> T;
    for (int t = 1; t <= T; t++) {
        string S;
        in >> S;
        for (int i = S.size() - 1; i > 0; i--) {
//            out << "i=" << i << "; S=" << S << endl;
            char& cur = S[i];
            char& prev = S[i - 1];
            if (prev > cur) {
                prev--;
                for (int j = i; j < S.size(); j++) {
                    S[j] = '9';
                }
            }
        }
        if (S[0] == '0') {
            S = S.substr(1);
        }
        out << "Case #" << t << ": " << S << endl;
    }
    return 0;
}

