#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int xx=1;xx<=t;xx++)
    {
    int x,a;
    cin>>x;
    priority_queue<ll>pq;
    pq.push(x);
    cin>>a;
    cout<<"Case #"<<xx<<": ";
    while(pq.empty()==false )
    {

        ll p=pq.top();

        pq.pop();
        if(p%2==0)
        {
            if(a==1)
            {
                cout<<p/2<<" "<<p/2-1<<endl;
                break;
            }
            pq.push(p/2-1);
            pq.push(p/2);
        }
        else
        {
            if(a==1)
            {
                cout<<(p-1)/2<<" "<<(p-1)/2<<endl;
                break;
            }
            pq.push((p-1)/2);
            pq.push((p-1)/2);
        }
        a--;
    }

    }
    return 0;
}
