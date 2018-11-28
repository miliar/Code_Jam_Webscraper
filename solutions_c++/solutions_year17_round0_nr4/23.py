#include<cstdio>
#include<cstring>
using namespace std;

int TEST,t,n,k,i,j,a,b,sc,cha;
char in[110][110],out[110][110],ch[3],ho[110],ver[110],dirp[220],dirm[220];

int main(){
    scanf("%d",&TEST);
    for(t=1;t<=TEST;t++){
        scanf("%d %d",&n,&k);
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                in[i][j]=0;
                out[i][j]=0;
            }
        }
        for(i=0;i<110;i++){
            ho[i]=0;
            ver[i]=0;
        }
        for(i=0;i<220;i++){
            dirp[i]=0;
            dirm[i]=0;
        }
        sc=0;
        for(i=0;i<k;i++){
            scanf("%s %d %d",ch,&a,&b);
            if(ch[0]=='+'){
                in[a][b]=2;
                out[a][b]=2;
                dirp[a+b]=1;
                dirm[a-b+100]=1;
                sc++;
            }
            if(ch[0]=='x'){
                in[a][b]=1;
                out[a][b]=1;
                ho[a]=1;
                ver[b]=1;
                sc++;
            }
            if(ch[0]=='o'){
                in[a][b]=3;
                out[a][b]=3;
                dirp[a+b]=1;
                dirm[a-b+100]=1;
                ho[a]=1;
                ver[b]=1;
                sc+=2;
            }
        }
        for(i=1;i<=n;i++){
            if(ho[i]==0){
                for(j=1;j<=n;j++){
                    if(ver[j]==0){
                        out[i][j]++;
                        ho[i]=1;
                        ver[j]=1;
                        sc++;
                        break;
                    }
                }
            }
        }
        for(i=n-1;i>=0;i--){
            if(dirm[100+i]==0){
                for(j=i+2;j<=2*n-i;j+=2){
                    if(dirp[j]==0){
                        dirm[100+i]=1;
                        dirp[j]=1;
                        out[(i+j)/2][(j-i)/2]+=2;
                        sc++;
                        break;
                    }
                }
            }
            if(i==0)break;
            if(dirm[100-i]==0){
                for(j=i+2;j<=2*n-i;j+=2){
                    if(dirp[j]==0){
                        dirm[100-i]=1;
                        dirp[j]=1;
                        out[(j-i)/2][(j+i)/2]+=2;
                        sc++;
                        break;
                    }
                }
            }

        }
        cha=0;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(in[i][j]!=out[i][j])cha++;
            }
        }
        printf("Case #%d: %d %d\n",t,sc,cha);
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(in[i][j]!=out[i][j]){
                    if(out[i][j]==1)printf("x %d %d\n",i,j);
                    if(out[i][j]==2)printf("+ %d %d\n",i,j);
                    if(out[i][j]==3)printf("o %d %d\n",i,j);
                }
            }
        }
    }
    return 0;
}
