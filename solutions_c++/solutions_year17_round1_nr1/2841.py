#include<cstdio>
#include<cstdlib>
#include<string>
#include<string.h>
#include<algorithm>
#define s 27
using namespace std;
char m[s][s];
int bl;
int l[26],r[26],u[26],d[26];
void expand(int k){
    bool halt=false;
    while(!halt){
        halt=true;
        bool cl=true;
        for(int i=u[k];i<d[k];i++){
            if(m[i][l[k]-1]!='?'){
                cl=false;
                break;
            }
        }
        if(cl){
            halt=false;
            l[k]--;
            for(int i=u[k];i<d[k];i++){
                bl--;
                m[i][l[k]]='A'+k;
            }
        }
        bool cr=true;
        for(int i=u[k];i<d[k];i++){
            if(m[i][r[k]]!='?'){
                cr=false;
                break;
            }
        }
        if(cr){
            halt=false;
            r[k]++;
            for(int i=u[k];i<d[k];i++){
                bl--;
                m[i][r[k]-1]='A'+k;
            }
        }
        bool cu=true;
        for(int j=l[k];j<r[k];j++){
            if(m[u[k]-1][j]!='?'){
                cu=false;
                break;
            }
        }
        if(cu){
            halt=false;
            u[k]--;
            for(int j=l[k];j<r[k];j++){
                bl--;
                m[u[k]][j]='A'+k;
            }
        }
        bool cd=true;
        for(int j=l[k];j<r[k];j++){
            if(m[d[k]][j]!='?'){
                cd=false;
                break;
            }
        }
        if(cd){
            halt=false;
            d[k]++;
            for(int j=l[k];j<r[k];j++){
                bl--;
                m[d[k]-1][j]='A'+k;
            }
        }
    }
}
int main(){
    freopen("inputA","r",stdin);
    freopen("outputA.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        for(int i=0;i<s;i++)for(int j=0;j<s;j++)m[i][j]=' ';
        int R,C;
        scanf("%d%d",&R,&C);
        for(int i=0;i<R;i++)for(int j=0;j<C;j++){
            m[i+1][j+1]='\n';
            while(m[i+1][j+1]=='\n')
                scanf("%c",&m[i+1][j+1]);
        }
        bool ex[26]={false};
        bl=R*C;
        for(int k=0;k<26;k++){
            l[k]=s;r[k]=0;u[k]=s;d[k]=0;
            for(int i=1;i<=R;i++)for(int j=1;j<=C;j++){
                if(m[i][j]=='A'+k){
                    ex[k]=true;
                    l[k]=min(l[k],j);
                    r[k]=max(r[k],j+1);
                    u[k]=min(u[k],i);
                    d[k]=max(d[k],i+1);
                }
            }
            for(int i=u[k];i<d[k];i++)for(int j=l[k];j<r[k];j++){
                m[i][j]='A'+k;
                bl--;
            }
        }
        while(bl){
            for(int k=0;k<26;k++){
                if(ex[k])expand(k);
            }
        }
        printf("Case #%d:\n",t);
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++)printf("%c",m[i][j]);
            puts("");
        }
    }
}
