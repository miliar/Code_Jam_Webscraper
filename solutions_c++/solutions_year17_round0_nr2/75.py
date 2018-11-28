#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <thread>
#include <unistd.h>
#include <cstring>
#include <sstream>

using namespace std;


#define ll long long
#define ull unsigned long long
#define uint unsigned int
//long long
#define dot(x,y) ((ll)x[0]*y[0]+ (ll)x[1]*y[1])

#define cleararray(array) memset(array, 0, sizeof(array))

int main() {
    int T;
    cin >> T;

    for (int testcase = 1; testcase <= T; testcase++) {
        ll N;
        cin >> N;

        stringstream ss;
        ss << N;
        string s;
        ss >> s;
        int start = 0;

        char last = s[0];
        int startofrun = 0;
        for (int idx = 1; idx < s.length(); idx++) {
            if (s[idx] < last) {
                char replace = last == '1' ? '9' : last - 1;
                for (int idx2 = idx; idx2 < s.length(); idx2++) {
                    s[idx2] = '9';
                }

                for (idx--; idx > startofrun; idx--) {
                    if (s[idx] == last)
                        s[idx] = '9';
                    else
                        break;
                }
                s[startofrun] = replace;
                if (replace == '9')
                    start = 1;  //trim first

                break;
            }
            if (s[idx] > last)
                startofrun = idx;
            last = s[idx];
        }
        printf("Case #%d: %s\n", testcase, s.substr(start).c_str());
    }
    return 0;
}
