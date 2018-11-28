//
//  main.cpp
//  17_round_1A_A
//
//
//
//

#include <iostream>
#include <cstdio>

int main() {
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out.txt", "w", stdout);
    int t, r, c;
    char s[26][26];
    scanf("%d\n", &t);
    for(int i=1; i<=t; i++){
        scanf("%d %d", &r, &c);
        for(int j=0; j<r; j++){
            scanf("\n");
            for(int k=0; k<c; k++) scanf("%c", &s[j][k]);
        }
        for(int j=0; j<r; j++){
            for(int k=1; k<c; k++) if(s[j][k]=='?') s[j][k]=s[j][k-1];
            for(int k=c-2; k>=0; k--) if(s[j][k]=='?') s[j][k]=s[j][k+1];
        }
        for(int k=0; k<c; k++){
            for(int j=1; j<r; j++) if(s[j][k]=='?') s[j][k]=s[j-1][k];
            for(int j=r-2; j>=0; j--) if(s[j][k]=='?') s[j][k]=s[j+1][k];
        }
        printf("Case #%d:\n", i);
        for(int j=0; j<r; j++){
            for(int k=0; k<c; k++) printf("%c", s[j][k]);
            printf("\n");
        }
    }
    return 0;
}