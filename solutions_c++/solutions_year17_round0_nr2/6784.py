#include <cstdio>
#include <cstring>
typedef long long LL;

LL tp[19];
char s[30], tmp[30];

int main() {
    tp[0] = 0;
    tp[1] = 1ll;
    for(int i = 2; i <= 18; i++) {
        tp[i] = tp[i-1]*10ll;
    }
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        scanf("%s", s);
        bool flag;
        while(true){
            flag = false;
            int len = strlen(s);
            for(int i = 1; i < len; i++) {
                if(s[i] < s[i-1]){
                    flag = true;
                    int k = i-1;
                    while(s[k] == '0' && k-- >= 0);
                    if(k == 0 && s[k] == '1') {
                        memset(s,0,sizeof(s));
                        for(int w = 0; w+i < len; w++) s[w] = '9';
                    } else {
                        s[k]--;
                        for(int w = k+1; w < len;w++) s[w] = '9';
                    }
                    break;
                }
            }
            if(!flag) break;
        }
        printf("Case #%d: %s\n", t,s);
    }
    return 0;
}