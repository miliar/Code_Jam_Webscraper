#include <cstdio>
#include <cstring>

using namespace std;
#define MAXN 1005
char str[MAXN];

int check(int s, int e){
    char first;
    first = str[s];
    for(int i = s+1; i < e; i++){
        if(str[i] != first){
            return -1;
        }
    }
    return (first == '+') ? 1 : 0;
}
void flip(int i, int k){
    for(int j = i; j < i+k; j++){
        str[j] = (str[j]=='+')?'-':'+';
    }
}
int solve(int k, int n){
    int ret, cnt, i;
    cnt = i = 0;
    if(k > n){
        return -1;
    }
    while(i < n){
        if(n-i == k){
            ret = check(i, n);
            if(ret == -1){
                return -1;
            }else{
                if(ret == 0){
                    cnt++;
                }
                return cnt;
            }
        }else{
            if(str[i] == '+'){
                i++;
            }else{
                flip(i, k);
                cnt++;
            }
        }
    }
    return cnt;
}

int main(){
    int t, k, n, res;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        scanf("%s", str);
        scanf("%d", &k);
        n = strlen(str);
        res = solve(k, n);
        if(res == -1){
            printf("Case #%d: IMPOSSIBLE\n", i);
        }else{
            printf("Case #%d: %d\n", i, res);
        }
    }
}
