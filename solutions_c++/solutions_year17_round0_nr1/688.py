#include <stdio.h>
#include <string.h>
char s[5005];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++){
        scanf("%s",s);
        int k,cnt=0;
        scanf("%d",&k);
        int l=strlen(s);
        for(int i=0;i+k<=l;i++){
            if(s[i]=='-'){
                cnt++;
                for(int j=0;j<k;j++){
                    if(s[i+j]=='-'){
                        s[i+j]='+';
                    }
                    else{
                        s[i+j]='-';
                    }
                }
            }
        }
        bool b=true;
        for(int i=l-k;i<l;i++){
            if(s[i]=='-'){
                b=false;
            }
        }
        printf("Case #%d: ",tc);
        if(!b){
            printf("Impossible\n");
        }
        else{
            printf("%d\n",cnt);
        }
    }
}
