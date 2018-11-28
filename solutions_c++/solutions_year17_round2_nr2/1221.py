#include <bits/stdc++.h>

#define ll long long
#define M 1000000007
#define INF 99999999999999999 // 9223372036854775807
#define mp(x, y) make_pair(x,y)
#define pb(x) push_back(x)
#define pmp(x, y) pb(mp(x,y))
#define ld double
#define PI 3.14159265
#define len(a) (ll)a.size()    //
#define F first
#define S second
#define endl "\n"
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;

char a[10000000];


int main() {

    ll t;
	fast();
    cin >> t;

    for (ll hell = 1; hell <= t; hell++) {

        ll n,r,o,y,g,b,v;
        
        cin>>n>>r>>o>>y>>g>>b>>v;

        ll mx=max({r,y,b});

        ll left=r+y+b-mx;

        char var;

        if(mx==r)
            var='R';
        else if(mx==y)
            var='Y';
        else
            var='B';

        if(mx>left)
        {
            cout << "Case #" << hell << ": IMPOSSIBLE\n";
            continue;
        }

        for (ll j = 0; j < 1000000; j++) {
            a[j]='x';
        }


        for (ll j = 0,cnt = 0 ; cnt < mx; j+=3,cnt++) {
            a[j]=var;
        }


        if(var=='R')            //redddd
        {
            ll j=1;
            for (ll cnt=0; cnt < y; j+=3,cnt++) {       //yellow
                a[j]='Y';
            }

            for (ll cnt=0,j = 3*r-1; cnt < b; j-=3,cnt++) {         //blue
                    
                a[j]='B';
            }
        }

        else if(var=='Y')
        {
            ll j=1;
            for (ll cnt=0; cnt <r; j+=3,cnt++) {       //red
                a[j]='R';
            }

            for (ll cnt=0,j = 3*y-1; cnt < b; j-=3,cnt++) {         //blue

                a[j]='B';
            }

        }

        else if(var=='B')
        {
            ll j=1;
            for (ll cnt=0; cnt <r; j+=3,cnt++) {       //red
                a[j]='R';
            }

            for (ll cnt=0,j = 3*b-1; cnt < y; j-=3,cnt++) {         //blue

                a[j]='Y';
            }


        }

        string ans="";

        for (ll j = 0; j < 30000; j++) {
            if(a[j]!='x')
                ans+=a[j];
        }
        
        
        cout << "Case #" << hell << ": " << ans<<endl;

    }


    return 0;
}
