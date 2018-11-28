#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
        ifstream input;
        ofstream res;
        int T;
        input.open("./Downloads/A-large.in");
        res.open("result_cj_q_20170407_Al.out");
        input >> T;
        for (int t = 0; t < T; t ++) {
                string s;
                input >> s;
                int len;
                input >> len;
                int ret = 0;
                for (int i = 0; i < s.length(); i ++) {
                        if (i + len > s.length()) {
                                if (s[i] == '-') {
                                        ret = -1;
                                        break;
                                }
                        } else if (s[i] == '-'){
                                ret ++;
                                for (int j = 0; j < len; j ++) {
                                        s[i + j] = (s[i + j] == '-') ? '+' : '-';
                                }
                        }
                }
                res << "Case #" << t + 1 << ": ";
                if (ret < 0) {
                        res << "IMPOSSIBLE" << endl;
                } else {
                        res << ret << endl;
                }
        }
        input.close();
        res.close();
}
