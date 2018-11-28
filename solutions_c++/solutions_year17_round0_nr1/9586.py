#include<bits/stdc++.h>

#define   db(x)         printf("**%d\n",x)
#define   loop(i,x,n)   for(int i=x;i<n;i++)
#define   pb            push_back
#define   pii           pair<int,int>
#define   imax          2147483647
#define   pcase(x)      printf("Case %d: ",x)
#define   md            1000000007
#define   mm(x,y)       memset(x,y,sizeof(x))
#define   pf1(x)        printf("%d\n",x)
#define   pf2(x,y)      printf("%d %d\n",x,y)
#define   sf1(x)        scanf("%d",&x)
#define   sf2(x,y)      scanf("%d %d",&x,&y)

using namespace std;

int main()
{
//    freopen("input.in","r",stdin);
//    freopen("output.out","w",stdout);
    int tc,p=1;
    scanf("%d",&tc);
    while(tc--)
    {
        getchar();
        string s,t;
        int k,cnt1=0,ans=1,cnt2=0,i,j;
        cin>>s>>k;
        t=s;
        int len=s.length();
        for(i=0;i<len-k+1;i++)
        {
            if(s[i]!='+')
            {
                cnt1++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='+') s[j]='-';
                    else s[j]='+';
                }
            }
        }
        for(;i<len;i++) if(s[i]=='-') ans=0;
        for(i=len-1;i>=k-1;i--)
        {
            if(t[i]!='+')
            {
                cnt2++;
                for(j=i;j>i-k;j--)
                {
                    if(t[j]=='+') t[j]='-';
                    else t[j]='+';
                }
            }
        }
        for(;i>=0;i--) if(t[i]=='-')ans=0;
        printf("Case #%d: ",p++);
        if(ans==0) printf("IMPOSSIBLE\n");
        else printf("%d\n",min(cnt1,cnt2));
    }
    return 0;
}
/*sample

*/

