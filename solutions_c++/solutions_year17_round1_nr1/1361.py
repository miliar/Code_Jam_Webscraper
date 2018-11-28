#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
        ifstream input;
        ofstream res;
        int T;
        input.open("./Downloads/A-large.in");
        res.open("result_cj_20170415_Al.out");
        input >> T;
        for (int t = 0; t < T; t ++) {
                unsigned R, C;
                input >> R >> C;
                vector<char> rw(C, 0);
                vector<vector<char> > mp(R, rw);
                for (unsigned i = 0; i < R; i ++) {
                        for (unsigned j = 0; j < C; j ++) {
                                input >> mp[i][j];
                        }
                }
                
                for (unsigned i = 0; i < R; i ++) {
                        for (int j = 0; j < C; j ++) {
                                if (mp[i][j] != '?') {
                                        int k = j - 1;
                                        while (k >= 0 && mp[i][k] == '?') {
                                                mp[i][k] = mp[i][k + 1];
                                                k --;
                                        }
                                        k = j + 1;
                                        while (k < C && mp[i][k] == '?') {
                                                mp[i][k] = mp[i][k - 1];
                                                k ++;
                                        }
                                }
                        }
                }

                for (int i = 0; i < R; i ++) {
                        if (mp[i][0] != '?') {
                                int k = i - 1;
                                while (k >= 0 && mp[k][0] == '?') {
                                        for (int j = 0; j < C; j ++) {
                                                 mp[k][j] = mp[k + 1][j];
                                        }
                                        k --;
                                }
                                k = i + 1;
                                while (k < R && mp[k][0] == '?') {
                                        for (int j = 0; j < C; j ++) {
                                                 mp[k][j] = mp[k - 1][j];
                                        }
                                        k ++;
                                }
                         }
                }

                res << "Case #" << t + 1 << ": " << endl;
                for (unsigned i = 0; i < R; i ++) {
                        for (unsigned j = 0; j < C; j ++) {
                                res << mp[i][j];
                        }
                        res << endl;
                }
        }
        input.close();
        res.close();
}
