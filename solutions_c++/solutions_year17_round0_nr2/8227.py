#include<bits/stdc++.h>
using namespace std;
#define ll long long
bool check(int x)
{
    vector<int> v;
    while(x)
    {
        v.push_back(x%10);
        x/=10;
    }
    reverse(v.begin(),v.end());
    bool f=1;
    for(int i=1;i<v.size();i++)
    {
        if(v[i]<v[i-1])
        {
            f=0;break;
        }
    }
    return f;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,n,k,i,j,ans;
    cin>>t;
    for(ll te=1;te<=t;te++)
    {
        cin>>n;
        for(i=n;i>=1;i--)
            if(check(i))
        {
            cout<<"Case #"<<te<<": "<<i<<endl;
            break;
        }
    }
    return 0;
}
