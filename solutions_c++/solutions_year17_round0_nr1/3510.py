#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

string s;

string solve(int n) {
    int i, j, k=0;
    for(i=0; i<s.length(); ++i) {
        if(s[i] == '-') {
            if(i + n > s.length()) {
                return "IMPOSSIBLE";
            }
            k++;
            for(j=i; j<i+n; ++j) {
                s[j] = (s[j] == '+') ? '-' : '+';
            }
        }
    }
    stringstream ss;
    ss << k;
    return ss.str();
}

int main() {
    int t, n, tt;
    fin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        fin >> s >> n;
        fout << "Case #" << tt << ": " << solve(n) << endl;
    }
    return 0;
}