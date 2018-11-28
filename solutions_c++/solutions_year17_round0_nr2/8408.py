#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

bool Tidy (int x) {
    stringstream ss;
    ss << x;
    string s = ss.str();
    for (int i = 1; i < s.length(); i++) {
        if ((int)s[i] < (int)s[i-1])
            return false;
    }
    return true;
}

int main () {
    ifstream fin ("tidyNumbersSmallIN.txt");
    ofstream fout ("tidyNumbersSmallOUT.txt");
    int T;
    fin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        fin >> N;
        int lastTidy = 1;
        for (int i = 1; i <= N; i++) {
            if (Tidy(i))
                lastTidy = i;
        }
        fout << "Case #" << (t+1) << ": " << lastTidy << "\n";
    }
    return 0;
}
