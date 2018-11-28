#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
int s[100],len;
char str[1000];
int main()
{
    freopen("E://project/code-jam/2017/Qualification/B-large.in","r",stdin);
    freopen("E://project/code-jam/2017/Qualification/B-large-out.txt","w",stdout);
    int t,k=0;
    cin>>t;
    while(t--){
        scanf("%s",str);
        len=strlen(str);
        for(int i=0;i<len;i++)s[i]=str[i]-'0';
        if(len==1){
            printf("Case #%d: %d\n",++k,s[0]);
            continue;
        }
        int l=1;
        while(l<len){
            if(s[l]<s[l-1])break;
            l++;
        }
        if(l<len){
            int left=l-1;
            while(left>0&&s[left]==s[left-1])left--;
            s[left]--;
            for(int i=left+1;i<len;i++)s[i]=9;
        }
        int i=0;
        if(s[0]==0)i=1;
        printf("Case #%d: ",++k);
        for(;i<len;i++)printf("%d",s[i]);
        printf("\n");
    }
    return 0;
}
