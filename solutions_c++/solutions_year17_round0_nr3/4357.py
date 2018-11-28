#include <bits/stdc++.h>
using namespace std;

int main() {

    // your code goes here
    int t;
    cin>>t;
    long long int n,k,l,r,x;
    for(int y = 1; y <= t; y++)
    {
        priority_queue<long long int> pq;
        cin>>n>>k;
        pq.push(n);
        for(int i = 0; i < k ; i++)
        {
            x = pq.top();
            pq.pop();
            if(x <= 0) break;
            if(x%2 == 0){
                l = x/2 - 1;
                r = x/2;
                pq.push(l);
                pq.push(r);
            }
            else
            {
                l = x/2;
                r = x/2;
                pq.push(l);
                pq.push(r);
            }
        }
        cout<<"Case #"<<y<<": "<<r<<" "<<l<<endl;
    }
    return 0;
}