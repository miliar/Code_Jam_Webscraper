#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<bits/stdc++.h>
#include<stack>
#include<queue>
#include<list>
#include<vector>
#include<bitset>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define fio ios_base::sync_with_stdio(false)
#define mod 1000000007
#define mod1 mod
#define mod2 100000009
#define li long long int
#define ll long long int
#define readi(x) scanf("%d",&x)
#define  reads(x)  scanf("%s", x)
#define readl(x) scanf("%I64d",&x)
#define rep(i,n) for(i=0;i<n;i++)
#define revp(i,n) for(i=(n-1);i>=0;i--)
#define myrep1(i,a,b) for(i=a;i<=b;i++)
#define myrep2(i,a,b) for(i=b;i>=a;i--)
#define pb push_back
#define mp make_pair
#define fi first
#define sec second
#define MAXN 1000000000000000100
#define MINN -10000000000000
#define pii pair<li,li> 
#define pic pair<int,char>
#define N 200010
#define lgn 20
#define ddouble long double
#define minus minu
#define INTMAX 1000
using namespace std;
using namespace __gnu_pbds;
typedef priority_queue<ll, vector<ll> > max_pq;
typedef priority_queue<pii , vector<pii > ,greater<pii > > min_pq;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;
ll po[70],st[70],en[70];
int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    st[0]=1;
    en[0]=1;
    po[0]=1;
    for(ll i=1;i<=60;i++)
    {
        po[i]=po[i-1]*2;
        st[i]=en[i-1]+1;
        en[i]=en[i-1]+po[i];
    }
    ll t;
    cin>>t;
    for(ll x=1;x<=t;x++)
    {
        ll n,k;
        cin>>n>>k;
        ll i=0;
        for(i=0;i<=60;i++)
        {
            if(k<=en[i])
                break;
        }
        ll val=(n-(k-st[i]))/po[i];
        cout<<"Case #"<<x<<": ";
        cout<<(val/2)<<" "<<(val-1)/2<<"\n";
    }
}

 