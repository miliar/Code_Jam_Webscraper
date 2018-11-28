#include<bits/stdc++.h>
using namespace std;

const int maxn = 112345;

char inp[maxn];

int main(){
    int T;
    scanf("%d",&T);
    int icase = 1;
    int n,k;
    while(T-- && ~scanf("%s %d",inp,&k)){
        n = strlen(inp);
        int ans = 0;
        for(int i = 0 ; i <= n - k ; i ++){
            if(inp[i] == '-'){
                ans++;
                for(int j = 0 ; j < k ; j ++){
                    inp[i+j] = inp[i+j] == '+' ? '-' : '+';
                }
            }
        }
        for(int i = 0 ; i < k ; i ++){
            if(inp[n-i-1] == '-')
                ans = -1;
        }
        printf("Case #%d: ",icase++);
        if(ans != -1){
            printf("%d\n",ans);
        }
        else{
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
