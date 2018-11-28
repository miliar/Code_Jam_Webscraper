#include <iostream>
#include <vector>
#include <cstdio>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <string.h>

#define ll long long int
#define li long int
#define pi pair<int,int>
#define pl pair<li,li>
#define pll pair<ll,ll>
#define mem0(a) memset(a,0,sizeof(a))
#define mem1(a) memset(a,-1,sizeof(a))
#define MOD 1000000007
#define loop(i,n) for(ll i=0;i<n;i++)
#define loop1(i,n) for(ll i=1;i<=n;i++)
#define fast_input cin.tie(0);ios_base::sync_with_stdio(0);

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int p=0;
    while(t--)
    {
        p++;
        priority_queue <ll> pq;
        ll n,k;
        cin>>n>>k;
        k--;
        pq.push(n);
        while(k--)
        {
            ll x = pq.top();
            pq.pop();
            if(x%2==0)
            {
                pq.push(x/2);
                pq.push(x/2-1);
            }
            else
            {
                pq.push(x/2);
                pq.push(x/2);
            }
        }
        ll x = pq.top();
        ll maxi,mini;
        if(x%2==0)
        { maxi = x/2;
         mini=maxi-1;
        }
        else
        {
            maxi=mini=x/2;
        }
        cout<<"Case #"<<p<<": ";
        cout<<maxi<<" "<<mini<<endl;

    }
    return 0;
}
