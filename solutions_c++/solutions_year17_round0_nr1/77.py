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
        string s;
        cin >> s;
        int K;
        cin >> K;

        int flip = 0;
        int w =0;
        for (int idx = 0; idx < s.length() - K + 1; idx++) {
            if (s[idx] =='-') {
                for (int idx2 = 0; idx2 < K; idx2++) {
                    s[idx+idx2] = s[idx+idx2] == '+' ? '-' : '+';
                }
                // flip ^= true;
                w++;
            }
        }
        for (int idx = s.length() - K; idx < s.length(); idx++) {
            if (s[idx] =='-') {
                printf("Case #%d: IMPOSSIBLE\n", testcase);
                goto next;
            }
        }

        printf("Case #%d: %d\n", testcase, w);
      next:
        ;
    }
    return 0;
}
