#include <bits/stdc++.h>

using namespace std;


#define Set(a, s) memset(a, s, sizeof (a))
#define rep(i, x, y) for(int i = x; i < y; i++)
#define Rep(i, x, y) for(int i = x; i <= y; i++)
#define vi vector<int>
#define vvi vector<vector<int> >
#define vp vector< pair< int, int > >
#define point pair<double, double >
#define pb push_back
#define mp make_pair
#define eps pow(10.0,-9.0)
#define MOD 1000000007
#define oo 1e18
#define Maxi 250000

#define prim 31
typedef unsigned long long ull;
typedef long long ll;


int main()
{
    //ios_base::sync_with_stdio(0);
    freopen("input.in","r", stdin);
    freopen("output.out","w", stdout);
    //Sieve(1000000);

    int t;
    cin>>t;
    for(int T=1 ; T<=t ; T++)
    {
        int n;
        double d, s, k, mini = INT_MIN;
        cin>>d>>n;
        cout<<"Case #"<<T<<": ";
        rep(i, 0, n)
        {
         cin>>s>>k;
         mini = max(mini, (d-s)/k);
        }
        cout<<setprecision(6)<<fixed<<d/mini<<endl;
    }
    return 0;
}

