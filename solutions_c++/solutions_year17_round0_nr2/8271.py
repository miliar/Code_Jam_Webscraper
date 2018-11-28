#include<bits/stdc++.h>
using namespace std;
const int N=20;
char s[N];
long long ans;

bool dfs(int pos,int len,int limit,int Max){
    if(pos==len)
        return true;
    if(!limit){
        ans=ans*10+9;
        dfs(pos+1,len,limit,9);
        return true;
    }
    if(s[pos]-'0'<Max)
        return false;
    for(int i=s[pos]-'0';i>=Max;i--){
        ans=ans*10+i;
        bool Flag=dfs(pos+1,len,limit&&(i==(s[pos]-'0')),i);
        if(Flag==false)
            ans=ans/10;
        else
            return true;
    }
    return false;
}

int main(){
    int _;
    freopen("B-large.in","r",stdin);
    freopen("1000.out","w",stdout);
    scanf("%d",&_);
    for(int Case=1;Case<=_;Case++){
        scanf("%s",s);
        int len=strlen(s);
        ans=0;
        dfs(0,len,1,0);
        printf("Case #%d: %lld\n",Case,ans);
    }
    return 0;
}
