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
        cin>>v[i];
}
void print(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        cout<<v[i];
}
void fun()
{
    double d;
    int n;
    cin>>d>>n;
    double c=0;
    for(int i=0;i<n;i++)
    {
        double dis,speed;
        cin>>dis>>speed;
        c=max(c,(d-dis)/speed);
    }
    double ans=d/c;
    cout<<fixed<<setprecision(18)<<ans;
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
    int t=1;
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
