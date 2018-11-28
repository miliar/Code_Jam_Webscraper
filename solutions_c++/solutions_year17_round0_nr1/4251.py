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

    string s;
    cin>>s;
    int k;
    cin>>k;
    int n=s.length();
    ll ans=0;
    bool flag=true;
    for(ll i=0;i<=n-k;i++)
    {
        if(s[i]=='-')
        {
            ans++;
            for(ll j=0;j<k;j++)
            {
                if(s[i+j]=='-')
                    s[i+j]='+';
                else if(s[i+j]=='+')
                    s[i+j]='-';
            }
        }

    }
    for(ll i=(n-k)+1;i<n;i++)
    {
        if(s[i]=='-')
            {
                flag=false;
                break;
            }
    }
    if(flag)
        cout<<"Case #"<<te<<": "<<ans<<endl;
    else
        cout<<"Case #"<<te<<": IMPOSSIBLE"<<endl;



}







    return 0;
}




