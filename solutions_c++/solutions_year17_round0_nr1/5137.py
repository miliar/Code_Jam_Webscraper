#include <iostream>
#include <fstream>
using namespace std;
#define dbg

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
        int K;
        in >> S >> K;
        int len = S.size();
        int cnt = 0;
        for (int i = 0; i < len - K + 1; i++) {
            if (S[i] == '-') {
                cnt++;
                for (int j = 0; j < K; j++) {
                    if (S[i + j] == '-') {
                        S[i + j] = '+';
                    } else {
                        S[i + j] = '-';
                    }
                }
            }
        }
        bool completed = true;
        for (int i = 0; i < len; i++) {
            if (S[i] == '-') {
                completed = false;
                break;
            }
        }
        out << "Case #" << t << ": ";
        if (completed) {
            out << cnt;
        } else {
            out << "IMPOSSIBLE";
        }
        out << endl;
    }
    return 0;
}

