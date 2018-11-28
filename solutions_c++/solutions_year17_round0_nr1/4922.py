#include <bits/stdc++.h>

using namespace std;

char str[1100];

int main(){
    int t, k, ans;
    bool possible;

    scanf("%d", &t);

    for( int tc = 1; tc <= t; tc++ ){
        ans = 0;
        possible = true;
        scanf("%s %d", str, &k);

        for( int i = 0; i < strlen(str); i++ ){
            if ( str[i] == '-' && i + k <= strlen(str) ){
                ans++;
                for( int j = i; j < i+k; j++ ){
                    if ( str[j] == '-' ){
                        str[j] = '+';
                    } else {
                        str[j] = '-';
                    }
                }
            }
        }

        for( int i = 0; i < strlen(str); i++ ){
            if ( str[i] == '-' ){
                possible = false;
            }
        }

        printf("Case #%d: ", tc);
        if ( possible ){
            printf("%d\n", ans);
        } else {
            puts("IMPOSSIBLE");
        }
        
    }
    
}