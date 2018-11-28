#include <cstdio>
#include <cstring>
#include <iostream>
#define N 1005
using namespace std;
int T,len;
char s[20],ans[20];
bool dfs(int p,int pre){
    if(p==len)return 1;
    int k=s[p]-'0';
    if(p)k=ans[p-1]==s[p-1]?k:9;
    for(int i=k;i>=pre;--i){
        ans[p]=i+'0';
        if(dfs(p+1,i))return 1;
    }
    return 0;
}
int main(void){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        scanf("%s",s);
        len=strlen(s);
        dfs(0,0);
        printf("Case #%d: ",t);
        int p=0;
        while(ans[p]=='0'&&p<len)p++;
        if(p==len)printf("0\n");
        else{
            for(int i=p;i<len;++i)printf("%c",ans[i]);
            printf("\n");
        }
    }
}
