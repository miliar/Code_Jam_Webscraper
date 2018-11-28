/* ***************************************
Author        :Scau.ion
Created Time  :2017/05/13 21:50:45 UTC+8
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
#define IN freopen("A-large.in", "r", stdin);
#define OUT freopen("A-large.out", "w", stdout);

int main()
{
    IN;
    OUT;
    IOS;
    int t;
    cin>>t;
    for (int i=1;i<=t;++i)
    {
        int n,p;
        cin>>n>>p;
        int a[4];
        memset(a,0,sizeof a);
        for (int j=1;j<=n;++j)
        {
            int x;
            cin>>x;
            ++a[x%p];
        }
        int ans=a[0];
        if (p==2)
        {
            ans+=a[1]/2;
            a[1]%=2;
            if (a[1]) ++ans;
        }
        else if (p==3)
        {
            int mi=min(a[1],a[2]);
            ans+=mi;
            a[1]-=mi;
            a[2]-=mi;
            ans+=a[1]/3;
            ans+=a[2]/3;
            a[1]%=3;
            a[2]%=3;
            if (a[1]||a[2]) ++ans;
        }
        else
        {
            int mi=min(a[1],a[3]);
            ans+=mi;
            a[1]-=mi;
            a[3]-=mi;
            a[2]+=a[1]/2;
            a[1]%=2;
            a[2]+=a[3]/2;
            a[3]%=2;
            ans+=a[2]/2;
            a[2]%=2;
            if (a[1]||a[2]||a[3]) ++ans;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
