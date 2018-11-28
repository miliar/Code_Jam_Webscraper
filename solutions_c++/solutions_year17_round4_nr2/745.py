/* ***************************************
Author        :Scau.ion
Created Time  :2017/05/13 22:52:54 UTC+8
File Name     :ion.cpp
*************************************** */

#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define ULL unsigned long long
#define PB push_back
#define MP make_pair
#define PII pair<int,int>
#define VI vector<int>
#define VPII vector<PII>
#define X first
#define Y second
#define IOS ios::sync_with_stdio(0);cin.tie(0);
#define IN freopen("B-small-attempt0.in", "r", stdin);
#define OUT freopen("B-small-attempt0.out", "w", stdout);

const int maxn=1010;

int sum[2][maxn];

int main()
{
    IN;
    OUT;
    IOS;
    int t;
    cin>>t;
    for (int i=1;i<=t;++i)
    {
        int n,c,m;
        cin>>n>>c>>m;
        int s[2]={0,0};
        memset(sum,0,sizeof sum);
        for (int j=1;j<=m;++j)
        {
            int p,b;
            cin>>p>>b;
            ++sum[b-1][p];
            ++s[b-1];
        }
        int ans=max(s[0],s[1]);
        int ans2=0;
        bool ty;
        if (s[0]<s[1]) ty=0;
        else ty=1;
        for (int j=1;j<=n;++j)
        {
            if (sum[ty][j]>s[!ty]-sum[!ty][j])
            {
                if (j==1) ans+=sum[ty][j]-(s[!ty]-sum[!ty][j]);
                else ans2+=sum[ty][j]-(s[!ty]-sum[!ty][j]);
            }
        }
        cout<<"Case #"<<i<<": "<<ans<<" "<<ans2<<endl;
    }
    return 0;
}
