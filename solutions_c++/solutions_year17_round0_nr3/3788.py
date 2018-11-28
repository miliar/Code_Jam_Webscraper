#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t,a=1;
    ll n,k,tmp,x,L,R;
    cin>>t;
    while(a<=t)
    {
        priority_queue<int> Q;
        cin>>n>>k;
        Q.push(n);
        while(k--)
        {
            tmp=Q.top();
            Q.pop();
            if(tmp%2==0)
            {
                x=tmp/2;
                L=x-1;
                R=x;
                if(R>=1)
                    Q.push(R);
                if(L>=1)
                    Q.push(L);
            }
            else
            {
                x=tmp/2;
                L=x;
                R=x;
                if(R>=1)
                {
                    Q.push(x);
                    Q.push(x);
                }
            }
        }
        cout<<"Case #"<<a<<": "<<R<<" "<<L<<endl;
        a++;
    }
}














