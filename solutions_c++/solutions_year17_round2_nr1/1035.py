#include<bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define lol long long
#define ld long double
#define db double
#define x first
#define y second
#define j1 sdfdsf
#define y0 gjkldf
#define fc cin.tie(NULL);ios_base::sync_with_stdio(false);

using namespace std;

const int N = 1e3+5;
const int M = 1e3;
const int inf = 2e9;
const int md = 1e9+7;
const db eps = 1e-6;

int t,n,it,i;
ld D,ans;
pair<ld, ld> a[N];

int main()
{
    fc

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);


    cin>>t;
    it = 0;
    while (t--)
    {
        cin>>D>>n;
        for (i=1; i<=n; ++i)
         cin>>a[i].x>>a[i].y;

       sort(a+1, a+n+1);
       ans = D / ((D - a[1].x) / a[1].y);

       for (i=2; i<=n; ++i)
        ans = min(ans, D / ((D - a[i].x) / a[i].y));

       ++it;
       cout<<"Case #"<<it<<": ";

       cout.precision(6);
       cout<<fixed<<ans<<"\n";

    }
}
