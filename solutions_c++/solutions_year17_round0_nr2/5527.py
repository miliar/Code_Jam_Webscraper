#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
int arr[18];
ull solve()
{
    memset(arr,0,sizeof(arr));
    ull n,ans=0;
    scanf("%llu",&n);
    int c=0;int i,j=0,k;
    ull temp=n;
    while(temp!=0)
    {
        arr[c++]=temp%10;
        temp/=10;
    }
    for(i=0;i<c-1;i++)
    {
        if(arr[i]>=arr[i+1])
            continue;
        else
        {
            for(k=j;k<=i;k++)
                arr[k]=9;
            arr[i+1]-=1;
            j=i+1;
        }
    }
    for(i=c-1;i>=0;i--)
    {
        ans*=10;
        ans+=arr[i];
    }
    return ans;
}
int main()
{
    freopen("a1.in","r",stdin);
    freopen("a1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: %llu\n",i,solve());
    }
    return 0;
}
