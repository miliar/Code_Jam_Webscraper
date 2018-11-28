/*************************************************************************
	> File Name: QualificationRound_B.cpp
	> Author: BMan
	> Mail: luo-kai-jia@163.com
	> Created Time: Sat 08 Apr 2017 12:27:17 PM CST
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;

int main() {
   int _T = 0;
    scanf("%d", &_T);
    for (int  _t = 1; _t <= _T; _t++) {
        char s[20];
        scanf("%s", s);
        int pos = -1;
        int sz = (int)strlen(s);
        for (int i = 0; i < sz - 1; i++) {
            if (s[i + 1] > s[i]) continue;
            if (s[i + 1] < s[i]) {
                pos = i;
                break;
            }
            int j = i + 1;
            while(j < sz && s[j] == s[i]) j++;
            if (j == sz) break;
            if (s[j] < s[i]) {
                pos = i;
                break;
            }
        }

        printf("Case #%d: ", _t);

        if (pos == -1) {
            printf("%s", s);
        } else if (pos == 0 && s[0] == '1') {
            for (int i = 1; i < sz; i++) {
                printf("9");
            }
        } else {
            for (int i = 0; i < sz; i++) {
                char c;
                if (i < pos) c = s[i];
                else if (i == pos) c = s[i] - 1;
                else c = '9';
                printf("%c", c);
            }
        }
        printf("\n");
    }
    return 0;
}
