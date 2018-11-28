#include <fstream>
#include <iostream>
#define DN 100005
using namespace std;
 
ifstream fin("A-large.in");
ofstream fout("output.txt");

void flip(string &s, int ind, int len) {
    for (int i = ind; i < ind+len; ++i)
        if (s[i] == '-')
            s[i] = '+';
        else
            s[i] = '-';
}

int solve(string &s, int k) {
    int res = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s.size() - i < k) {
            if (s[i] == '-')
                return -1;
            continue;
        }
        if (s[i] == '-') {
            ++res;
            flip(s, i, k);
        }
    }
    return res;
}

int main() {
    int t, k, res;
    string s;
    fin >> t;
    for (int tst = 0; tst < t; ++tst) {
        fin >> s >> k;
        res = solve(s, k);
        fout << "Case #" << tst+1 << ": ";
        if (res != -1)
            fout << res;
        else
            fout << "IMPOSSIBLE";
        fout << '\n';
    }
    return 0;
}