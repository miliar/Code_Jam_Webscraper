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
map<string,int> L;
bool ch(long long int k)
{
    ll o,t;
    o=k%10;
    while(k>0)
    {
        t=k%10;
        k=k/10;
        if(t>o)
        {
            return false;
        }
        o=t;
    }
    return true;
}
int main()
{
    int T;
    long long int N;
    cin>>T;
    rep(i,0,T)
    {
        cin>>N;
        while(1)
        {
            if(ch(N))
            {
                cout<<N<<"\n";
                break;
            }
            N--;
        }
    }
}