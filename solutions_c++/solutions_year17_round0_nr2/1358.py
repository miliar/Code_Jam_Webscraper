#include<cstdio>
#include<cstring>
int main(){
    freopen("input.in","r+",stdin);
    freopen("output.out","w+",stdout);
    int t,len;
    char s[20];
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        memset(s,0,sizeof(s));
        scanf("%s",s);
        len=(int)strlen(s);
        for(int j=0;j<len-1;j++){
            if(s[j]>s[j+1]){
                s[j]--;
                for(int k=j+1;k<len;k++){
                    s[k]='9';
                }
                j=-1;
            }
        }
        for(int j=0;j<len;j++){
            if(s[j]!='0'){
                printf("Case #%d: %s\n",i,s+j);
                break;
            }
        }
    }
}
