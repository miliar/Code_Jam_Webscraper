#include <bits/stdc++.h>

using namespace std;
#define mod  1000000007
typedef long long ll;
#define N 1234567

int b[N];
vector<int> vec[N];


int judge(int x)
{
    int b[20]={0};
    int t = 0;
    while (x)
    {
        b[++t]=x%10;
        x/=10;
    }
    for (int i=2;i<=t;i++)
    if (b[i]>b[i-1]) return 0;

    return 1;
}

int main()
{
    int T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int _=1;_<=T;_++)
    {
        ll x;
        cin>>x;
        int ans  = 0;
        for (int i=1;i<=x;i++)
        {
            if (judge(i))
            {
                ans = i;
            }
        }

        printf("Case #%d: %d\n",_,ans);
    }
    return 0;
}
