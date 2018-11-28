#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdio>
char S[1005];
bool d[1005];
int K;
int N;
void solve(){
    scanf("%s%d",S, &K);
    N = strlen(S);
    for (int i=0;i<N;++i){
        d[i]=(S[i]=='+');
    }
    int ans=0;
    for (int i=0;i+K<=N;++i){
        if (!d[i]){
            ans+=1;
            for (int j=0;j<K;++j){
                d[i+j]=!d[i+j];
            }
        }
    }
    bool possible = true;
    for (int i=0;i<N;++i){
        possible &= d[i];
    }
    if (!possible){
        puts("IMPOSSIBLE");
    }else{
        printf("%d\n",ans);
    }
}
int main(){
    int N;
    scanf("%d",&N);
    for (int i=1;i<=N;++i){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
