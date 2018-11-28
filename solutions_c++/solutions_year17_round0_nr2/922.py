#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main() {
        ifstream input;
        ofstream res;
        int T;
        input.open("./Downloads/B-large.in");
        res.open("result_cj_q_20170407_Bl.out");
        input >> T;
        for (int t = 0; t < T; t ++) {
                unsigned long long N;
                input >> N;
                vector<unsigned> dig;
                while (N) {
                        dig.push_back(N % 10);
                        N = N / 10;
                }
                bool ch = false;
                for (int i = dig.size() - 1; i >= 1; i --) {
                        if (ch) {
                                dig[i] = 9;
                        } else if (dig[i] > dig[i - 1]) {
                                ch = true;
                                dig[i] --;
                                int st = i;
                                while (st < dig.size() - 1 && dig[st] < dig[st + 1]) {
                                        dig[st] = 9;
                                        dig[st + 1] --;
                                        st ++;
                                }
                        }
                        
                }
                if (ch) {
                        dig[0] = 9;
                }
                unsigned long long ret = 0;
                for (int i = dig.size() - 1; i >= 0; i --) {
                        ret = ret * 10 + dig[i];
                }
                res << "Case #" << t + 1 << ": " << ret << endl;
        }
        input.close();
        res.close();
}
