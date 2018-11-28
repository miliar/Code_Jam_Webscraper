#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";

        ll n,k;
        ll mx,mn,cnt;
        cin>>n>>k;
        map<ll,ll>mp;
        mp[n]=1;
        while(k>0)
        {
            auto it = mp.end();
            it--;
            n=it->first;
            cnt=it->second;
            mp.erase(it);
            mx=n/2;//4 -> 2 , 5 -> 2
            mn=(n-1)/2;//4 -> 1 , 5 -> 2
            mp[mx]+=cnt;
            mp[mn]+=cnt;
            k-=cnt;
        }
        cout<<mx<<" "<<mn<<"\n";
    }
    return 0;
}
