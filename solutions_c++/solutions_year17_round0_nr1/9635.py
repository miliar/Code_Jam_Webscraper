#include <stdio.h>
#include <string.h>

int main(){
    int a;
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int n;
    scanf("%d",&a);
    for(int i = 0; i < a;i++){
        char arr[1020];
        int dp[1020];
        int x;
        char c;
        scanf("%c",&c);
        int ctr = 0;
        scanf("%s %d",arr,&x);
        int ans = 0;
        int cnt = 0;
        int subs = 0;
        if(arr[0] == '-') dp[0] = 1;
        else{
            dp[0] = 0;
        }
        int len = strlen(arr);
        for(int i = 0; arr[i] != '\0';i++,cnt++){

            if( arr[i] == '-' && i+x <= len ){
                ctr++;
                for(int j = 0,k=i; arr[k] != '\0' && j < x;j++,k++){
                    if(arr[k] == '-'){
                        dp[k] = ctr;
                        arr[k] = '+';
                    }
                    else {
                        dp[k] = dp[k-1]+1;

                        arr[k] = '-';
                    }
                }

            }
            else if( i-1 >= 0 && arr[i] == '+') {
                dp[i] = dp[i-1];
            }
            if(arr[i] == '+') ans++;
        }
        if(ans == cnt){
            printf("Case #%d: %d\n",i+1,dp[ans-1]);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n",i+1);

        }
    }

    return 0;
}
