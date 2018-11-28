#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool myComp(vector<unsigned long long> const & a, vector<unsigned long long> const & b)
{
        return a[0] < b[0];
}

int main() {
        ifstream input;
        ofstream res;
        int T;
        input.open("./Downloads/C-large.in");
        res.open("result_cj_q_20170407_Cl.out");
        input >> T;
        for (int t = 0; t < T; t ++) {
                unsigned long long N;
                unsigned long long K;
                input >> N;
                input >> K;

                vector<unsigned long long> pair(2, 1);
                pair[0] = N;
                unsigned long long left = 0;
                unsigned long long right = 0;
                vector<vector<unsigned long long> > arr(1, pair);
                while (K) {
                        unsigned long long cnt = arr.back()[1];
                        unsigned long long len = arr.back()[0];
                        right = len / 2;
                        left = ((len % 2) == 0) ? len / 2 - 1 : len / 2;
                        if (K > cnt) {
                                K = K - cnt;
                                vector<unsigned long long> tmp(2, cnt);
                                if (left > 0) {
                                        tmp[0] = left;
                                        auto ptr = lower_bound(arr.begin(), arr.end(), tmp, myComp);
                                        if ((*ptr)[0] == tmp[0]) {
                                                (*ptr)[1] = (*ptr)[1] + cnt;
                                        } else {
                                                arr.insert(ptr, tmp);
                                        }
                                }

                                if (right > 0) {
                                        tmp[0] = right;
                                        auto ptr = lower_bound(arr.begin(), arr.end(), tmp, myComp);
                                        if ((*ptr)[0] == tmp[0]) {
                                                (*ptr)[1] = (*ptr)[1] + cnt;
                                        } else {
                                                arr.insert(ptr, tmp);
                                        }
                                }
                                arr.pop_back();
                        } else {
                                K = 0;
                        }
                }
                res << "Case #" << t + 1 << ": " << right << " " << left << endl;
        }
        input.close();
        res.close();
}
