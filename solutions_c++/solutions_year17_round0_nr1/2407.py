#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int solve(bool pancakes[], int len, int kk){
    int cnt = 0;
    for(int i = 0; i <= len-kk; i++){
        if(!pancakes[i]){
            for(int j = 0; j < kk; j++){
                pancakes[i+j] = !pancakes[i+j];
            }
            cnt++;
        }
    }
    for(int i = 0; i < len; i++){
        if(!pancakes[i]){
            return -1;
        }
    }
    return cnt;
}

int main(void){
    int tt, kk;
    char str[1010];
    bool pancakes[1010];
    scanf("%d", &tt);
    for(int tc = 1; tc <= tt; tc++){
        scanf("%s%d", str, &kk);
        int len = strlen(str);
        for(int i = 0; i < len; i++){
            pancakes[i] = (str[i] == '+');
        }

        int ans = solve(pancakes, len, kk);
        printf("Case #%d: ", tc);
        if(ans == -1){
            printf("IMPOSSIBLE\n");
        }else{
            printf("%d\n", ans);
        }
    }
    return 0;
}
