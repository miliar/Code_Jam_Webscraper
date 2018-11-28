#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<ctime>
#include<vector>
#include<queue>
using namespace std;

int T,R,C;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-output.txt","w",stdout);
    scanf("%d",&T);
    for(int z=1;z<=T;z++){
        scanf("%d %d",&R,&C);
        char a[30][30];
        for(int i=0;i<R;i++){
            scanf("%s",a[i]);
        }
        for(int i=0;i<R;i++){
            char temp=0;
            bool flag=false;
            for(int j=0;j<C;j++){
                if(a[i][j]!='?'){
                    flag=true;
                    temp = a[i][j];
                }
                else{
                    if(flag)
                        a[i][j] = temp;
                }
            }
            flag=false;
            for(int j=C-1;j>=0;j--){
                if(a[i][j]!='?'){
                    flag=true;
                    temp=a[i][j];
                }
                else{
                    if(flag)
                        a[i][j]=temp;
                }
            }
        }
        for(int j=0;j<C;j++){
            char temp=0;
            bool flag=false;
            for(int i=0;i<R;i++){
                if(a[i][j]!='?'){
                    flag=true;
                    temp = a[i][j];
                }
                else{
                    if(flag)
                        a[i][j] = temp;
                }
            }
            flag=false;
            for(int i=R-1;i>=0;i--){
                if(a[i][j]!='?'){
                    flag=true;
                    temp=a[i][j];
                }
                else{
                    if(flag)
                        a[i][j]=temp;
                }
            }
        }
        printf("Case #%d: \n",z);
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                printf("%c",a[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
