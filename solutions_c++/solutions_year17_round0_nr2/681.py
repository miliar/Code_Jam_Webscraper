#include <stdio.h>
#include <string.h>
char s[1000];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        scanf("%s",s);
        int l=strlen(s);
        for(int i=0;i+1<l;i++){
            if(s[i]>s[i+1]){
                int j;
                for(j=i;j>=0;j--){
                    if(s[j]!=s[j-1]){
                        break;
                    }
                }
                s[j]--;
                for(j++;j<l;j++){
                    s[j]='9';
                }
                break;
            }
        }
        printf("Case #%d: ",t);
        for(int i=0;i<l;i++){
            if(i==0&&s[i]=='0'){
                continue;
            }
            printf("%c",s[i]);
        }
        printf("\n");
    }
}
