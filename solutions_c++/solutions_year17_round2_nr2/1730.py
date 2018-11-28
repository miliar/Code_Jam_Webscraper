#include <iostream>
#include <cstdio>
#define N 1005
using namespace std;
typedef long long ll;
int T,n,c[3],cc[3],k;
char hc[3]={'R','Y','B'},hcc[3]={'O','G','V'};
char s[N];
char ooxx(int x){
    c[x]--;
    return hc[x];
}
int main(void){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        scanf("%d%d%d%d%d%d%d",&n,&c[0],&cc[0],&c[1],&cc[1],&c[2],&cc[2]);
        int minn=-1;
        for(int i=0;i<3;++i)if(c[i]){
            if(minn=-1)minn=i;
            else{
                if(c[i]<c[minn]||(c[i]==c[minn]&&hc[i]<hc[minn]))
                    minn=i;
            }
        }
        s[0]=ooxx(minn);
        for(k=1;k<n;++k){
            if(s[k-1]=='R'){
                if(max(c[1],c[2])==0)break;
                if(c[1]>c[2]||(c[1]==c[2]&&hc[1]<hc[2]))s[k]=ooxx(1);
                else s[k]=ooxx(2);
            }else if(s[k-1]=='Y'){
                if(max(c[0],c[2])==0)break;
                if(c[0]>c[2]||(c[0]==c[2]&&hc[0]<hc[2]))s[k]=ooxx(0);
                else s[k]=ooxx(2);
            }else if(s[k-1]=='B'){
                if(max(c[0],c[1])==0)break;
                if(c[0]>c[1]||(c[0]==c[1]&&hc[0]<hc[1]))s[k]=ooxx(0);
                else s[k]=ooxx(1);
            }
        }
        if(k==n&&s[0]!=s[k-1]){
            s[k]='\0';
            printf("Case #%d: %s\n",t,s);
        }else printf("Case #%d: IMPOSSIBLE\n",t);
    }
}
