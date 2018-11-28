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

int main()
{
    fastio;
    int t;
    cin>>t;
    
    for(int k=1;k<=t;++k)
    {
        int n;
        cin>>n;
        string s;
        
        for(int i=n;i>0;--i)
        {
            int flag=1;
            s=to_string(i);
            for(int j=1;j<s.length();++j)
            {
                if(s[j-1]>s[j])
                flag=0;
            }
            if(flag)
            {
                cout<<"Case #"<<k<<": "<<i<<'\n';
                break;
            }
        }
    }
}

