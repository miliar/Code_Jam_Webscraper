#include <bits/stdc++.h>
using namespace std;

int main()
{
   freopen("B-large.in", "r",  stdin);
   freopen("B.out", "w", stdout);
    int t,ca=1;
    char s[20];
    scanf("%d", &t);
    while(t--) {
        scanf("%s", s);
        int n = strlen(s);
        bool flag= true;
        for(int i = 0; i < n; i++) {
            if(s[i] > '1') break;
            if(s[i] == '0') flag=false;
        }
        printf("Case #%d: ", ca++);
        int len = -1;
        char ret[20];
        memset(ret, 0, sizeof(ret));
        if(flag) {
            int pre = '1';
            for(int i = 0; i < n; i++) {
                for(int j = '9'; j >= pre; j--) {
                    bool flag = true;
                    for(int k = i; k < n; k++) {
                        if(s[k] > j) {
                            break;
                        } else if(s[k] < j){
                            flag = false; break;
                        }
                    }
                    if(flag) {
                        ret[i] = j;
                        break;
                    }
                }
                if(ret[i] < s[i]) {
                    for(int j = i + 1; j < n; j++) ret[j] = '9';
                    break;
                }
            }
            printf("%s\n", ret);
        }
        else {
            for(int i = 0; i < n-1;i++) printf("9");
            puts("");
        }
    }
    return 0;
}
