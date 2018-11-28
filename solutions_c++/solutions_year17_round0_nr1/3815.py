#include <bits/stdc++.h>
using namespace std;

char s[1010];
int n,ans = 30,k;


int main() {
    freopen("in.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cs = 1;
    while(t--){
        scanf(" %s %d",s,&k);
        int nn = strlen(s);
        n = nn-k+1;
        ans = 0;
        for(int i=0;i<n;i++){
            if(s[i] == '-'){
                for(int j=i;j<i+k;j++){
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
                ans++;
            }
        }
        bool can =1 ;
        for(int i=0;i<nn;i++){
            if(s[i] == '-')
                can = 0;
        }
        printf("Case #%d: ",cs++);
        if(!can){
            puts("IMPOSSIBLE");
        }
        else{
            printf("%d\n",ans);
        }
    }
    return 0;
}
