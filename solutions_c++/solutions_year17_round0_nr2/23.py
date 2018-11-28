#include<cstdio>
#include<cstring>
using namespace std;

int TEST,t,len,i,j,a,b,c;
char st[30];

int main(){
    scanf("%d",&TEST);
    for(t=1;t<=TEST;t++){
        scanf("%s",st);
        len=strlen(st);
        for(i=1;i<len;i++){
            if(st[i-1]>st[i]){
                c=st[i-1];
                for(j=i-1;j>=0;j--){
                    if(st[j]!=c)break;
                    st[j]--;
                }
                j+=2;
                for(;j<len;j++)st[j]='9';
                break;
            }
        }
        printf("Case #%d: ",t);
        i=0;
        while(i<len){
            if(st[i]=='0')i++;
            else break;
        }
        for(;i<len;i++){
            printf("%c",st[i]);
        }
        printf("\n");
    }
    return 0;
}
