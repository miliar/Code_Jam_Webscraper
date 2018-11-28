#include<bits/stdc++.h>
#define ll long long
#define vll vector<ll>
#define mll map<ll,ll>
#define sll set<ll>
#define fo(i,n) for(i=0;i<n;i++)
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    //freopen("000.txt","r",stdin);
    //freopen("0as.in","r",stdin);
    freopen("0al.in","r",stdin);
    //freopen("02as.txt","w",stdout);
    freopen("02al.txt","w",stdout);

    ll n,i,j,k,t,l;
    double a,b,d,e,f;
    cin>>t;

    cout<<fixed<<setprecision(12);
    for(l=1;l<=t;l++)
    {
        cout<<"Case #"<<l<<": ";

        cin>>d>>n;

        f=0;
        fo(i,n)
        {
            cin>>a>>b;

            e=(d-a)/b;
            f=max(f,e);
        }

        cout<<d/f;
        cout<<endl;
    }

    return 0;
}
