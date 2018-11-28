//template by murugappan....Copied from chamow :p

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define priq(i,comp) priority_queue( i, vector< i >,comp)

template<class t>
t lcm(t a,t b)
{
    return ((a*b)/__gcd(a,b));
}

#define fastread ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

#define maxn 10000000
// root(n) prime check
bool isprime(ll num)
{
    if(num==1)
    return false;
    ll limit=sqrt(num);
    if(num==2)
    return true;
    if(num%2==0)
    return false;
    for(ll i=3;i<=limit;i+=2)
    {
        if(num%i==0)
        {
            return false;
        }
    }
    return true;
}
//end of template



pair<ll,ll> info[2000];

ll dest,n;
ld limit=(ld)1e-10;
ld mysearch(ld left,ld right)
{
    if(abs(left-right)<limit)
        return left;
    ld mid=(left+right)/2;
    bool can=true;
    for(ll i=0;i<n;i++)
    {
        if(info[i].x>=dest)
            continue;
        ld timereq=((dest-info[i].x)*1.00)/info[i].y;
        if(timereq>mid)
        {
            can=false;
            break;
        }
    }
    if(can)
        return mysearch(left,mid);
    else
        return mysearch(mid,right);
}
int main()
{
    assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
int c=0;
    int t;
    cin>>t;
    //cout.precision(6);
       // cout<<"Case #"<<c<<": "<<fixed<<(ld)3.9999991<<endl;
    while(t--)
    {
        c++;
        cin>>dest>>n;
        for(ll i=0;i<n;i++)
        {
            cin>>info[i].x>>info[i].y;
        }
        ld left=0,right=1e13;
        ld timereq=mysearch(left,right);
        ld speed=dest/timereq;
        cout.precision(6);
        cout<<"Case #"<<c<<": "<<fixed<<speed<<endl;
    }
    return 0;
}
