#include <cstdio>
#include <cstring>

int K, mi = 500, len;
bool dyn[2005];
char str[1005];

void flip(int pos, int cnt, int t){
    t|=(1<<pos);
    if(dyn[t])
        return;
    dyn[t] = true;
    if(cnt >= mi)
        return;
    bool chk = true;
    for(int i = pos; i < pos+K; ++i){
        if(str[i] == '+')
            str[i] = '-';
        else if(str[i] == '-')
            str[i] = '+';
    }
    for(int i = 0; i < len; ++i){
        if(str[i] == '-'){
            chk = false;
            break;
        }
    }
    if(chk){
        if(cnt < mi)
            mi = cnt;
        for(int i = pos; i < pos+K; ++i){
            if(str[i] == '+')
                str[i] = '-';
            else if(str[i] == '-')
                str[i] = '+';
        }
        return;
    }
    for(int i = 0; i <= len-K; ++i){
        if(i == pos)
            continue;
        flip(i, cnt+1, t);
    }
    for(int i = pos; i < pos+K; ++i){
        if(str[i] == '+')
            str[i] = '-';
        else if(str[i] == '-')
            str[i] = '+';
    }
    return;
}

int main(){
    int totalCases;
    scanf("%d", &totalCases);
    for(int T = 1; T <= totalCases; ++T){
        for(int i = 0; i < 2000; ++i)
            dyn[i] = false;
        mi = 500;
        scanf("%s", str);
        scanf("%d", &K);
        len = strlen(str);
        bool chk = true;
        for(int i = 0; i < len; ++i){
            if(str[i] == '-'){
                chk = false;
                break;
            }
        }
        if(chk)
            mi = 0;
        for(int i = 0; i <= len-K; ++i){
            flip(i, 1, (1<<i));
        }
        printf("Case #%d: ", T);
        if(mi == 500)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", mi);
    }
    return 0;
}
