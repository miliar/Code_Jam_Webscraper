#include<cstdio>
#include<cstdlib>
#include<string>
#include<string.h>
#include<algorithm>
using namespace std;
int main(){
    freopen("inputA","r",stdin);
    freopen("outputA.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        char s[1001];
        scanf("%s",&s);
        int l=strlen(s);
        int k;
        scanf("%d",&k);
        int ans=0;
        for(int i=0;i<=l-k;i++){
            if(s[i]=='-'){
                ans++;
                for(int j=0;j<k;j++){
                    if(s[i+j]=='-')s[i+j]='+';
                    else s[i+j]='-';
                }
            }
        }
        bool pos=true;
        for(int i=l-k+1;i<l;i++){
            if(s[i]=='-'){
                pos=false;
                break;
            }
        }
        printf("Case #%d: ",t);
        if(pos){
            printf("%d\n",ans);
        }
        else puts("IMPOSSIBLE");
    }
}
