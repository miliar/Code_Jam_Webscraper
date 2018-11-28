#include <iostream>
#include <set>
#include <cstdlib>
#include <stdexcept>
#include <cassert>
#include <string>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int T,cas;
char s[22];

bool check(){
    for (int i=1; s[i]; i++){
        if (s[i]<s[i-1]){
            s[i-1]--;
            for (int j=i; s[j]; j++)
                s[j]='9';
            return true;
        }
    }
    return false;
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.txt", "w", stdout);
    scanf("%d", &T);
    for (cas=1; cas<=T; cas++){
        scanf("%s", s);
        while (check()) ;
        int cur =0;
        while (s[cur]=='0')
            cur++;

        printf("Case #%d: ", cas);
        for (int i=cur; s[i]; i++)
            printf("%c", s[i]);
        printf("\n");
    }
    return 0;
}
