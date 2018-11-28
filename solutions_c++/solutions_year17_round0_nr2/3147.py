#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int T;
ll m;
int ok(ll m)
{
    vector<int> f;
    while(m)
    {
        f.push_back(m%10);
        m/=10;
    }
    auto r = f.begin();
    auto l = r++;
    while(r!=f.end())
    {
        if(*l<*r)
            return 0;
        l++;
        r++;
    }
    return 1;
}
ll deal(ll m)
{

    vector<int>f;
    vector<ll>ans;
    ans.push_back(m);
    while(m)
    {
        f.push_back(m%10);
        m/=10;
    }
    int size = f.size();
    for(int i=0;i<size;i++)
    {
        for(int j=0;j<i;j++)
            f[j]=9;
        f[i]=f[i]-1;
        if(f[i]<0)
            continue;
        ll temp = 0;
        ll base = 1;
        for(int j=0;j<size;j++)
        {
            temp+=base*(ll)f[j];
            base*=10LL;
        }
        ans.push_back(temp);
    }
    sort(ans.begin(),ans.end());
    reverse(ans.begin(),ans.end());
    for(auto e:ans)
        if(ok(e))
            return e;
    return 1;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    cin>>T;
    for(int it=1;it<=T;it++)
    {
        cin>>m;
        printf("Case #%d: ",it);
        cout<<deal(m)<<endl;
    }
    return 0;
}
