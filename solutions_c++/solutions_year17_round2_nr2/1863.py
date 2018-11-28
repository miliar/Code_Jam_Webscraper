#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#define DN 500005
#define ALPH_SIZE 26
using namespace std;

// ifstream fin("input.txt");
ifstream fin("B-small-attempt1.in");
ofstream fout("output.txt");

int no[10], lb;

bool fill(char last, string &res) {
    if (no[1] && last != 'R') {
        res += 'R';
        --no[1];
        return true;
    } else if (no[2] && last != 'Y') {
        res += 'Y';
        --no[2];
        return true;
    } else if (no[4] && last != 'B') {
        if (lb == -1)
            lb = res.size();
        res += 'B';
        --no[4];
        return true;
    }
    return false;
}

bool fill2(string &res) {
    if (no[4] && lb > 0) {
        lb --;
        if (lb == -1)
            res.insert(0, 1, 'B');
        else
            res.insert(lb, 1, 'B');
        return true;
    }
    return false;
}

int main() {
    int T, n;
    fin >> T;
    for (int tst = 1; tst <= T; ++tst) {
        fin >> n;
        string res = "";
        lb = -1;
        int ok = 1;
        fin >> no[1] >> no[3] >> no[2] >> no[6] >> no[4] >> no[5];
        fout << "Case #" << tst << ": ";
        for (int i = 0; i < n; ++i) {
            char last = 'A';
            if (res.size()) last = res.back();
            if(!fill(last, res) && !fill2(res)) {
                ok = 0;
                break;
            }
        }
        if (ok && res.back() != res[0])
            fout << res;
        else
            fout << "IMPOSSIBLE";
        fout << '\n';
    }
    return 0;
}