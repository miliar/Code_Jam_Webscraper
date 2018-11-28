#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
int main()
{
    ifstream inp;
    ofstream out;
    inp.open("input.txt");
    out.open("output.txt");
    int T;
    ll int n,k;
    inp>>T;
    for(int t=1;t<=T;t++)
    {
        inp>>n>>k;
        vector<ll int> v;
        ll int num = n,N;
        ll int cnt= 0;
        while(num!=0)
        {
            cnt++;
            num = num>>1;
        }
        num = 1;
        if(cnt!=64)
            N = (num<<cnt)-1;
        else
            N = LLONG_MAX;
        num = N - n;
        while(N!=1)
        {
            N = N/2;
            v.pb(N);
        }
        out<<"Case #"<<t<<": ";
        ll int counT=1,ans=-1;
        cnt = 2;
        if(k==1)
        {
            if(n&1)
                out<<n/2<<' '<<n/2<<endl;
            else
                out<<n/2<<' '<<n/2-1<<endl;
            continue;
        }
        for(int i=0;i<v.size();i++)
        {
            ll int d,r,val1,val2,cnt1,cnt2;
            d = num/cnt;
            r = num%cnt;
            val1 = v[i]-d;
            cnt1 = cnt-r;
            if(counT+cnt1>=k)
            {
                ans = val1;
                break;
            }
            val2 = val1-1;
            cnt2 = r;
            counT+=cnt;
            if(r!=0 && counT>=k)
            {
                ans = val2;
                break;
            }
            cnt*=2;
        }
        if(ans&1)
            out<<ans/2<<' '<<ans/2<<endl;
        else
            out<<ans/2<<' '<<ans/2-1<<endl;
    }
    return 0;
}
