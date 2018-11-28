#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

typedef long long int lli;

int main(){
    ios :: sync_with_stdio(false);
    cin.tie(NULL);
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    lli t,len,ans,k;
    char str[1000 + 100];
    bool possible = true;
    scanf("%lld",&t);

    for(lli i_t = 0; i_t < t; i_t++){
        possible = true;
        scanf("%s %lld",str,&k);
        ans = 0;
        len = strlen(str);

        for(lli i = 0; i < len - k + 1; i++){
            if(str[i] == '-'){
                for(lli j = 0; j < k; j++){
                    if(str[i+j] == '-'){
                        str[i+j] = '+';
                    }
                    else{
                        str[i+j] = '-';
                    }
                }
                ans++;
            }
        }

        for(lli i = 0; i < len; i++){
            if(str[i] == '-')
                possible = false;
        }

        if(possible){
            printf("Case #%lld: %lld\n",i_t + 1, ans);
        }
        else{
            printf("Case #%lld: IMPOSSIBLE\n",i_t+1);
        }
    }

}
