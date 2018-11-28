#include<bits/stdc++.h>
#define ll long long
#define fin(x) scanf("%lld",&x)
#define fout(x) printf("%lld\n",x)
#define pll pair<ll,ll>
#define mp(x,y) make_pair(x,y)
#define cases int t;  scanf("%d",&t);   while(t--)
#define MOD 1000000007
#define MAXN 1234567
#define read() freopen("input.txt","r",stdin)
#define write() freopen("output.txt","w",stdout)

using namespace std;

int main()
{
    read();
    write();
    ll TC = 0;
    cases
    {
        TC++;
        ll n, N;
        fin(n);
        N = n;
        vector <ll> v;
        while(n)
        {
            v.push_back(n % 10);
            n /= 10;
        }
        reverse(v.begin(), v.end());
        if(N < 10)
        {
            cout << "Case #" << TC << ": " << N << endl;
            continue;
        }
        else
        {
            ll i = 0;
            while(i < v.size() - 1)
            {
                if(v[i] > v[i + 1])
                {
                    v[i] -= 1;
                    for(ll j = i + 1; j < v.size(); j++)
                    {
                        v[j] = 9;
                    }
                    i = 0;
                }
                else
                    i++;
            }
            i = 0;
            for(i = 0; i < v.size(); i++)
            {
                if(v[i] != 0)
                    break;
            }
            cout << "Case #" << TC << ": ";
            for(; i < v.size(); i++)
                cout << v[i];
            cout << endl;
        }
    }
    return 0;
}
