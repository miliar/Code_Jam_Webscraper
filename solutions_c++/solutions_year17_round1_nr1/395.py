#include<bits/stdc++.h>

typedef long long lnt;
char a[30][30],ans[30][30];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("QAQ.txt","w",stdout);
    int T,t=0;
    scanf("%d",&T);
    while(T--){
        t++;
        int n,m,k,i,j,g;
        scanf("%d%d",&n,&m);
        for(k=0;k<n;k++) scanf("%s",a[k]);
        int now=-1,last,find=-1;
        for(k=n-1;k>=0;k--){
            for(i=0;i<m;i++){
                if(a[k][i]!='?'){
                    find=k;
                    break;
                }
            }
            if(find!=-1) break;
        }
        for(k=0;k<n;k++){
            int qq=-1,up=k;
            if(k==find) up=n-1;
            bool ok=false;
            for(i=0;i<m;i++){
                if(a[k][i]!='?') ok=true;
                else continue;
                for(j=now+1;j<=up;j++){
                    for(g=qq+1;g<=i;g++){
                        ans[j][g]=a[k][i];
                    }
                }
                last=i;
                qq=i;
            }
            if(!ok) continue;
            if(qq!=m-1){
                for(j=now+1;j<=up;j++){
                    for(g=qq+1;g<m;g++){
                        ans[j][g]=a[k][last];
                    }
                }
            }
            now=k;
        }
        
        printf("Case #%d:\n",t);
        for(k=0;k<n;k++){
            for(i=0;i<m;i++){
                printf("%c",ans[k][i]);
            }
            puts("");
        }
    }
}
