#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;

LL a;
int T;
int num[25];
int vis[25];

int main(){
    //freopen("in.txt","w",stdout);
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        cin>>a;
        int a1=a;
        int cnt=0;
        while(a){
            num[++cnt]=a%10;
            a/=10;
        }
        reverse(num+1,num+cnt+1);
        //for(int i=1;i<=cnt;i++)cout<<num[i]<<endl;
        memset(vis,0,sizeof(vis));
        while(1){
        int ok=1;
        for(int i=2;i<=cnt;i++){
            if(vis[i]==1&&num[i]==9){
                break;
            }
            if(num[i]<num[i-1]){
                ok=0;
                num[i-1]=(num[i-1]-1+10)%10;
                num[i]=9;
                vis[i]=1;
                break;
            }
        }
        //for(int i=1;i<=cnt;i++)cout<<num[i];
        //cout<<endl;
        if(ok==1)break;
        }
        int ok=0;
        printf("Case #%d: ",kase);
        for(int i=1;i<=cnt;i++){
            if(num[i]==0&&ok==0)continue ;
            ok=1;
            printf("%d",num[i]);
            if(num[i]==9){
                for(int j=i+1;j<=cnt;j++){
                    printf("9");
                }
                break;
            }
        }
        cout<<endl;
    }
    return 0;
}
