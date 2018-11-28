#include<cstdio>
#include<cstring>

int main(){
    int T,n;
    char N[30];
    bool sorted;

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%s",N);
        n=strlen(N);

        for(int i=n-1;i>0;i--){
            sorted=1;
            for(int j=0;j<n-1;j++){
                if(N[j]>N[j+1]){
                    sorted=0;
                    break;
                }
            }
            if(sorted==1) break;

            if(N[i]!='9'){
                N[i]='9';
                int ii=i-1;
                while(N[ii]=='0'){
                    N[ii]='9';
                    ii--;
                }
                N[ii]--;
            }
        }
        printf("Case #%d: ",t);
        if(N[0]!='0') printf("%c",N[0]);
        for(int i=1;i<n;i++) printf("%c",N[i]);
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
