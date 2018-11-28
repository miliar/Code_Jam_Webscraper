#include<bits/stdc++.h>
using namespace std;

char s[32];

int check(){
    int idx = -1;
    for(int j = 1; s[j]; j ++){
        if(s[j] < s[j - 1]){
            idx = j - 1; break;
        }
    }
    return idx;
}

int main(){
    freopen("2.txt", "r", stdin);
    freopen("1.txt", "w", stdout);
    int T; scanf("%d", &T);
    for(int cas = 1; cas <= T; cas ++){
        scanf("%s", s + 1);
        s[0] = '0';
        int idx = -1;
        for(int j = 1; s[j]; j ++){
            if(s[j] < s[j - 1]){
                idx = j - 1; break;
            }
        }
        printf("Case #%d: ", cas);
        if(idx == -1) puts(s + 1);
        else{
            while(idx != -1){
                s[idx] -= 1;
                for(int i = idx + 1; s[i]; i ++) s[i] = '9';
                idx = check();
            }
            for(int i = 0; s[i]; i ++){
                if(s[i] != '0'){
                    puts(s + i);
                    break;
                }
            }
        }
    }
    return 0;
}
