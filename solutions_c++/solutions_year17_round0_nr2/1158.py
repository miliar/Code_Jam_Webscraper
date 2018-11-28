#include<bits/stdc++.h>
using namespace std;
long long int n;
long long solve(long long a)
{
    vector<int> dig;
    while(a>0)
    {
        dig.push_back(a%10);
        a=a/10;
    }
    reverse(dig.begin(),dig.end());
    int l=dig.size();
    for(int r=l-1;r>=1;r--)
    {
        if(dig[r]<dig[r-1])
        {
            int tem_r=r-1;
            while(dig[tem_r]==0)
            {
                dig[tem_r]=9;
                tem_r--;
            }
            dig[tem_r]--;
            for(int ou=r;ou<l;ou++)
            {
                dig[ou]=9;
            }
        }
    }
    long long ans=0;
    for(int ret=0;ret<l;ret++)
    {
        ans=ans*10+dig[ret];
    }
    return ans;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outmain.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int q=1;q<=t;q++)
    {
        scanf("%lld",&n);
        printf("Case #%d: %lld\n",q,solve(n));
    }
}
