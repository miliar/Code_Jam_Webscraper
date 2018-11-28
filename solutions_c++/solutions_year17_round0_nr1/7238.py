//Author:: Satish Srinivas
#include<bits/stdc++.h>

#define foi(i,m,n) for(int i=(m);i<=(n);i++)
#define fol(i,m,n) for(ll i=(m);i<=(n);i++)
#define fri(i,m,n) for(int i=(m);i>=(n);i--)
#define frl(i,m,n) for(ll i=(m);i>=(n);i--)
//#define mp make_pair
//#define pb push_back
#define pi 3.1415926536

typedef long long int ll;

ll gcd(ll a,ll b){return (b)?gcd(b,a%b):a;}
ll lcm(ll a,ll b){return (a*b)/gcd(std::max(a,b),std::min(a,b));}

using namespace std;

int main()
{
ios_base::sync_with_stdio(false);
cin.tie(NULL);

freopen("in.in", "r", stdin);
freopen("out.out", "w", stdout);

int t,te=1;
cin>>t;

while(t--)
{
    string s;
    int k;

    cin>>s>>k;

    int n = s.length();

    int c=0,i;

    for(i=0;i<n-k+1;i++)
    {
        if(s[i]=='-')
   {
       c++;
       for(int j=i;j<i+k;j++)
            {
        if(s[j]=='-')
            s[j]='+';
        else
            s[j]='-';
            }

    }

    }

    int f=0;

    for(int j=i;j<n;j++)
    {
        if(s[j]=='-')
        {
            cout<<"Case #"<<te++<<": IMPOSSIBLE"<<"\n";
        f=1;
        break;
        }

    }

    if(f==0)
            cout<<"Case #"<<te++<<": "<<c<<"\n";



}



return 0;
}
