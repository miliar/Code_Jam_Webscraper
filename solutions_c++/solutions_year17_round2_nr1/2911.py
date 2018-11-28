#include <iostream>
#include <fstream>
#include <map>
#include <iomanip>

using namespace std;
//#define dbg

#ifndef dbg
    istream &in = cin;
    ostream& out = cout;
#else
    ifstream input("/Users/smakarenko/input.txt");
    istream &in = input;
    ofstream outf("/Users/smakarenko/out.txt");
    ostream& out = outf;
#endif


int main(int argc, char** argv) {

    int T;
    in >> T;
    for (int t = 1; t <= T; t++) {
        long long D;
        long long H; 
        in >> D >> H;
        map<long long, long long, std::greater<int>> all;
        for (int i = 0; i < H; i++) {
            long long  k;
            long long s;
            in >> k >> s;
            all.insert(make_pair(k, s));
        }
        double curt = 0;
        for (auto & it : all) {
            long long dist = D - it.first;
            double ttime = (double)dist / it.second;
            if (curt < ttime) {
                curt = ttime;
            }
        }
        double result = (double) D / curt;
        out << "Case #" << t << ": " << std::fixed << result << endl;
    }
    return 0;
}
