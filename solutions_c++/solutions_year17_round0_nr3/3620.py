#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
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
int main()
{
    ll t;
    cin>>t;
    for(ll i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        ll n,k;
        cin>>n>>k;
        ll start=1;
        ll end=n+2;
        priority_queue<ld> pq;
        pq.push((ld)n);ld p,q,r;
        while(k>1)
        {
           r = pq.top();
           p = ceil(r/2);
           q = floor(r/2);
           p = p-1;
           pq.pop();
           pq.push(p);
           pq.push(q);
           k--;
        }
        r = pq.top();
        p = ceil(r/2);
        q = floor(r/2);
        cout<<max(p-1,q)<<" "<<min(p-1,q)<<endl;
    }
}