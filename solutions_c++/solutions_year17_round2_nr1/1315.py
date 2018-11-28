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

int main() {

    ll t;

    cin>>t;

    for (ll i = 1; i <=t; i++) {

        ld d,n;
        cin>>d>>n;
        ld max=0;
        while (n--)
        {
            ld k,s;
            cin>>k>>s;
            k=d-k;

            ld time=k/s;

            if(time>max)
                max=time;

        }

    cout<<"Case #"<<i<<": ";
        printf("%lf\n",d/max);

    }



    return 0;
}
