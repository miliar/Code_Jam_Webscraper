/*************************************************************************
	> File Name: QualificationRound_A.cpp
	> Author: BMan
	> Mail: luo-kai-jia@163.com
	> Created Time: Sat 08 Apr 2017 12:10:03 PM CST
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int _T = 0;
    scanf("%d", &_T);
    char s[2000];
    for (int _t = 1; _t <= _T; _t++)  {
        int K;
        scanf("%s %d", s, &K);
        int len = strlen(s);
        int cnt = 0;
        for (int i = 0; i < len - (K - 1); i++) {
            if (s[i] == '+') continue;
            cnt++;
            for (int j = i; j < i + K; j++) {
                if (s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }
        
        bool check = true;
        for (int i = 0; i < len; i++) {
            if (s[i] == '-') check = false;
        }
        
        if (check)
            printf("Case #%d: %d\n", _t, cnt);
        else 
            printf("Case #%d: %s\n", _t, "IMPOSSIBLE");
    }
    return 0;
}
