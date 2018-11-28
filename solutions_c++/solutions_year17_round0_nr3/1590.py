#include <bits/stdc++.h>
using namespace std;
#define ll          long long
#define MOD         1000000007
#define ll          long long
#define pb          push_back
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define endl        '\n'
#define PI          3.14159265359d
#define sz(x)       (int)x.size()
#define INF         INT_MAX
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int t,T;
    ll n,k;
    map<ll,ll> mp;
    map<ll,ll>::reverse_iterator it;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>n>>k;
        mp.clear();
        mp[n]++;
        for(it=mp.rbegin();it!=mp.rend();it++)
        {
            k-=it->S;
            if(k<=0)
                break;
            mp[(it->F-1)/2]+=it->S;
            mp[it->F-1-(it->F-1)/2]+=it->S;
        }
        cout<<"Case #"<<t<<": "<<max((it->F-1)/2,it->F-1-(it->F-1)/2)<<" "<<min((it->F-1)/2,it->F-1-(it->F-1)/2)<<endl;
    }
    return 0;
}
