#include<bits/stdc++.h>

using namespace std;

char s[1005];

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cs = 1; cs <= T; cs++) {
        scanf("%s",s);
        int n = strlen(s);
        for(int it = 0; it < 20; it++) {
            int last = 0;
            for(int i = 0; i < n; i++) {
                int si = s[i] - '0';
                if(si < last) {
                    s[i-1]--;
                    for(int j = i; j < n; j++) s[j] = '9';
                    break;
                }
                last = si;
            }
        }
        printf("Case #%d: ",cs);
        char* temp = s;
        for(int i = 0; i < n; i++) {
            if(s[i] != '0') {
                temp = &s[i];
                break;
            }
        }
        printf("%s\n",temp);
    }

}