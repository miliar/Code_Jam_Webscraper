#include<bits/stdc++.h>
using namespace std;
#define ll long long
struct comparator
{
    bool operator()(ll a,ll b)
    {
        return a<b;
    }
};
int main()
{
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    ll t;
    cin>>t;
    int c=0;
    while(t--)
    {

        c++;
        ll n,k;
        cin>>n>>k;
        priority_queue< ll, vector<ll>, comparator >p;
        p.push(n);
        for(int i=1;i<k;i++)
        {
            ll temp=p.top();
            //cout<<temp<<endl;
            p.pop();
            ll pos=(temp+1)/2;
            p.push(pos-1);
            p.push(temp-pos);
        }
        ll temp=p.top();
        //cout<<temp<<endl;
            p.pop();
            ll pos=(temp+1)/2;
        cout<<"Case #"<<c<<": "<<max(pos-1,temp-pos)<<" "<<min(pos-1,temp-pos)<<"\n";

    }
    return 0;
}
