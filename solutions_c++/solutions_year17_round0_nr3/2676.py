#include <bits/stdc++.h>
using namespace std;
typedef long long int ll; 
typedef vector<ll> vll;
typedef pair<ll,ll> pll;
#define pb push_back
#define endl '\n'
#define f first
#define s second
#define forn(i,n) for(int i = 0; i < int(n); i++)
const ll INF = 1e9, MOD = 1e9+7;
ll e2[100];
int main()
{
    ios_base::sync_with_stdio(false);
    e2[0] = 1;
    for(int i = 1; i < 70; i++) e2[i] = e2[i-1]*2;
    int t;
    cin >> t;
    for(int casen = 1; casen <= t; casen++)
    {
        ll n, k;
        cin >> n >> k;
        cout << "Case #" << casen << ": ";
        ll currk = 0, currmax = n, step;
        for(step = 0; currk + e2[step] < k; step++)
        {
            // if(currk + e2[step] < k)
            currk += e2[step];
            currmax = (currmax - 1)/2;
        }
        // cout << currmax << " " << currk << " " << step << endl;
        // cout << "VAL = " << 
        if(k <= n - e2[step]*currmax)
        {
            // cout << "CHECK!!" << endl;
            cout << (currmax+1)/2 << " " << currmax/2 << endl;
        }
        else
            cout << currmax/2 << " " << (currmax-1)/2 << endl;


    }
    return 0;
}