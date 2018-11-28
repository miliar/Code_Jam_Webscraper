#include <iostream>
#include <functional>
#include <queue>

using namespace std;

#define ll long long

int main()
{
    ll t;
    cin>>t;
    ll z;
    for(z=1;z<=t;z++)
    {
        priority_queue <ll> pq;
        ll n;
        ll k,x,max,min;
        cin>>n>>k;
        pq.push(n);
        while(k--)
        {
            x = pq.top();
            pq.pop();
            if(x%2==0)
            {
                max = x/2;
                min = (x/2)-1;
                pq.push(max);
                pq.push(min);
            }
            else
            {
                max = x/2;
                min = x/2;
                pq.push(max);
                pq.push(min);
            }
        }
        cout<<"Case #"<<z<<": "<<max<<" "<<min<<endl;
    }
    return 0;
}