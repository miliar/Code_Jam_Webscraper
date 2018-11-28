//
//  main.cpp
//  Problem B Tidy Numbers
//
//  Created by Parinthorn Saithong on 4/9/2017.
//  Copyright © 2017 Parinthorn Saithong. All rights reserved.
//

#include <iostream>
#include <cstdio>

int main(int argc, const char * argv[]) {
    int t, casei = 0;
    scanf("%d ", &t);
    while(t--) {
        char n[20];
        scanf("%s", n);
        char res[20];
        int i = 0;
        bool remainingNine = false;
        while(n[i] != '\0') {
            if(remainingNine) {
                res[i] = '9';
                ++i;
                continue;
            }
            if(n[i + 1] != '\0') {
                if(n[i] <= n[i + 1]) {
                    res[i] = n[i];
                } else {
                    res[i] = n[i] - 1;
                    int j = i;
                    while(j > 0) {
                        if(res[j] < res[j - 1]) {
                            res[j] = '9';
                            if(res[j - 1] - '0' == 0) {
                                break;
                            }
                            res[j - 1] = res[j - 1] - 1;
                        }
                        --j;
                    }
                    remainingNine = true;
                }
            } else {
                res[i] = n[i];
            }
            ++i;
        }
        res[i] = '\0';
        i = 0;
        printf("Case #%d: ", ++casei);
        while(res[i] != '\0') {
            if(res[i] - '0' != 0)
                printf("%c", res[i]);
            ++i;
        }
        printf("\n");
    }
    return 0;
}
