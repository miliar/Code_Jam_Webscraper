#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
char s[10005];
int main(){
    int t,T=0;;
    scanf("%d",&t);
    while(t--){T++;
        int k;
        scanf("%s%d",s,&k);
        int n=strlen(s);
        int ans=0;
        for(int i=0;i<n-k+1;i++){
            if(s[i]=='-'){
                ans++;
                for(int j=0;j<k;j++)
                    s[i+j]=s[i+j]=='-'?'+':'-';
                }
            }
        for(int i=0;i<n;i++)
            if(s[i]=='-')
                ans=-1;
        printf("Case #%d: ",T);
        if(~ans)
            printf("%d\n",ans);
        else
            printf("IMPOSSIBLE\n");
        }
    return 0;
    }
