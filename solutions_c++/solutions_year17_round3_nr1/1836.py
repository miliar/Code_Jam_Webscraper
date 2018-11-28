#include<iostream>
#include<fstream>
#include<iomanip>
#include<algorithm>
#include<math.h>
#include<vector>
#include<stack>
#include<map>
#define int long long
using namespace std;
struct code
{
    int64_t r,h,s;
};
bool comp(code a , code b)
{
    return a.s>b.s or (a.s==b.s and a.r<b.r) or (a.s==b.s and  a.r==b.r and a.h<b.h);
}
const int MX=2e5+10;
int ans[MX];
code a[MX];
main()
{
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    int test,cnt=1;
    cin>>test;
    while(test--)
    {
        int n,k;
        cin>>n>>k;
        for(int i=1;i<=n;i++)
        {
            cin>>a[i].r>>a[i].h;
            a[i].s=2*a[i].r*a[i].h;
        }
        sort(a+1 , a+n+1 , comp);
        int ans=0;
        for(int i=1;i<=n;i++)
        {
            int64_t now=a[i].r*(a[i].r+2*a[i].h);
            int cnt=k-1;
            for(int j=1;cnt;j++)
            {
                if(j==i) continue;
                now+=a[j].s;
                cnt--;
            }
            ans=max(ans,now);
        }
        cout<<"Case #"<<cnt++<<": "<<setprecision(6)<<fixed<<ans*M_PI<<endl;
    }
}
/*
 M_PI*R0(R0+2*H0)

 2*M_PI*H0*R0

*/
