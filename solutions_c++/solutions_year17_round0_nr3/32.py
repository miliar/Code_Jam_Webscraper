


/*
    Prob:
    Author: 
    Time:   
    Description:
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int T;
long long n, m;

vector<long long> num, cnt;

int main(int argc, char* argv[]) { 
    if (argc >= 2) {
        string post = argv[1][0] == 's' ? 
                      "-small-" + string(argv[2]) + "-attempt" + string(argv[3]):
                      "-large";  
        string input_file  = string(argv[0]) + post + ".in",
               output_file = string(argv[0]) + post + ".ans";
        freopen(input_file.c_str(), "r", stdin);
        freopen(output_file.c_str(), "w", stdout);
    }
    
    cin >> T;
    for (int testcase = 1; testcase <= T; ++ testcase) {
        cin >> n >> m;
        num.clear(); cnt.clear();
        num.push_back(n);
        cnt.push_back(1);
        
        long long pos = 0, sum = 0;
        while (sum + cnt[pos] < m) {
            long long tmpl = num[pos] >> 1, tmps = (num[pos] - 1) >> 1;
            if (tmpl != num[num.size() - 1]) {
                num.push_back(tmpl);
                cnt.push_back(0);
            }
            cnt[cnt.size() - 1] += cnt[pos];
            if (tmps != num[num.size() - 1]) {
                num.push_back(tmps);
                cnt.push_back(0);
            }
            cnt[cnt.size() - 1] += cnt[pos];
            sum += cnt[pos ++];
        }

        long long ansl = num[pos] >> 1, anss = (num[pos] - 1) >> 1;
        cout << "Case #" << testcase << ": " << ansl << " " << anss << endl;
    }
    
    return 0;
}