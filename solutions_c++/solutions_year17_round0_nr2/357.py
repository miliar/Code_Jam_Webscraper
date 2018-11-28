#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <string>
using namespace std;


// 534
// 499

// 584
// 579
void verfiy(string s, string sol) {
    long long n, sn, correct = 0;
    istringstream iss(s + " " + sol);
    iss >> n >> sn;
    
    for (long long i = 1; i <= n; ++i) {
        ostringstream oss;
        oss << i;
        string tmp = oss.str();
        string ts = tmp;
        sort(ts.begin(), ts.end());
        if (ts == tmp) {
            correct = i;
        }
    }
    if (correct != sn) {
        cerr << "why ?? " << n << ' ' << sn << ' ' << correct << endl;
    }
}

int main () {
    int cases;
    cin >> cases;

    for (int cc = 1; cc <= cases; ++cc) {
        string s, sol;
        cin >> s;

        bool turned = false;
        sol += s[0];
        for (int i = 1; i < s.size(); ++i) {
            if (turned) {
                sol += '9';
                continue;
            }
            if (s[i] < s[i - 1]) {
                --sol[i - 1];
                for (int j = i - 2; j >= 0; --j) {
                    if (sol[j] > sol[j + 1]) {
                        --sol[j];
                        sol[j + 1] = '9';
                    }
                }
                turned = true;
                sol += '9';
            } else {
                sol += s[i];
            }
        }
        if (sol[0] == '0') {
            sol = sol.substr(1);
        }
        //verfiy(s, sol);
        cout << "Case #" << cc << ": " << sol << endl;
    }
}
