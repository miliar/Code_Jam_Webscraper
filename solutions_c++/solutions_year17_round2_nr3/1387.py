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
//ll arr[6];
//ll red,orange,yellow,green,blue,violet;
//ll redc,yellowc,bluec;
int c;
ld inf=std::numeric_limits<long double>::infinity();
int main()
{
   assert(freopen("input.txt","r",stdin));
 assert(freopen("output.txt","w",stdout));
    //small dataset
    int t;
    cin>>t;
    while(t--)
    {
        c++;
        int n,q;
        cin>>n>>q;
        ll adjmat[n+1][n+1];
        ll distance[n+1],speed[n+1];
        ld timereq[n+1];
        for(ll i=0;i<=n;i++)
            timereq[i]=inf;
        timereq[1]=0;
        for(ll i=1;i<=n;i++)
            cin>>distance[i]>>speed[i];
        for(ll i=1;i<=n;i++)
        {
            for(ll j=1;j<=n;j++)
                cin>>adjmat[i][j];
        }
        ll src,dest;
        cin>>src>>dest;
        //starting position
        for(ll i=1;i<=n;i++)
        {
            ll travel=0;
            //to dest
            ll prev=i;
            for(ll j=i+1;j<=n;j++)
            {
                travel+=adjmat[prev][j];
                if(travel>distance[i])
                    break;
                timereq[j]=min(timereq[j],timereq[i]+((travel*1.000)/speed[i]));
                prev=j;
            }
        }
        cout.precision(10);
        cout<<"Case #"<<c<<": "<<fixed<<timereq[n]<<endl;
    }
    return 0;
}


