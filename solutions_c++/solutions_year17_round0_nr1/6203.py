#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#define MAXN 1002
using namespace std;
int T,K;
char S[MAXN];
int solve(){
    int ans=0;
    int len = strlen(S);
    for(int i=0;i<len-K+1;++i){
        if(S[i]=='-'){
            for(int j=i;j<i+K;++j){
                if(S[j]=='-') S[j]='+';
                else if(S[j]=='+') S[j]='-';
            }
            ans++;
        }
    }
    for(int i=len-1;i>=len-K;--i){
        if(S[i]=='-')
            return -1;
    }
    return ans;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(int c=1;c<=T;++c){
        scanf("%s%d",&S,&K);
        int ans = solve();
        printf("Case #%d: ",c);
        if(ans==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
