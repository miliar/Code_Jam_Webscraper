//Author:: Satish Srinivas
#include<bits/stdc++.h>

#define foi(i,m,n) for(int i=(m);i<=(n);i++)
#define fol(i,m,n) for(ll i=(m);i<=(n);i++)
#define fri(i,m,n) for(int i=(m);i>=(n);i--)
#define frl(i,m,n) for(ll i=(m);i>=(n);i--)
//#define mp make_pair
//#define pb push_back
#define pi 3.1415926536

typedef unsigned long long int ll;

ll gcd(ll a,ll b){return (b)?gcd(b,a%b):a;}
ll lcm(ll a,ll b){return (a*b)/gcd(std::max(a,b),std::min(a,b));}

using namespace std;


int main()
{
ios_base::sync_with_stdio(false);
cin.tie(NULL);

freopen("in2.in", "r", stdin);
freopen("out2.out", "w", stdout);

ll t,te=1;
string n;

cin>>t;

while(t--)
{
    cin>>n;

    ll l=n.length();
    ll f=0,i;
    ll co=0,ans =0;

    for(i=0;i<l-1;i++)
    {
        if(n[i]<=n[i+1])
        {

            if(n[i]==n[i+1])
            {
            ans=ans*10+ n[i]-'0';
            co++;
            }

            else
           {
            co=0;
            ans=ans*10+ n[i]-'0';
            }
        }


        else
        {
            f=1;

            if(co==0)
            {
            if(n[i]!='0')
            ans=ans*10+ n[i]-'0'-1;
            else
                ans=ans*10+ '9' - '0';
            }

            else
            {
                ans=ans/(pow(10,co));

            if(n[i]!='0')
            ans=ans*10+ n[i]-'0'-1;
            else
                ans=ans*10+ '9' - '0';

            i=i-co;

            }
            break;
        }
    }

    if(f==1)
    {
        for(ll j=i+1;j<l;j++)
        {

            ans=ans*10+9;
        }
    }

    else
        ans=ans*10+ n[l-1] - '0';


      cout<<"Case #"<<te++<<": "<<ans<<endl;

}

return 0;
}
