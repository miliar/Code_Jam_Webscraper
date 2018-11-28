#include<cstdio>
#include<cstring>
int main(){
    int T,K;
    char S[1005];
    int i,n,cnt;

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%s",S); n=strlen(S);
        scanf("%d",&K);
        i=0; cnt=0;
        while(i<n-K+1){
            if(S[i]=='-'){
                for(int j=0;j<K;j++){
                    if(S[i+j]=='-') S[i+j]='+';
                    else S[i+j]='-';
                }
                cnt++;
            }
            i++;
        }
        for(;i<n;i++){
            if(S[i]=='-'){
                cnt=-1;
                break;
            }
        }

        if(cnt==-1) printf("Case #%d: IMPOSSIBLE\n",t);
        else printf("Case #%d: %d\n",t,cnt);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
