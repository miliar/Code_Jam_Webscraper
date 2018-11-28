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
	freopen("B-large.in","r",stdin);
#endif

freopen("B-large.out","w",stdout);

//  --------------------------------------------------------------------------------------

    ll T;
    cin>>T;
    ll bk=T;
    while(T--)
    {
        string t;
        cin>>t;

        for(int i=t.length()-1;i>0;i--)
        {
            if(t[i]<t[i-1])
            {
                t[i-1]--;
                rep(j,i,t.length())
                {
                    t[j]='9';
                }
            }
        }
        cout<<"Case #"<<bk-T<<": ";
        int f=0;
        int i=0;
        while(t[i]=='0')i++;
        rep(j,i,t.length())
        {
            cout<<t[j];
        }
        cout<<endl;
    }

//  --------------------------------------------------------------------------------------

return 0;
}
