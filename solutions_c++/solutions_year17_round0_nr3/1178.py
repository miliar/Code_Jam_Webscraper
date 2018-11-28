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

void print(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        printf("%d ",v[i]);
}
// c large
void fun()
{
    ll n,k;
    cin>>n>>k;
    ll low=n;
    for(ll j=0;;j++)
    {
        ll temp=1LL<<j;
        if(k-temp<=0)
        {
            //low=(low-1)/2;
            low--;
            ll lef=(n-(temp-1))%temp;
            if(lef>=k)
            {
                low++;
                cout<<low-low/2<<" "<<low/2;
            }
            else
            {
                cout<<low-low/2<<" "<<low/2;
            }
            return;
        }
        low=(low-1)/2;
        k-=temp;
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
    int acc;cin>>acc;
    return 0;
}
