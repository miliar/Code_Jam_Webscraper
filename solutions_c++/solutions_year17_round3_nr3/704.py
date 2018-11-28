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


void scan(vector<ll> & v)
{
    for(int i=0;i<v.size();i++)
        cin>>v[i];
}
void print(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        cout<<v[i];
}

void fun()
{
    int n,k;
    cin>>n>>k;
    double u,uu;
    cin>>u;
    vector<double> v(n);
    for(int i=0;i<n;i++)
        cin>>v[i];
    sort(v.begin(),v.end());
    uu=u;
    int i=0;
    for(;i<n-1;i++)
    {

        if((v[i+1]-v[i])*(i+1)>u)
        {
            break;
        }
        u-=((v[i+1]-v[i])*(i+1));
    }
    int index=i;
    for(int i=0;i<=index;i++)
    {
        uu+=v[i];
    }
    uu/=(index+1);

    double ans=1;
    for(int i=0;i<=index;i++)
    {
        ans*=(uu);
    }
    for(int i=index+1;i<n;i++)
    {
        ans*=v[i];
    }
    cout<<fixed<<setprecision(15)<<ans;
}

int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);cout.tie(0);
    bool test=1;
    if(test==1)
    {
        freopen("input_file_name.txt","r",stdin);
        freopen("output_file_name.txt","w",stdout);
    }
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        fun();
        cout<<endl;
    }
    int acc;cin>>acc;
    return 0;
}
