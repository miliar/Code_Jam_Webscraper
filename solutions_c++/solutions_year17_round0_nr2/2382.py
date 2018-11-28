#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long int LL;

LL getTidyNumber(LL n){
    char str[30];
    sprintf(str, "%lld", n);
    bool done = false;
    int len = strlen(str);
    while(!done){
        int i;
        for(i = 0; i < len-1; i++){
            if(str[i] > str[i+1]){
                str[i]--;
                for(int j = i+1; j < len; j++){
                    str[j] = '9';
                }
                break;
            }
        }
        if(i == len-1){
            done = true;
        }
    }
    LL re;
    sscanf(str, "%lld", &re);
//    printf("n  : %lld\n", n);
//    printf("str: %s\n", str);
//    printf("re : %lld\n", re);
    return re;
}

int main(void){
    int t;
    LL n;
    scanf("%d", &t);
    for(int tc = 1; tc <= t; tc++){
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", tc, getTidyNumber(n));
    }
    return 0;
}
