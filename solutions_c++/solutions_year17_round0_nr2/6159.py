#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
#define present(m,v) (m.find(v)!=m.end())
#define INF 1e18
#define mod 1000000007
#define lim 1000001
#define sz(a) int(a.size())
#define all(x) (x).begin(), (x).end()
#define rep(i,n) for(i=0;i<n;i++)
#define forn(i,a,b) for(i=a;i<b;i++)

ll tidy(ll n)
{
    ll a[19],n1=n,i;
    for(i=0;i<19;i++)
        a[i]=0;
    i=18;
    while(n1>0)
    {
        a[i--]=n1%10;
        n1/=10;
    }
    ll start=i+1,minv=9;
    for(i=18;i>=0;i--)
    {
        if(a[i]<=minv)
            minv=a[i];
        else
        {
            minv=a[i]-1;
            a[i]=minv;
            for(ll j=i+1;j<19;j++)
                a[j]=9;
        }
    }
    ll ans=0;
    for(i=0;i<19;i++)
    {
        ans=ans*10+a[i];
    }
    return ans;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");
	ll t,n,i,l;
	fin>>t;
	for(l=1;l<=t;l++)
    {
        fin>>n;
        fout<<"Case #"<<l<<": ";
        fout<<tidy(n)<<endl;
    }
	fin.close();
    fout.close();
	return 0;
}
