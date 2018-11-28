#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
#define ll long long int
#define ld long double
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>
#define vvi vector<vector<int> >
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define nu 100001
#define mod 1000000007
ll tree[1000005];
ll lazy[1000005];
ll A[100005];
void build(ll node,ll start, ll end)
{
    if(start == end)
    {
        // Leaf node will have a single element
        tree[node] = A[start];
    }
    else
    {
        ll mid = (start + end) / 2;
        // Recurse on the left child
        build(2*node, start, mid);
        // Recurse on the right child
        build(2*node+1, mid+1, end);
        // Internal node will have the sum of both of its children
        tree[node] = tree[2*node] + tree[2*node+1];
    }
}
void updateRange(ll node, ll start, ll end, ll l, ll r, ll val)
{
    if(lazy[node] != 0)
    { 
        // This node needs to be updated
        tree[node] += (end - start + 1) * lazy[node];    // Update it
        if(start != end)
        {
            lazy[node*2] += lazy[node];                  // Mark child as lazy
            lazy[node*2+1] += lazy[node];                // Mark child as lazy
        }
        lazy[node] = 0;                                  // Reset it
    }
    if(start > end or start > r or end < l)              // Current segment is not within range [l, r]
        return;
    if(start >= l and end <= r)
    {
        // Segment is fully within range
        tree[node] += (end - start + 1) * val;
        if(start != end)
        {
            // Not leaf node
            lazy[node*2] += val;
            lazy[node*2+1] += val;
        }
        return;
    }
    ll mid = (start + end) / 2;
    updateRange(node*2, start, mid, l, r, val);        // Updating left child
    updateRange(node*2 + 1, mid + 1, end, l, r, val);   // Updating right child
    tree[node] = tree[node*2] + tree[node*2+1];        // Updating root with max value 
}

ll queryRange(ll node, ll start, ll end, ll l, ll r)
{
    if(start > end or start > r or end < l)
        return 0;         // Out of range
    if(lazy[node] != 0)
    {
        // This node needs to be updated
        tree[node] += (end - start + 1) * lazy[node];            // Update it
        if(start != end)
        {
            lazy[node*2] += lazy[node];         // Mark child as lazy
            lazy[node*2+1] += lazy[node];    // Mark child as lazy
        }
        lazy[node] = 0;                 // Reset it
    }
    if(start >= l and end <= r)             // Current segment is totally within range [l, r]
        return tree[node];
    ll mid = (start + end) / 2;
    ll p1 = queryRange(node*2, start, mid, l, r);         // Query left child
    ll p2 = queryRange(node*2 + 1, mid + 1, end, l, r); // Query right child
    return (p1 + p2);
}

int main()
{
    ll t;
    cin>>t;
    for(ll i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        string s;
        ll k;
        cin>>s>>k;
        ll n=s.size();
        build(1,1,s.size());
        ll ans=0;
        for(ll i=0;i<s.size()-k+1;i++)
        {
            if((s[i]=='-'&&queryRange(1,1,n,i+1,i+1)%2==0)||(s[i]=='+'&&queryRange(1,1,n,i+1,i+1)%2==1))
            {
                updateRange(1,1,n,i+1,i+1+k-1,1);ans++;
            }
        }
        ll flag=0;
        for(ll i=0;i<s.size();i++)
        {
            if((s[i]=='-'&&queryRange(1,1,n,i+1,i+1)%2==0)||(s[i]=='+'&&queryRange(1,1,n,i+1,i+1)%2==1))
            {
                flag=1;
            }
        }
        if(flag==0)
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
        for(ll i=1;i<=s.size();i++)
            A[i]=0;
        for(ll i=1;i<=5000;i++)
            lazy[i]=0,tree[i]=0;
    }
}