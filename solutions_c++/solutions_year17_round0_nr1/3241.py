//
//  main.cpp
//  17_qual_A
//
//
//
//

#include <iostream>
#include <cstdio>
#include <cstring>

int main() {
    int t, ans, y, k;
    scanf("%d\n", &t);
    char s[1005];
    bool z;
    for(int i=1; i<=t; i++){
        scanf("%s %d", s, &k);
        y=strlen(s);
        ans=0;
        for(int j=y-1; j>=k-1; j--){
            if(s[j]=='-'){
                ans++;
                for(int l=0; l<k; l++) s[j-l]='+'+'-'-s[j-l];
            }
        }
        z=true;
        for(int j=0; j<k && z; j++) if(s[j]=='-') z=false;
        printf("Case #%d: ", i);
        if(z) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
