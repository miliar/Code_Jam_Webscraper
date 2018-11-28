#include<iostream>
#include<iomanip>
#include<algorithm>
#include<queue>
#include<set>
#include<cstdio>
#include<map>
#include<limits>
#include<cstring>
using namespace std;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    for(int I=1;I<=T;++I){
        static char s[1010];
        int k,l;
        scanf("%s%d",s+1,&k);
        l=strlen(s+1);
        int ans=0;
        for(int i=1;i+k-1<=l;++i){
            if(s[i]=='-'){
                ++ans;
                for(int j=1;j<=k;++j){
                    if(s[i+j-1]=='+')
                        s[i+j-1]='-';
                    else
                        s[i+j-1]='+';
                }
            }
        }
        for(int i=1;i<=l;++i)
           if(s[i]=='-')
               ans=~0u>>1;
        if(ans==~0u>>1){
            printf("Case #%d: IMPOSSIBLE\n",I);
        }else{
            printf("Case #%d: %d\n",I,ans);
        }
    }
    return 0;
}
