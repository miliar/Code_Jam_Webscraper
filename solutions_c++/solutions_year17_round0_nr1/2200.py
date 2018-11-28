#include<bits/stdc++.h>
using namespace std;

char s[1003];
int n,t,res,T,cs;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.ou","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%s%d",s,&t);
        n=strlen(s);
        res=0;
        for(int i=0; i+t-1<n; ++i)if(s[i]=='-'){
            ++res;
            for(int j=i; j<i+t; ++j)if(s[j]=='-')s[j]='+';else s[j]='-';
        }
        bool ok=1;
        for(int i=0; i<n; ++i)if(s[i]=='-'){ok=0;break;}
        printf("Case #%d: ",++cs);
        if(ok)printf("%d\n",res);
        else puts("IMPOSSIBLE");
    }
}
