#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    int T;
    cin >> T;
    string str;
    bool S[1001];
    int K;
    for(int tc=1;tc<=T;tc++) {
        cin >> str >> K;
        int len = str.length();
        for(int i=0;i<len;i++) {
            if(str[i] == '+') S[i] = 1;
            else S[i] = 0;
        }
        int ans = 0;
        bool isImpossible = false;
        for(int i=0;i<len;i++) {
            if(S[i] == 0) {
                if(i+K > len) {
                    isImpossible = true;
                    break;
                }
                for(int j=i;j<i+K;j++) {
                    S[j] = 1 - S[j];
                }
                ans++;
            }
        }

        if(!isImpossible) {
            printf("Case #%d: %d\n", tc, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", tc);
        }
    }
    return 0;
}
