#include <iostream>
#include <queue>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("C-small-2.in", "r", stdin);
    freopen("C-small-2.out", "w", stdout);
    int T,n,k,mx,mn, cur;
    cin>>T;
    for(int c=1;c<=T;c++)
    {
        cin>>n>>k;
        priority_queue <int> pq;
        pq.push(n);
        while(k--)
        {
            cur = pq.top();
            pq.pop();
            mx = int(cur/2);
            mn = int((cur-1)/2);
            pq.push(mx);
            pq.push(mn);
        }
        cout<<"Case #"<<c<<": "<<mx<<" "<<mn<<endl;
    }
}