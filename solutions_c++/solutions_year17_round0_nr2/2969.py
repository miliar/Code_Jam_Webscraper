#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T;
char s[20];
int main() {
    cin >> T;
    for (int C = 1, k; C <= T; C++) {
        scanf("%s", s);
        int n = strlen(s);
        for (int i = 1; i < n; i++) {
            if (s[i-1] > s[i]) {
                for (int j = i-1; j >= 0; j--) {
                    if (j == 0 || s[j] - 1 >= s[j-1]) {
                        s[j]--;
                        for (int k = j+1; k < n; k++) s[k] = '9';
                        break;
                    }
                }
                break;
            }
        }
        printf("Case #%d: ", C);
        if(n>1 && s[0]=='0') puts(s+1); else puts(s);
    }
}