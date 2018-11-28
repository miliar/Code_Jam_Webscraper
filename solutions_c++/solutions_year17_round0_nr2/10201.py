#include<bits/stdc++.h>
using namespace std;
int T;
int N;
bool check(int s)
{
    int temp[10];
    int top=0;
    while(s)
    {
        temp[++top]=s%10;
        s/=10;
    }
    for(int i=top;i>1;i--)
    {
        if(temp[i]>temp[i-1])return false;
    }
    return 1;
}
int main()
{
    freopen("2.out","w",stdout);
    int Case=0;
    cin>>T;
    while(T--)
    {
        scanf("%d",&N);
        int ans=0;
        for(int i=1;i<=N;i++)
        {
            if(check(i))
                ans=i;
        }
        printf("Case #%d: %d\n",++Case,ans);
    }
    return 0;
}
