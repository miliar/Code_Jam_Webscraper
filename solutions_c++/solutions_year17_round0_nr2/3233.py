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
        ll n;
        cin>>n;
        cout<<"Case #"<<T<<": ";
        vi v;
        while(n)
        {
            v.pb(n%10);
            n/=10;
        }
        bool r = 0;
        for(int i = (int)v.size()-2 ; i>=0 ; i--)
        {
            if(v[i]<v[i+1])
            {
                int idx = i;
                for(int j = i+1 ; j<v.size() ; j++)
                {
                    if(v[j]>v[j-1])
                    {
                        v[j]--;
                        idx = j-1;
                    }
                    if(!v[j])
                        r=1;
                }
                if(r) break;
                for(int j = idx ; j>=0 ; j--)
                    v[j] = 9;
            }
        }

        if(r)
            rep(i,0,(int)v.size()-1)
            cout<<9;
        else
            for(int i = (int)v.size()-1 ; i>=0 ; i--)
                cout<<v[i];
        cout<<endl;
    }
    return 0;
}

