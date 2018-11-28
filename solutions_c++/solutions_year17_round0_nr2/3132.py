#include <bits/stdc++.h>
using namespace std;
#define f(i,a,b) for(int i=a;i<b;i++)
#define b(i,a,b) for(int i=a;i>b;i--)
#define mpr(a,b) make_pair(a,b)
#define prll pair<ll,ll>
#define si(s) scanf("%d",&s)
#define pri pair<int,int>
#define ll long long
#define inf INT_MAX/10
#define gmax 200005
#define mod 1000000009
#define mod1 1610612741
#define mod2 1000000009
#define line cout<<"\n"
#define bp __builtin_popcount
#define pb push_back
#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define getfile freopen("C:\\Users\\VISHAL ASHANK\\Desktop\\B-large.in","r",stdin)
#define givefile freopen("C:\\Users\\VISHAL ASHANK\\Desktop\\inp2.txt","w",stdout)
vector<int> digits;
void filldig(ll num)
{
    while(num!=0)
    {
        int d=num%10;
        digits.pb(d);
        num=num/10;
    }
    reverse(digits.begin(),digits.end());
}
main()
{
    getfile;
    givefile;
    int t,tot;
    cin>>t;tot=t;
    while(t--)
    {
        ll n;
        cin>>n;
        digits.clear();
        filldig(n);int mx=digits[0];int posc=0;int pos=0;
        f(i,1,digits.size())
        {
            if(digits[i]<digits[i-1])
            {
                break;
            }
            else if(digits[i]>digits[i-1])
            {
                mx=digits[i];
                posc=i;
                pos=i;
            }
            else
            {
                pos=i;
            }
        }
        ll ans=0;
        if(pos==digits.size()-1)
        {
            //cout<<n;
            ans=n;
        }
        else
        {
            ll ten=10;
            f(i,0,posc)
            {
                ans=ans*ten+(ll)digits[i];
            }
            ans=ans*ten+(ll)(digits[posc]-1);ll nine=9;
            f(i,0,digits.size()-posc-1)
            ans=ans*ten+nine;
        }
        cout<<"Case #"<<tot-t<<": ";
        cout<<ans<<endl;
    }
}
