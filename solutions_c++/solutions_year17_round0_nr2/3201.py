//
//  main.cpp
//  17_qual_B
//
//
//
//

#include <iostream>
#include <cstdio>
#include <cstring>

int main() {
    freopen("B-large.in.txt", "r", stdin);
    freopen("B-large.out.txt", "w", stdout);
    int t, y;
    scanf("%d", &t);
    char s[20];
    bool z;
    for(int i=1; i<=t; i++){
        scanf("%s", s);
        y=strlen(s);
        z=true;
        for(int j=1; j<y && z; j++){
            if(s[j-1]>s[j]){
                s[j-1]--;
                for(int k=j; k<y; k++) s[k]='9';
                for(int k=j-2; k>=0 && z; k--){
                    if(s[k]>s[k+1]){
                        s[k]--;
                        s[k+1]='9';
                    }
                    else z=false;
                }
                z=false;
            }
        }
        printf("Case #%d: ", i);
        if(s[0]=='0') printf("%s\n", s+1);
        else printf("%s\n", s);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}