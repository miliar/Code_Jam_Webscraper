#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<vector>
#include<stack>
#include<string>
using namespace std;
char str[2000];
int main()
{
    freopen("D:A2.in","r",stdin);

    freopen("D:A1.out","w",stdout);
    int T,k;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        scanf("%s",str);
        scanf("%d",&k);
        int len=strlen(str);
        int ans=0;
        for(int i=0;i<=len-k;i++)
        {
            if(str[i]=='-')
            {
                for(int j=i;j<i+k;j++)
                {
                    if(str[j]=='-')
                        str[j]='+';
                    else str[j]='-';
                }
                ans++;
            }
        }
        int flag=0;
        for(int i=0;i<len;i++)
        {
            if(str[i]!='+')
            {
                flag=1;
            }

        }
        printf("Case #%d: ",ca);
        if(flag==1)
            cout<<"IMPOSSIBLE"<<endl;
        else
        cout<<ans<<endl;
    }
}
