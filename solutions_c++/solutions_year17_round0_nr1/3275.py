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
        string s;
        int n;
        cin>>s>>n;
        cout<<"Case #"<<T<<": ";
        int cnt = 0, c=0;
        rep(i, 0, s.size())
        {
            if(s[i]=='-')
                c++;
            if(s[i]=='+' && c)
            {
                int rem = n-c;
                for(int j=i; rem ; j++, rem--)
                s[j] = (s[j]=='+' ? '-' : '+');
                i--;
                cnt++;
                c=0;
            }
            if(c==n)
            {
                cnt++;
                c=0;
            }
        }
        if(c)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<cnt<<endl;
    }
    return 0;
}

