#include<cstdio>

using namespace std;

int i,j,k,l,t,test,r,c,f,fc,tc;
char st[27][27];

int main(){
    scanf("%d",&test);
    for(t=1;t<=test;t++){
        scanf("%d %d",&r,&c);
        for(i=0;i<r;i++)scanf("%s",st[i]);
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(st[i][j]!='?'){
                    f=i;
                    while(f!=0&&st[f-1][j]=='?')f--;
                    for(k=f;k<=i;k++)st[k][j]=st[i][j];
                    fc=j;
                    tc=j;
                    while(fc!=0){
                        fc--;
                        for(k=f;k<=i;k++){
                            if(st[k][fc]!='?')break;
                        }
                        if(k!=i+1){
                            break;
                        }
                        for(k=f;k<=i;k++)st[k][fc]=st[i][j];
                    }
                    while(tc!=c-1){
                        tc++;
                        for(k=f;k<=i;k++){
                            if(st[k][tc]!='?')break;
                        }
                        if(k!=i+1){
                            break;
                        }
                        for(k=f;k<=i;k++)st[k][tc]=st[i][j];
                    }
                }
            }
        }
        for(j=0;j<c;j++){
            k=r-1;
            while(st[k][j]=='?')k--;
            for(l=k+1;l<r;l++)st[l][j]=st[k][j];
        }
        printf("Case #%d:\n",t);
        for(i=0;i<r;i++)printf("%s\n",st[i]);
    }
}
