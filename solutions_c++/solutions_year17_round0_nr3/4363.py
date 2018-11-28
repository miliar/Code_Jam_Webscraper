#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<map>
#include<cstdio>
#include<algorithm>
#define ll long long int
#define loop(i,n) for(ll i=0;i<n;i++)
#define loop2(i,a,b) for(ll i=a;i<b;i++)
#define mp(a,b) make_pair(a,b)
using namespace std;


ll power(ll a ,ll b)
{

    ll c=0;
    if(b==1)
        return a;
    if(b&1)//odd
    {
        c = power(a,b-1);
        return a*c;
    }
    else
    {
        c=power(a,b/2);
        return c*c;
    }

}

int main()
{

cin.tie(0);
cout.tie(0);

cin.sync_with_stdio(false);
cout.sync_with_stdio(0);


freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

int t;
cin>>t;
for(ll te=1;te<=t;te++)
{

    ll n,k;
    cin>>n>>k;
    priority_queue<ll> pq;

    pq.push(n);
    for(ll i=1;i<k;i++)
    {
        ll top=pq.top();
        pq.pop();
        if(top&1)
        {
            ll half=top>>1;
            pq.push(half);
            pq.push(half);
        }
        else
        {
            ll half=top>>1;
            ll half2=(top-1)>>1;
            pq.push(half);
            pq.push(half2);
        }
    }

    ll half1;
    ll half2;

    ll top=pq.top();
    if(top&1)
        {
            half1=top>>1;
            half2=top>>1;
        }
        else
        {
            half1=top>>1;
            half2=(top-1)>>1;
        }



    cout<<"Case #"<<te<<": "<<half1<<" "<<half2<<endl;


   }






    return 0;
}




