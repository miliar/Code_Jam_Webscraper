#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define maxn 1010

char ch[maxn];

int main() {
    freopen("A-Large.in", "r", stdin);
    freopen("A-Large.out", "w", stdout);
    int T, num = 0;
    scanf("%d", &T);
    while(T--) {
        int k;
        scanf("%s%d", ch, &k);
        int cnt = 0, len = strlen(ch);
        for(int i = 0; i < len-k; i++) {
            if(ch[i] == '-') {
                cnt++;
                for(int j = i; j <= i+k-1; j++) {
                    if(ch[j] == '+') ch[j] = '-';
                    else ch[j] = '+';
                }
            }
        }
        bool flag = true;
        for(int i = len-k+1; i < len; i++)
            if(ch[i] != ch[i-1]) flag = false;
        if(!flag) printf("Case #%d: IMPOSSIBLE\n", ++num);
        else printf("Case #%d: %d\n", ++num, cnt + (ch[len-1] == '-'));
    }
}
