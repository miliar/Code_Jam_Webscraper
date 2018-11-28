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
        int n, k;
        cin>>n>>k;
        cout<<"Case #"<<T<<": ";
        map<ll,int> m;
        priority_queue<ll> q;
        q.push(n);
        m[n]=1;
        while(!q.empty())
        {
            ll b = q.top();
            q.pop();

            k -= m[b];
            if(k<=0)
            {
              cout<<b/2<<" "<<(b-1)/2<<endl;
              break;
            }
            //cout<<k<<" "<<b<<endl;
            if(b%2)
            {
                ll c = b/2;
                if(m[c] == 0)
                    q.push(c);
                m[c] += (2*m[b]);
            }
            else
            {
                ll c = b/2;
                if(m[c] == 0)
                    q.push(c);
                m[c] += m[b];
                c--;
                if(m[c] == 0)
                    q.push(c);
                m[c] += m[b];
            }
        }
    }
    return 0;
}

