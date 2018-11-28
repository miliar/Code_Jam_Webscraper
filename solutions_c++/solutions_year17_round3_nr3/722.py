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
void scan(vector<ll> & wfkwjfwkfjwkf)
{
    for(int pkpkpk=0;pkpkpk<wfkwjfwkfjwkf.size();pkpkpk++)
        cin>>wfkwjfwkfjwkf[pkpkpk];
}
void print(vector<int> & wfkwjfwkfjwkf)
{
    for(int pkpkpk=0;pkpkpk<wfkwjfwkfjwkf.size();pkpkpk++)
        cout<<wfkwjfwkfjwkf[pkpkpk];
}
void fnwfkwnkjew()
{
    int n,k;
    cin>>n>>k;
    double u,knkenkjenkenkjnw;
    cin>>u;
    vector<double> wfkwjfwkfjwkf(n);
    for(int pkpkpk=0;pkpkpk<n;pkpkpk++)
        cin>>wfkwjfwkfjwkf[pkpkpk];
    sort(wfkwjfwkfjwkf.begin(),wfkwjfwkfjwkf.end());
    knkenkjenkenkjnw=u;
    int pkpkpk=0;
    for(;pkpkpk<n-1;pkpkpk++)
    {
        if((wfkwjfwkfjwkf[pkpkpk+1]-wfkwjfwkfjwkf[pkpkpk])*(pkpkpk+1)>u)
        {
            break;
        }
        u-=((wfkwjfwkfjwkf[pkpkpk+1]-wfkwjfwkfjwkf[pkpkpk])*(pkpkpk+1));
    }
    int fnwlknwlnkw=pkpkpk;
    for(int pkpkpk=0;pkpkpk<=fnwlknwlnkw;pkpkpk++)
    {
        knkenkjenkenkjnw+=wfkwjfwkfjwkf[pkpkpk];
    }
    knkenkjenkenkjnw/=(fnwlknwlnkw+1);
    double wjwlcjfwlcjwjcw=1;
    for(int pkpkpk=0;pkpkpk<=fnwlknwlnkw;pkpkpk++)
    {
        wjwlcjfwlcjwjcw*=(knkenkjenkenkjnw);
    }
    for(int pkpkpk=fnwlknwlnkw+1;pkpkpk<n;pkpkpk++)
    {
        wjwlcjfwlcjwjcw*=wfkwjfwkfjwkf[pkpkpk];
    }
    cout<<fixed<<setprecision(15)<<wjwlcjfwlcjwjcw;
}
int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);cout.tie(0);

        freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    int kwnckwnc;
    cin>>kwnckwnc;
    for(int pkpkpk=1;pkpkpk<=kwnckwnc;pkpkpk++)
    {
        cout<<"Case #"<<pkpkpk<<": ";
        fnwfkwnkjew();
        cout<<endl;
    }
    return 0;
}
