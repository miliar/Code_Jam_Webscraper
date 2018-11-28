#include <bits/stdc++.h>
#define INF 1000000009
#define mod 1000000007
#define PI 3.14159
#define vi vector<int>
#define ll long long
#define ii pair<int, int>
#define pll pair<ll, ll>
#define vii vector<ii>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define mt make_tuple
#define eb emplace_back
#define CLR(arr) memset(arr, 0, sizeof(arr))
#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;

typedef pair<int, double> typ;

bool comp(typ x, typ y)
{
    return x.fs<y.fs;
}


int main()
{
    freopen("inp.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int ctr=1; ctr<=T; ++ctr)
    {
        int D, N;
        cin>>D>>N;
        vector<typ> V;
        for(int i=0; i<N; ++i)
        {
            int K;
            double S;
            cin>>K>>S;
            V.eb(D-K, S);
        }
        sort(V.begin(), V.end(), comp);
        double tim = V[0].fs/V[0].sc;

        for(int i=1; i<N; ++i)
        {
            double tp = V[i].fs/V[i].sc;
            if(tp < tim)
                V[i].sc = V[i].fs/tp;
            else
                tim = tp;
        }
        double ans = 0;
        ans = D/tim;
        cout<<"Case #"<<ctr<<": ";
        printf("%.6f\n", ans);

    }
    return 0;
}
