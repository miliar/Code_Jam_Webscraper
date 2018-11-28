#include <bits/stdc++.h>
#define SIZE 1105
using namespace std;
char str[SIZE];
int ara[SIZE];
int n, k;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cs=0;
    scanf("%d", &t);
    while(t--){
        scanf("%s%d", str, &k);
        n=strlen(str);
        memset(ara, 0, sizeof(ara));
        int val=0;
        for(int i=0; i<n; i++){
            int cnt=0;
            for(int j=max(i-k+1, 0); j<i; j++){
                if(ara[j]==1){
                    cnt++;
                }
            }
            if(str[i]=='+'){
                ara[i]=cnt%2;
                val+=cnt%2;
            }
            else{
                if((cnt%2)==0){
                    ara[i]=1;
                    val++;
                }
            }
        }
        bool fg=0;
        for(int j=max(n-k+1, 0); j<n; j++){
            if(ara[j]==1){
                fg=1;
            }
        }
        if(fg) printf("Case #%d: IMPOSSIBLE\n", ++cs);
        else printf("Case #%d: %d\n", ++cs, val);
    }
    return 0;
}
