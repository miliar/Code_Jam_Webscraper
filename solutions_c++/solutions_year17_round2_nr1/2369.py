#include <bits/stdc++.h>
 
using namespace std;

using llong = long long;
using ld = long double;
using ii = pair<int,int>;
using ull = unsigned long long;


#define endl "\n"
#define fi first
#define se second
#define left LEVO
#define right PRAVO
#define time CHAS
#define prev PAPEREDNIKXD
#define next NASTUPNIKXD
#define pb push_back
#define deb cout<<"CHECK\n";
 
#define elif else if
#define cclear cout<<flush;
#define fclear fflush(stdout);
#define files freopen("melman.in","r",stdin);freopen("melman.out","w",stdout);
#define kchay ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
 
const llong over999 = 1e8;
const double eps = 1e-16;
const double Pi = acos(-1);
const llong md = 1e9+7;
/*****()***********************************************************/


main() {
    kchay;
    int test;
    cin >> test;
    cout << fixed << setprecision(6);
    for(int tcase = 1; tcase<=test; tcase++)
    {
        cout << "Case #" << tcase << ": ";
        ld time = 0, d, x, v;
        int n;
        cin >> d >> n;
        for(int i=0;i<n;i++)
        {
            cin >> x >> v;
            time = max(time, (d-x)/v);
        }
        cout << d/time << endl;
    }
    return 0;
}