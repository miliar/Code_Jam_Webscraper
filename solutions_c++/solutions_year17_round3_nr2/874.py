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
    int ac,aj;
    cin>>ac>>aj;
    int a,b,c,d;
    if(ac+aj==1)
    {
        cin>>a>>b;
        cout<<2;
        return;
    }
    cin>>a>>b>>c>>d;
    if(ac==1&&aj==1)
    {
        cout<<2;
        return;
    }
    int mi=min(a,c);
    int ma=max(b,d);
    if(ma-mi<=720)
    {
        cout<<2;
        return;
    }
    int cc=max(c,a);
    int bb=min(b,d);
    if(1440-cc+bb<=720)
    {
        cout<<2;
        return;
    }
    cout<<4;
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
