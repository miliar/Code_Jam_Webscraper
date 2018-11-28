#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define ld long double
#define ii pair<int,int>
#define iii pair<ii,int>
#define vii vector<pair<int,ll> >
#define vi vector<ll>
#define vvi vector<vector<int> >
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define nu 100001
#define mod 1000000007
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)

int k,n;
int f(string s,int m,int v)
{
    int flag=0;
    for(int i=0;i<n;++i)
    {
        if(s[i]!='+')
        flag++;
    }
    
    if(!flag)
    return v;
    
    if(m>n-k)
    return 100;
    
    string t=s;
    for(int i=m;i<m+k;++i)
    {
        if(s[i]=='+')
        t[i]='-';
        else
        t[i]='+';
    }
    return min(f(s,m+1,v),f(t,m+1,v+1));
}

int main()
{
    fastio;
    int t;
    cin>>t;
    
    for(int l=1;l<=t;++l)
    {
        string s;
        cin>>s;
        
        n=s.length();
        cin>>k;
        int x=f(s,0,0);
        if(x>n)
        cout<<"Case #"<<l<<": "<<"IMPOSSIBLE"<<'\n';
        else
        cout<<"Case #"<<l<<": "<<x<<'\n';
    }
}

