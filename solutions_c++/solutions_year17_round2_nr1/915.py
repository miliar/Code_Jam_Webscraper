
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout<<#x " = "<<(x)<<endl
#define un(x)       x.erase(unique(x.begin(),x.end()), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pb          push_back
#define mp          make_pair
#define xx          first
#define yy          second
#define hp          (LL) 999983
#define MAX         100000
#define eps         1e-9
#define pi          acos(-1.00)
typedef long long int LL;
typedef pair<int,int> pii;


int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k, t;
    int d, n, ki, si, cs;
    double mx;

    sf(t);
    for(cs = 1; cs <= t; cs++)
    {
        mx = 0.0;
        sff(d, n);
        for(i = 1; i <= n; i++)
        {
            sff(ki, si);
            mx = max(mx, (d - ki) / (double) si);
        }

        printf("Case #%d: %0.10f\n", cs, d / mx);
    }
    return 0;
}






