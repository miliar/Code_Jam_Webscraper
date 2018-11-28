#include<bits/stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    int T,c=1;
    ll N,M;
    cin>>T;
    while(T--)
    {
        cin>>N>>M;
        priority_queue<ll> pq;
        pq.push(N);M--;
        while(M--)
        {
            ll v = pq.top();
            pq.pop();
            if( v%2==0 ){
                pq.push(v/2);
                pq.push(v/2-1);
            }else{
                pq.push(v/2);
                pq.push(v/2);
            }
        }
        ll a,b;
        a = pq.top();
        b = a/2;
        if(a%2==0) b--;
        a = a/2;
        cout<<"Case #"<<c++<<": ";
        cout<<a<<' '<<b<<'\n';
    }
}

