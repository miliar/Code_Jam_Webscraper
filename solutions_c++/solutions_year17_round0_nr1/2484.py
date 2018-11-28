#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b)                for(ll i=a;i<b;i++)
#define repr(i,n)                for(ll i=n-1;i>=0;i--)
#define ll long long int
#define ld long double
#define llu long long unsigned
#define pb push_back
#define mod 1e9+7

/*
                    ** author **
                ** Parth Lathiya **
    ** https://www.cse.iitb.ac.in/~parthiitb/ **
*/



int main()
{

ios::sync_with_stdio(false);

#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
#endif

freopen("A-large.out","w",stdout);

//  --------------------------------------------------------------------------------------

    ll T;
    cin>>T;
    ll bk=T;
    while(T--)
    {
        string a;
        int k;
        cin>>a>>k;
        int f=0,cnt=0;
        rep(i,0,a.length())
        {
            if(a[i]=='-')
            {
                if(i+k>a.length())
                    {f=1;break;}
                else
                {
                    cnt++;a[i]=='+';
                    rep(j,1,k)
                    {
                        a[i+j]=(a[i+j]=='-')?'+':'-';
                    }
                }
            }
        }
        if(f==1) 
            cout<<"Case #"<<bk-T<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<bk-T<<": "<<cnt<<endl;

    }

//  --------------------------------------------------------------------------------------

return 0;
}
