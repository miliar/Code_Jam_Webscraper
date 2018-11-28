#include <fstream>
#include <iostream>
#define DN 100005
using namespace std;
 
ifstream fin("B-large.in");
// ifstream fin("input.txt");
ofstream fout("output.txt");

void make9(string &s, int ind) {
    for (;ind < s.size(); ++ind)
        s[ind] = '9';
}

void propagate_backwards(string &s, int ind) {
    if (ind == 0) {
        if (s[ind] == '0')
            s.erase(0, 1);
        return;
    }
    if (s[ind] < s[ind-1]) {
        s[ind-1]--;
        s[ind] = '9';
        propagate_backwards(s, ind-1);
    }
}

void solve(string &s) {
    for (int i = 0; i < s.size()-1; ++i) {
        if (s[i] > s[i+1]) {
            make9(s, i+1);
            --s[i];
            propagate_backwards(s, i);
            break;
        }
    }
}

int main() {
    int t, res;
    string s;
    fin >> t;
    for (int tst = 0; tst < t; ++tst) {
        fin >> s;
        solve(s);
        fout << "Case #" << tst+1 << ": ";
        fout << s;
        fout << '\n';
    }
    return 0;
}