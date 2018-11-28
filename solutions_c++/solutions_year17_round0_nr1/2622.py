#include <bits/stdc++.h>

using namespace std;

#define MP make_pair
#define PB push_back
typedef long long LL;
typedef pair<int,int> PII;
const double eps=1e-8;
const double pi=acos(-1.0);
const int K=1e6+7;
const int mod=1e9+7;


char ss[100000];

int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,n,cnt=1,len;cin>>t;
    while(t--)
    {
        int ans=0;
        scanf("%s%d",ss+1,&n);
        len=strlen(ss+1);
        for(int i=1;i<=len;i++)
        if(ss[i]=='-')
        {
            if(len-i+1<n)
            {
                ans=-1;break;
            }
            int j=0;
            while(j<n)
            {
                if(ss[i+j]=='-')ss[i+j]='+';
                else    ss[i+j]='-';
                j++;
            }
            ans++;
        }
        if(ans!=-1)
            printf("Case #%d: %d\n",cnt++,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",cnt++);
    }
    return 0;
}
