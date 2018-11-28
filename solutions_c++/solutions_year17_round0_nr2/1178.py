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
#define ll int
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
typedef priority_queue<pii, vector<pii> > max_pq;
typedef priority_queue<pii , vector<pii > ,greater<pii > > min_pq;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;
int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t;
    cin>>t;
    for(ll x=1;x<=t;x++)
    {
        string c;
        cin>>c;
        string ans;
        ll i=0,flag=0;
        if(c.size()==1)
            cout<<"Case #"<<x<<": "<<c<<"\n";
        else
        {
            for(i=0;i<(c.size()-1);i++)
            {
                if(c[i]<=c[i+1])
                {

                }
                else
                {
                    flag=1;
                    break;
                }
            }
            if(!flag)
            {
                cout<<"Case #"<<x<<": "<<c<<"\n";    
                continue;
            }
            ll en=i;
            ll st=i;
            for(ll j=en-1;j>=0;j--)
            {
                if(c[j]==c[j+1])
                {
                    st--;
                }
                else
                {
                    break;
                }
            }
            cout<<"Case #"<<x<<": ";;
            for(ll i=0;i<st;i++)
                cout<<c[i];
            if(c[st]!='1')
                cout<<(char)(c[st]-1);
            for(ll i=st+1;i<c.size();i++)
                cout<<'9';
            cout<<"\n";
        }
    }
}

 