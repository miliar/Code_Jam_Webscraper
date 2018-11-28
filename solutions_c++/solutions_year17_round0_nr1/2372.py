#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
char s[10005];
int len;
int cal(int l,int r){
    if(l>r)return 0;
    int left=l;
    while(left<=r){
        if(s[left]=='+')left++;
        else break;
    }
    if(left>r)return 0;
    if(r-left+1<len)return -1;
    for(int i=left;i<left+len;i++){
        if(s[i]=='-')s[i]='+';
        else s[i]='-';
    }
    int ans=cal(left,r);
    if(ans<0)return -1;
    return ans+1;
}
int main()
{
    freopen("E://project/code-jam/2017/Qualification/A-large.in","r",stdin);
    freopen("E://project/code-jam/2017/Qualification/a-large-out.txt","w",stdout);
    int n,k=0,ans,length;
    scanf("%d",&n);
    while(n--){
        scanf("%s%d",s,&len);
        length=strlen(s);
        ans=cal(0,length-1);
        if(ans<0)printf("Case #%d: IMPOSSIBLE\n",++k,ans);
        else printf("Case #%d: %d\n",++k,ans);
    }
    return 0;
}
