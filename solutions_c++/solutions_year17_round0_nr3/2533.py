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
	freopen("C-large.in","r",stdin);
#endif

freopen("C-large.out","w",stdout);

//  --------------------------------------------------------------------------------------

    ll T;
    cin>>T;
    ll bk=T;
    while(T--)
    {
        llu n,k;
        cin>>n>>k;

        map<llu,llu> my;
        my[n]=1;
        while(1)
        {
            llu mx=my.rbegin()->first;
            // cout<<mx<<" "<<k<<" "<<my[mx]<<endl;
            if(mx%2==0)
            {
                my[mx/2] += my[mx];
                my[(mx/2)-1] += my[mx];
                if(k<=my[mx]){cout<<"Case #"<<bk-T<<": "<<mx/2<<" "<<(mx/2)-1<<endl;break;}
                k -= my[mx];
                my.erase(mx);
            }
            else
            {
                my[mx/2] += 2*my[mx];
                if(k<=my[mx]){cout<<"Case #"<<bk-T<<": "<<mx/2<<" "<<mx/2<<endl;break;}
                k -= my[mx];
                my.erase(mx);
            }
        }
        // cout<<my[500]<<endl;
    }

//  --------------------------------------------------------------------------------------

return 0;
}