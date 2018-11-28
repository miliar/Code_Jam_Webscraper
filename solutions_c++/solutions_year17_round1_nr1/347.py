#include<bits/stdc++.h>
using namespace std;
char s[30][30];
int main(void){
    freopen("1233.in","r",stdin);
    freopen("out.out","w",stdout);
    int i,j,k,n,m,A,B,ca=1,T;
    scanf("%d",&T);
    while(T--){
        scanf("%d %d",&A,&B);
        for(i=0;i<A;i++){
            scanf("%s",s[i]);
        }
        for(i=0;i<A;i++){
            for(j=0;j<B;j++){
                if(s[i][j]!='?'){
                    for(k=0;k<j;k++){
                        if(s[i][k]=='?') s[i][k]=s[i][j];
                    }
                    for(k=j+1;k<B;k++){
                        if(s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                    }
                }
            }
        }
        for(i=0;i<A;i++){
            for(j=0;j<B;j++){
                if(s[i][j]!='?'){
                    for(k=0;k<i;k++){
                        if(s[k][j]=='?') s[k][j]=s[i][j];
                    }
                    for(k=i+1;k<A;k++){
                        if(s[k][j]=='?') s[k][j]=s[i][j];
                        else break;
                    }
                }
            }
        }
        printf("Case #%d:\n",ca++);
        for(i=0;i<A;i++) printf("%s\n",s[i]);
    }
}
