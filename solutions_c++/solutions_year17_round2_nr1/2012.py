#include <bits/stdc++.h>

#define mod 1000000007
#define inf 1000000000000LL
#define root2 1.41421
#define root3 1.73205
#define pi 3.14159
#define MAX 100001
#define cntbit __builtin_popcountll
#define ll long long int
#define PII pair<int, int>
#define f first
#define s second
#define mk make_pair
#define PLL pair<ll, ll>
#define gc getchar
#define pb push_back

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ca=1, t, n, i;
    double tm, k, d, s;
    cin>>t;
    while(ca<=t)
    {
        cout<<"Case #"<<ca<<": ";ca++;
        tm=0;
        cin>>d>>n;
        for(i=0;i<n;i++)
        {
            cin>>k>>s;
            tm=max(tm, (d-k)/s);
        }
        printf("%0.6lf\n", d/tm);
    }
    return 0;
}
