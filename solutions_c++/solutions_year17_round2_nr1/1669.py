#include <bits/stdc++.h>
using namespace std;

#define sz(v)        ((int)v.size())
#define ll           long long
#define all(v)       (v.begin()) , (v.end())
#define rall(v)      (v.rbegin()) , (v.rend())
#define SetTo(v, a)  memset(v,a,sizeof(v))

int pos[1005], speed[1005];

int main ()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int tc, n, d;
    cin >> tc;
    for(int test = 1;test <= tc;test++){
        printf("Case #%d: ", test);
        scanf("%d%d", &d, &n);
        for(int i=0;i<n;i++){
            scanf("%d%d", pos + i, speed + i);
        }
        long double ans , tmp;

        ans = 1.0 * (d - pos[n-1])/speed[n-1];

        for(int i=n-2;i>=0;i--){
            tmp = 1.0 * (d - pos[i])/speed[i];
            ans = max(ans, tmp);
        }


        cout << fixed << setprecision(6) << (1.0*d/ans) << endl;

    }
    return 0;
}
