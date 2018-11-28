#include <bits/stdc++.h>
using namespace std;
const int N  = 103;
char str[N];
int num[N], ans[N], len;


bool dfs(int pos, int nowNum, bool start){
    ans[pos] = nowNum;
    if(pos == len - 1) return true;
    int from = start ? num[pos + 1] : 9;
    if(nowNum > from) return false;

    for(int i = from; i >= nowNum; i--){ // no decrease
        if(dfs(pos + 1, i, start && i == num[pos+1])) return true;
    }
    return false;
}
int main(){


    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T, t;
    int k;
    scanf("%d", &T);
    for(t = 1; t <= T; t++){
        printf("Case #%d: ", t);
        scanf("%s", str);
        len = strlen(str);
        for(int i = 0; i < len; i++) num[i] = str[i] - '0';

        memset(ans, 0, sizeof(ans));
        for(int i = num[0]; i >= 0; i--){
            if (dfs(0, i, i == num[0])) break;
        }
        int i = 0;
        while(i < len && ans[i] == 0 ) i++;
        while(i < len) printf("%c", ans[i++] + '0');
        printf("\n");

    }
    return 0;
}
