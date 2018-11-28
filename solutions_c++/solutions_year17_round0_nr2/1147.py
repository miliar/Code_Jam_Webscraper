#include<bits/stdc++.h>
#include <stdio.h>

using namespace std;

#define mod 1000000007LL
#define pi 3.141592653589793238462643383279;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define f first
#define s second
#define pic pair<char,long long >
void scan(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        scanf("%d",&v[i]);
}

void print(vector<ll> & v)
{
    for(ll i=0;i<v.size();i++)
        printf("%lld",v[i]);
}
// b large
void fun()
{
    ll n;
    cin>>n;
    vector<ll> v;
    while(n)
    {
        v.push_back(n%10);
        n/=10;
    }
    reverse(v.begin(),v.end());
    ll i=0;
    for(;i<v.size()-1;i++)
    {
        if(v[i]>v[i+1])
            break;
    }
    if(i==v.size()-1)
    {
        // print no
        print(v);
        return;
    }
    for(ll j=i+1;j<v.size();j++)
        v[j]=9;
    ll x=v[i];
    ll j=i;
    while(j>0&&v[j]==v[j-1])
    {
        v[j]=9;
        j--;
    }
    if(v[j]==1&&j==0)
    {
        v.erase(v.begin());
        print(v);
        return;
    }
    else
    {
        v[j]--;
        print(v);
        // print no
    }

}
int main()
{

    bool test=1;
    if(test==1)
    {
        freopen("input_file_name.txt","r",stdin);
        freopen("output_file_name.txt","w",stdout);
    }
    int t;
    scanf("%d",&t);
    //cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        fun();
        cout<<endl;
    }
    //int acc;cin>>acc;
    return 0;
}
