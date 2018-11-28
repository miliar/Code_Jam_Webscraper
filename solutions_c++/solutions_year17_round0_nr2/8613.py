#include<string>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<unordered_map>
#include<string.h>
#include<queue>
#include<map>
using namespace std;
#define N 400005
#define INF 1100000000
map<string,int> mp;
void baoli(int s)
{
    int ans;
    int q[10];
    int len=0;
    int flag=1;
    for(int i=1;i<=s;i++){
            int t=i;
    len=0;
    flag=1;
    while(t)q[len++]=t%10,t/=10;
   // if(i==999)for(int j=0;j<len;j++)cout<<q[j]<<endl;
    for(int j=0;j<len-1;j++)
        if(q[j]<q[j+1])flag=0;
        if(flag)ans=i;
    }
    cout<<ans<<endl;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    int ca=0;
    scanf("%d",&t);
    while(t--)
    {
        string s;
        cin>>s;
       // baoli(k);
        int len=s.length();
        for(int i=len-1;i>=0;i--)
        {
            int j=i-1;
            if(s[j]>s[i])
            {
                s[j]--;
                while(j&&s[j]=='0'||s[j-1]>s[j])s[--j]--;
               // cout<<j<<endl;
                for(j+=1;j<len;j++)
                    s[j]='9';
                break;
            }
        }
        printf("Case #%d: ",++ca);
        int i=0;
        for(;i<len;i++)
            if(s[i]!='0')break;
        for(;i<len;i++)cout<<s[i];
        puts("");
    }

    return 0;
}


