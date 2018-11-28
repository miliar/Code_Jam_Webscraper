#include <stdio.h>
#include <string.h>
char s[50][50],s2[50][50];
int a[50],a2[50];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        for(int i=0;i<50;i++){
            memset(s[i],'\0',49);
            memset(s2[i],'\0',49);
            a[i]=0;
        }
        int x,y,z;
        scanf("%d ",&x);
        scanf("%d",&y);
        for(int i=0;i<x;i++){
            scanf("%s",s[i]);
        }
        z=-1;
        bool bb=true;
        for(int i=0;i<x;i++){
            bool b=true;
            for(int j=0;j<y;j++){
                if(s[i][j]!='?'){
                    b=false;
                }
            }
            if(b==false){
                a[i]=-1;
                if(bb==true){
                    z=i;
                    bb=false;
                }
            }
        }
//        for(int i=0;i<x;i++)printf("%d ",a[i]);
//        printf("\n");
        for(int i=0;i<x;i++){
            if(i<z) a2[i]=z;
            else{
                if(a[i]==-1){
                    a2[i]=i;
                    z=i;
                }
                else{
                    a2[i]=z;
                }
            }
        }
//        for(int i=0;i<x;i++)printf("%d ",a2[i]);
        for(int i=0;i<x;i++){
            if(a[i]==0) continue;
            char c;
            for(int j=0;j<y;j++){
                if(s[i][j]!='?'){
                    c=s[i][j];
                    break;
                }
            }
            for(int j=0;j<y;j++){
                if(s[i][j]!='?'){
                    s2[i][j]=s[i][j];
                    c=s[i][j];
                }
                else{
                    s2[i][j]=c;
                }
//                printf("%c %c",s[i][j],s2[i][j]);
            }
        }
        printf("Case #%d:\n",t);
        for(int i=0;i<x;i++){
            printf("%s\n",s2[a2[i]]);
        }
    }
}
