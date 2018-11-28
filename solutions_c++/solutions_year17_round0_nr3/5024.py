#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
    ll t;
    ll n;
    ll k;
    ll abcd;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        cin>>n;
        cin>>k;

        priority_queue<ll> prior_queue;
        ll left,right,max1,min1;
        abcd = n;
        for(int j=0; j<k; j++)
        {
           abcd = abcd -1;
           left = abcd/2;
           right = abcd - left;
           prior_queue.push(left);
           prior_queue.push(right);
           max1=max(left,right);
           min1=min(left,right);
           abcd=prior_queue.top();
           prior_queue.pop();
        }
        cout<<"Case #"<<i+1<<": "<<max1<<" "<<min1<<endl;
        while(!prior_queue.empty())
        {
			prior_queue.pop();
        }
    }
    return 0;
}



