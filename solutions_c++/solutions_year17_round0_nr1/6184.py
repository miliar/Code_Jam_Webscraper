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
int l;
int pos(string z,int k)
{
    rep(i,k,l)
    {
        if(z[i]=='-')
        {
            return i;
        }
    }
    return l;
}
int main()
{
    int T,i,p,S,c=0;
    string X;
    cin>>T;
    rep(i,0,T)
    {
        cin>>X;
        l=X.length();
        cin>>S;
        p=pos(X,0);
        c=0;
        while(p<=l-S)
        {
            c++;
            rep(j,p,p+S)
            {
                if(X[j]=='-')
                {
                    X[j]='+';
                }
                else if(X[j]=='+')
                {
                    X[j]='-';
                }
            }
            p=pos(X,p);
        }
        cout<<"Case #"<<i+1<<": ";
        if(p==l)
        {
            cout<<c<<"\n";
        }
        else
        {
            cout<<"IMPOSSIBLE\n";
        }
    }
}