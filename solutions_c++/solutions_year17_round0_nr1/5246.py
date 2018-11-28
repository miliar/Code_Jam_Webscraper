#include <cstdio>
#include <cstring>
char s[1111];
void flip(int j) {
    if ( s[j] == '-' ) s[j] = '+';
    else if ( s[j] == '+' ) s[j] = '-';
}
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        int K;
        scanf("%s %d",s,&K);
        int ans = 0;
        int len = strlen(s);
        for ( int i = 0 ; i < len-K+1 ; i++ ) {
            if ( s[i] == '-' ) {
                ans ++;
                for ( int j = i ; j < i+K ; j++ ) 
                    flip(j);
            }
        }
        bool imp = false;
        for ( int i = 0 ; i < len ; i++ ) 
            if ( s[i] == '-' ) imp = true;
        if ( imp ) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
