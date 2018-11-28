#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    int t;
    string s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> s; 
        bool done = true; 
        while (done) {
            int n = -9999999;
            bool tidy = true;
            for (char c : s) {
                int cc = c - 48;
                if (cc >= n) { 
                    n = cc;
                }
                else {
                    tidy = false;
                    break;
                }
            }
            if (!tidy) {
                long long cTidy = atol(s.c_str());
                cTidy = cTidy - 1;
                stringstream ss;
                ss << cTidy;
                s.assign(ss.str());
            } else {
                done = false;
            }
        }
        cout << "Case #" << i << ": " << s << endl;
    }
    return 0;
}
