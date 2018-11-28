#include <iostream>
#include <string>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define ld long double
#define vi vector< int >
#define vll vector< ll >
#define pii pair<int, int>
#define pll pair<ll, ll>
#define piii pair<int, pair<int, int> >
#define plll pair<ll, pair<ll, ll> >
#define rep(i, l, r) for (long long int i = l; i < r; i++)
#define repb(i, r, l) for (long long int i = r; i >= l; i--)
#define sz(a) (int)a.size()
#define fi first
#define se second
priority_queue<ll> mypq;
int main()
{
    int T;
    ll K,N,b,a;
    cin>>T;
    rep(i,0,T)
    {
        mypq=priority_queue <ll>();
        cin>>N>>K;
        mypq.push(N);
        while(K--)
        {
            b=mypq.top();
            mypq.pop();
            b--;
            a=b/2;
            mypq.push(a);
            mypq.push(b-a);
        }
        cout<<"Case #"<<i+1<<": "<<max(a,b-a)<<" "<<min(a,b-a)<<"\n";
    }
}