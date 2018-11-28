#include <iostream>
#include <queue>
using namespace std;

int main ()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
    int test,t;
    long long int n,m,k;
    priority_queue<int> pq;
    cin>>test;
    t=test;
    while(test--)
    {
        cin>>n>>k;
        pq.push(n);
        k=k-1;
        while(k--)
        {
            if((pq.top()&1)==0)
            {
                m=pq.top();
                pq.pop();
                pq.push(m/2);
                pq.push(m/2-1);
            }
            else
            {
                m=pq.top();
                pq.pop();
                pq.push(m/2);
                pq.push(m/2);
            }
        }
        if((pq.top()&1)==0)
            cout<<"Case #"<<t-test<<": "<<pq.top()/2<<" "<<pq.top()/2-1<<endl;
        else
            cout<<"Case #"<<t-test<<": "<<pq.top()/2<<" "<<pq.top()/2<<endl;

        while(!pq.empty())
            pq.pop();
    }
    return 0;
}

