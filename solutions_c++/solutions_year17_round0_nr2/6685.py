#include<cstdio>
#include<cstdlib>
#include<string>
#include<string.h>
#include<algorithm>
using namespace std;
#define maxl 20
int main(){
    freopen("inputB","r",stdin);
    freopen("outputB.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        char s[maxl];
        for(int i=0;i<maxl;i++)s[i]='0';
        long long int n;
        scanf("%lld",&n);
        for(int i=maxl-1;i>=0;i--){
            s[i]='0'+(n%10);
            n/=10;
        }
        int r=maxl;
        for(int i=maxl-2;i>=0;i--)
            if(s[i]-s[i+1]>0)r=i;
        if(r<maxl){
            int l;
            for(int i=r;i>=0;i--){
                if(s[i]==s[r])l=i;
                else break;
            }
            s[l]=s[l]-1;
            for(int i=l+1;i<maxl;i++)s[i]='9';
        }
        bool p=false;
        printf("Case #%d: ",t);
        for(int i=0;i<maxl;i++){
            if(s[i]!='0'||i==maxl-1)p=true;
            if(p)printf("%c",s[i]);
        }
        puts("");
    }
}
