#include <iostream>
#include <fstream>
#include <map>

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


void pm(std::map<int, int, std::greater<int>> const& m) {
    for (auto& it : m) {
        out << it.first << " " << it.second << endl;
    } 
}

int main(int argc, char** argv) {

    int T;
    in >> T;
    for (int t = 1; t <= T; t++) {
        int N; int K;
        in >> N >> K;
        map<int, int, std::greater<int>> all;
        all.insert(make_pair(N, 1));
        while (K > 1) {
//            out << "K = " << K << " ; m=";
//            pm(all);
            int size = all.begin()->first - 1;
            --all.begin()->second;
            if (all.begin()->second == 0) {
                all.erase(all.begin());
            }
            int l = size / 2;
            int r = size - l;
            all[l]++;
            all[r]++;
            K--;
        }
//        out << "end ; m=";
//        pm(all);
        int size = all.begin()->first - 1;
        int l = size / 2;
        int r = size - l;
        out << "Case #" << t << ": " << r << " " << l << endl;
    }
    return 0;
}

