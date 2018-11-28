#include<cstdio>
#include<cstring>
using namespace std;

int TEST,t,len,i,j,a,b,c;
char st[1010];

int main(){
    scanf("%d",&TEST);
    for(t=1;t<=TEST;t++){
        scanf("%s",st);
        len=strlen(st);
        scanf("%d",&b);
        c=0;
        for(i=0;i<len;i++){
            if(i+b<=len){
                if(st[i]=='-'){
                    c++;
                    for(j=0;j<b;j++){
                        if(st[i+j]=='-')st[i+j]='+';
                        else st[i+j]='-';
                    }
                }
            }
            else if(st[i]=='-'){
                printf("Case #%d: IMPOSSIBLE\n",t);
                break;
            }
        }
        if(i==len)printf("Case #%d: %d\n",t,c);
    }
    return 0;
}
